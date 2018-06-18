# coding=utf-8

# 列表生成器

print range(1, 11)

# 但如果要生成[1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for i in range(1, 11):
    L.append(i * i)

print L
# 但是循环太繁琐，而列表生成式则可以用一行语句代替循环生成上面的list：
# 这个表达式 前面就是计算方法
L = [x * x for x in range(1, 11)]
print L

# 写列表生成式时要把生成的元素x*x 写在前面，后面跟for循环，就可以把list创建出来，
# 而且for循环后面还可以加上 if 语句判断

L = [x * x for x in range(0, 5) if x % 2 == 0]
print L

s = range(0, 100)
L = [x * x for x in s[::10]]
print L

# 这里使用的是两层循环，生成全排列
L = [m + n + z for m in "ABC" for n in "XYZ" for z in "123"]
print L

import os

d = [d for d in os.listdir(".")]
print d

# for循环其实可以同时使用两个甚至多个变量，比如dict的iteritems()可以同时迭代key和value：
d = {"x": "A", "y": "B", "z": "C"}
for k, v in d.iteritems():
    print "key=", k, "value=", v

for key, value in d.items():
    print key, "---", value
# 除了for in之外  还可以使用列表表达式来实现
L = [k + "=" + v for k, v in d.iteritems()]
print L

list = ["A", "B", "C", "D", "E", 1, 2222]

# L= [a.lower() for a in list ]
# print L

L = [a.lower() for a in list if not isinstance(a, (int, float))]
print L

for i in list:
    if isinstance(i, (int, float)):
        print i
    else:
        a = i.lower()
        print a

# 生成器


# 下面是列表生成式
L = [x * x for x in range(10)]
print L
# 下面是生成器
g = (x * x for x in range(10))
print g

# 我们讲过，generator保存的是算法，每次调用next()，就计算出下一个元素的值，直到计算到最后一个元素，没有更多的元素时，抛出StopIteration的错误。
#
# 当然，上面这种不断调用next()方法实在是太变态了，正确的方法是使用for循环，因为generator也是可迭代对象：


for x in range(0, 10):
    print "使用next获得：", g.next()

# 如果不重新设置列表生成器的话  会因为前面把所有的g.next 都取完  导致没有数据打印
# g = (x * x for x in range(10))
for n in g:
    print "\t", n

# print range(0,5)


L = ["Micheal", "Sarah", "Bob"]

print L[::3]

s = L[1:2]
print s

# 在这里测试一个  如果数据是空的话  for循环是否会报错
Q = []
for i in Q:
    print i


# 经过测试发现这样并不会报错


# 我们创建了一个generator后，基本上永远不会调用next()方法，而是通过for循环来迭代它。
#
# generator非常强大。如果推算的算法比较复杂，用类似列表生成式的for循环无法实现的时候，还可以用函数来实现。


# 写个生成斐波那契数列的方法  a是前面一个数  b 是后面一个数
def fib(max):
    n, a, b = 1, 1, 1
    while n < max:
        c = a
        a = b
        b = c + b
        n = n + 1
        print c


def fib_new(max):
    n, a, b = 0, 0, 1
    while (n < max):
        print b
        a, b = b, a + b
        n = n + 1


fib(10)


# fib_new(10)

# 仔细观察，可以看出，fib函数实际上是定义了斐波拉契数列的推算规则，可以从第一个元素开始，推算出后续任意的元素，这种逻辑其实非常类似generator。
#
# 也就是说，上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print b改为yield b就可以了：


def fib_generator(max):
    n, a, b = 1, 1, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1


fib_generator(10)


# 这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：


# 这里，最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
#
# 举个简单的例子，定义一个generator，依次返回数字1，3，5：

def odd():
    print 'step1:'
    yield 1
    print 'step2:'
    yield 2
    print 'step3'
    yield 3


o = odd()
print o.next()
print o.next()
print o.next()
# print o.next()

#   确实跟上面猜想的差不多  每次next的时候都会再从yield 的地方继续执行，相当于指针后移  所以在上面使用for循环 next之后再使用for循环直接打印列表生成器就会出现里面不存在数据的情况|

# 同样的，把函数改成generator后，我们基本上从来不会用next()来调用它，而是直接使用for循环来迭代：
# 一般情况下 我们很少使用next来循环generator，而是使用for循环
print "#########################################"
for i in odd():
    print i


# 还有一个就是for循环斐波那契数 看下

print "斐波那契生成器"
for g in fib_generator(10):
    print g
#
#小结
# generator是非常强大的工具，在Python中，可以简单地把列表生成式改成generator，也可以通过函数实现复杂逻辑的generator。
# 要理解generator的工作原理，它是在for循环的过程中不断计算出下一个元素，并在适当的条件结束for循环。对于函数改成的generator来说，遇到return语句或者执行到函数体最后一行语句，就是结束generator的指令，for循环随之结束。


