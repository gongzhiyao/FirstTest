#!/usr/bin/env python
# coding=utf-8
# 函数式编程
print "函数式编程"
# 高阶函数
# 变量可以指向函数
print abs(-120)
print abs
# 可见，abs(-10)是函数调用，而abs是函数本身。
# 要获得函数调用结果，我们可以把结果赋值给变量：

x = abs(-100)
print x
# 如果把函数自身赋值给变量
a = abs
print a
# 结论：函数本身也可以赋值给变量，即：变量可以指向函数。
# 如果一个变量指向了一个函数，那么，可否通过该变量来调用这个函数？用代码验证一下：
print a(-10000)
# 成功！说明变量f现在已经指向了abs函数本身。


# 函数名也是变量

# 那么函数名是什么呢？函数名其实就是指向函数的变量！对于abs()这个函数，完全可以把函数名abs看成变量，它指向一个可以计算绝对值的函数！
# 如果把abs指向其他对象，会有什么情况发生？
# abs = 10
print abs(-100)


# 把abs指向10后，就无法通过abs(-10)
# 调用该函数了！因为abs这个变量已经不指向求绝对值函数了！
# 当然实际代码绝对不能这么写，这里是为了说明函数名也是变量。要恢复abs函数，请重启Python交互环境。
# 注：由于abs函数实际上是定义在__builtin__模块中的，所以要让修改abs变量的指向在其它模块也生效，要用__builtin__.abs = 10。

# 传入函数
# 既然变量可以指向函数，函数的参数能接收变量，那么一个函数就可以接收另一个函数作为参数，这种函数就称之为高阶函数。
# 一个最简单的高阶函数

# 把函数作为参数传进去，称为高阶函数
def add(x, y, f):
    return f(x) + f(y)


abs_result = add(1, -1113, abs)
print abs_result


# 小结
# 把函数作为参数传入，这样的函数称为高阶函数，函数式编程就是指这种高度抽象的编程范式。
#


# map/reduce


def f(x):
    if isinstance(x, (int, float)):
        return x * x
    else:
        return 0


L = [1, 2, 3, 4, 5, 5, 66, "a", "b2", "c"]
print map(f, L)

# 如果不使用map的话 同样可以使用for循环来实现

S = []
for i in L:
    if not isinstance(i, (int, float)):
        i = 0
    S.append(i * i);
print S
# 的确可以，但是，从上面的循环代码，能一眼看明白“把f(x)作用在list的每一个元素并把结果生成一个新的list”吗？
# 所以，map()作为高阶函数，事实上它把运算规则抽象了，因此，我们不但可以计算简单的f(x)=x2，还可以计算任意复杂的函数，比如，把这个list所有数字转为字符串：
print map(str, [1, 2, 3, 445, 5, 6, 6, 67, 7, 78, 8, 8, 8, 8, ])


# 这样子的话  只需要一行代码

# #再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
#  reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)


# 比如给一个序列求和,可以使用reduce来实现
def abs_add(x, y):
    if isinstance(x, (int, float)) & isinstance(y, (int, float)):
        return abs(x) + abs(y)
    else:
        return abs(x) + 0


print reduce(abs_add, [1, 2, 3, 3, 4, 4, 556, 6, "SDSDSSSS", 33333])


# 当然求和运算可以使用sum  不用使用reduce就可以
# 但是如果是进行复杂的运算  就得用reduce了

def change_big_num(x, y):
    return x * 10 + y


print reduce(change_big_num, [1, 2, 3, 4, 5, 6, 6])


# 这个例子本身没多大用处，但是，如果考虑到字符串str也是一个序列，对上面的例子稍加改动，配合map()，我们就可以写出把str转换为int的函数：

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}[s]


# 这个是 reduce和map 结合
print reduce(change_big_num, map(char2num, ['1', '2', '3']))

print {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4}['1']


# 下面整合成一个str2int 的方法是
def str2int(s):
    def change_big_num(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(change_big_num, map(char2num, s))


print str2int('0123456789')


# 可以使用lambda 函数进行简化
# todo


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


def char2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# filter 用于过滤
# Python内建的filter()函数用于过滤序列。
# 和map()类似，filter()也接收一个函数和一个序列。和map()不同的时，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 例如在一个list里面，删除偶数，只保留奇数。

def is_odd(x):
    return x % 2 == 1


L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, -1, -2]

print filter(is_odd, L)


# 删除数组中的空串
def is_not_blank(s):
    return s and s.strip()


print filter(is_not_blank, ["", "1", "2", "2", "3", "33333"])


def is_suShu(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


print filter(is_suShu, range(2, 100))
# sort 排序算法

# Python内置的sorted()函数就可以对list进行排序：
print sorted([99, 23, 3, 4, 1, 0])


# 此外，sorted()函数也是一个高阶函数，它还可以接收一个比较函数来实现自定义的排序。比如，如果要倒序排序，我们就可以自定义一个reversed_cmp函数：
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    else:
        return 0


print sorted([1, 2, 32, 34, 4, 5, 52, 32, 34, 1123, 42, 4131, 1], reversed_cmp)

# 按照acsII 码进行排序  先是数字  然后大写字母 然后小写字母
print sorted(["ZSSSS", "a", "A", 1223, "zssddf"])


# 默认情况下，对字符串排序，是按照ASCII的大小比较的，由于'Z' < 'a'，结果，大写字母Z会排在小写字母a的前面。
# 现在，我们提出排序应该忽略大小写，按照字母序排序。要实现这个算法，不必对现有代码大加改动，只要我们能定义出忽略大小写的比较算法就可以

def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 > u2:
        return -1
    if u1 < u2:
        return 1
    else:
        return 0


# 忽略大小写来比较两个字符串，实际上就是先把字符串都变成大写（或者都变成小写），再比较。
# 这样，我们给sorted传入上述比较函数，即可实现忽略大小写的排序：

print sorted(["A", "a", "s", "Z"], cmp_ignore_case)



