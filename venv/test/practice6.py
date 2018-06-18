#!/usr/bin/env python
# coding=utf-8

# 返回函数
# 函数作为返回值
# 高阶函数除了可以接受函数作为参数外，还可以把函数作为结果值返回。
# 我们来实现一个可变参数的求和。通常情况下，求和的函数是这样定义的：
def calc_sum(*args):
    ax = 0
    for n in args:
        ax = ax + n
    return ax


# 但是，如果不需要立刻求和，而是在后面的代码中，根据需要再计算怎么办？可以不返回求和的结果，而是返回求和的函数！

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax

    return sum


# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：
f = lazy_sum(1, 2, 3, 4, 5)
print f
# 调用函数f时，才真正计算求和的结果：
print f()

# 在这个例子中，我们在函数lazy_sum中又定义了函数sum，并且，内部函数sum可以引用外部函数lazy_sum的参数和局部变量，当lazy_sum返回函数sum时，相关参数和变量都保存在返回的函数中，
# 这种称为“闭包（Closure）”的程序结构拥有极大的威力。
# 请再注意一点，当我们调用lazy_sum()时，每次调用都会返回一个新的函数，即使传入相同的参数：


f1 = lazy_sum(1, 3, 5, 7, 9)
f2 = lazy_sum(1, 3, 5, 7, 9)
print f1 == f2


# 闭包

# 注意到返回的函数在其定义内部引用了局部变量args，所以，当一个函数返回了一个函数后，其内部的局部变量还被新函数引用，所以，闭包用起来简单，实现起来可不容易。
# 另一个需要注意的问题是，返回的函数并没有立刻执行，而是直到调用了f()才执行。我们来看一个例子：
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i

        fs.append(f)
    return fs


f1, f2, f3 = count()
# 在上面的例子中，每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
# 你可能认为调用f1()，f2()和f3()结果应该是1，4，9，但实际结果是：

print f1()
print f2()
print f3()


# 全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。
# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
# 如果一定要引用循环变量怎么办？方法是再创建一个函数，用该函数的参数绑定循环变量当前的值，无论该循环变量后续如何更改，已绑定到函数参数的值不变：


def count_new():
    fs = []
    for i in range(1, 4):
        def f(j):
            def g():
                return j * j

            return g

        fs.append(f(i))
    return fs


# 这样相当于把循环的状态都放到了g方法里面  所以每次执行的时候都是正确的数值了

f1, f2, f3 = count_new()
print f1()
print f2()
print f3()

# 匿名函数

# 当我们在传入函数时，有些时候，不需要显式地定义函数，直接传入匿名函数更方便。
# 在Python中，对匿名函数提供了有限支持。还是以map()函数为例，计算f(x)=x2时，除了定义一个f(x)的函数外，还可以直接传入匿名函数：

print map(abs, [1, 2, -200])

print map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])


# 通过对比可以看出，匿名函数lambda x: x * x实际上就是：

def f(i):
    return i * i


# 关键字lambda表示的是匿名函数，冒号前面的X表示的是函数参数
# 匿名函数有个限制就是只能够有一个表达式，不用谢return，返回值就是表达式的结果
# 用匿名函数有个好处就是以为函数没有名字，不必担心函数名冲突，此外匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量，再利用变量来调用该函数

f = lambda x: x * x
print f
print f(5)


# 也可以把匿名函数作为返回值返回
def build(x):
    return lambda x: x * x * x


print build(2)
b = build(1)
print b
print b(3)


# 从上面来看如果是需要入参的函数，并且返回的也是个函数的话  那么需要在先用个变量来接受下这个匿名函数，而且要有个入参，然后再调用的时候  需要执行这个变量 然后再设置入参，真正计算的是这个传入变量的参数的值

# 小结
# Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。


# 装饰器
# 由于函数也是一个对象，而且函数对象可以被赋值给变量，所以，通过变量也能调用该函数。

def now():
    print '2013-12-25'


f = now
f()

# 函数对象有一个__name__属性，可以拿到函数的名字：
print now.__name__
print f.__name__


# 现在，假设我们要增强now()函数的功能，比如，在函数调用前后自动打印日志，但又不希望修改now()函数的定义，这种在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
# 本质上，decorator就是一个返回函数的高阶函数。所以，我们要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print 'call %s()：' % func.__name__
        return func(*args, **kw)

    return wrapper


# 观察上面的log，因为它是一个decorator，所以接受一个函数作为参数，并返回一个函数。我们要借助Python的@语法，把decorator置于函数的定义处：
@log
def now_new():
    print '2018-6-17'


now_new()

# 调用now()函数，不仅会运行now()函数本身，还会在运行now()函数前打印一行日志
now_new = log(now_new)
now_new()


# 由于log()是一个decorator，返回一个函数，所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
# wrapper()函数的参数定义是(*args, **kw)，因此，wrapper()函数可以接受任意参数的调用。在wrapper()函数内，首先打印日志，再紧接着调用原始函数。
# 如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，写出来会更复杂。比如，要自定义log的文本：

def log_new(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print '%s %s:' % (text, func.__name__)
            return func(*args, **kw)

        return wrapper

    return decorator


# 这个3层嵌套的decorator用法如下：
@log_new("马上开始执行")
def test():
    print "this is a test"


test()

# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
test = log_new('马上开始执行')(test)

# 我们来剖析上面的语句，首先执行log('execute')，返回的是decorator函数，再调用返回的函数，参数是now函数，返回值最终是wrapper函数。
# 以上两种decorator的定义都没有问题，但还差最后一步。因为我们讲了函数也是对象，它有__name__等属性，但你去看经过decorator装饰之后的函数，它们的__name__已经从原来的'now'变成了'wrapper'：
print test.__name__
# 确实已经成了wrapper


# 因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。
# 不需要编写wrapper.__name__ = func.__name__这样的代码，Python内置的functools.wraps就是干这个事的，所以，一个完整的decorator的写法如下：


import functools


def log_new2(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s:' % func.__name__
        return func(*args, **kw)

    return wrapper


@log_new2
def test2():
    print "hello world"


test2()
print test2.__name__

# 或者针对带参数的decorator：


# 这个实现了函数的默认入参，  还有就是实现了调用前后的  代码执行
import functools


def log_new3(text="begin call"):
    def decrator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if text == None or text == "":
                _text = "empty"
            else:
                _text = text
            print "%s %s:" % (_text, func.__name__)
            result = func(*args, **kw)
            print "end call"
            return result

        return wrapper

    return decrator





@log_new3()
def test4():
    print "this is test4"


# test4 = log_new3("")(test4)


test4()
print test4.__name__

# import functools是导入functools模块。模块的概念稍候讲解。现在，只需记住在定义wrapper()的前面加上@functools.wraps(func)即可。

# 小结
# 在面向对象（OOP）的设计模式中，decorator被称为装饰模式。OOP的装饰模式需要通过继承和组合来实现，而Python除了能支持OOP的decorator外，直接从语法层次支持decorator。Python的decorator可以用函数实现，也可以用类实现。
# decorator可以增强函数的功能，定义起来虽然有点复杂，但使用起来非常灵活和方便。
