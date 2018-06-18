#!/usr/bin/env python
# coding=utf-8

# https://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000/0013868196352269f28f1f00aee485ea27e3c4e47f12bc7000


# 切片
L = ["michael", "sarah", "tracy", "Bob", "Jack"]
print [L[0], L[1]]

r = []
n = 3
for i in range(n):
    r.append(L[i])
print r

# 使用切片
print L[0:3]
print L[0:10]

# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
# 如果索引是0的话 可以省略
print L[:4]

# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：
# 表示倒数的两个
print '取倒数两个数', L[-2:]
# 倒数第二个
print L[-2:-1]

# 记住倒数第一个是-1 然后倒数第二个是 -2
L = range(100)

print L[:10]
print L[-10:]
print L[10:20]
print L[10:20:2]
print L[::5]

p = L
print '打印L', p

o = L[:]
print o

test = (1, 2, 3, 4, 6, 76, 778, 9)[::2]
print test

# ############################################
# 迭代


# 可以看出，Python的for循环抽象程度要高于Java的for循环，因为Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。
#
# list这种数据类型虽然有下标，但很多其他数据类型是没有下标的，但是，只要是可迭代对象，无论有无下标，都可以迭代，比如dict就可以迭代：
d = {"a": 5, "b": 6, "c": 7}
for key in d:
    print key

for k in d.iterkeys():
    print k

for value in d.itervalues():
    print value

for k, v in d.iteritems():
    print k + " " + str(v)
# 因为dict的存储不是按照list的方式顺序排列，所以，迭代出的结果顺序很可能不一样。
#
# 默认情况下，dict迭代的是key。如果要迭代value，可以用for value in d.itervalues()，如果要同时迭代key和value，可以用for k, v in d.iteritems()。
#
# 由于字符串也是可迭代对象，因此，也可以作用于for循环：

for ch in "ABC":
    print ch

from collections import Iterable

print isinstance("abc", Iterable)
print isinstance([1, 2, 3], Iterable)
print isinstance(123, Iterable)
# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？
# Python内置的enumerate函数可以把一个list变成索引-元素对，
# 这样就可以在for循环中同时迭代索引和元素本身：

for i, key in enumerate(d):
    value = d[key]
    print '按照下标循环', i, key, value

    print value

# 上面的for循环里，同时引用了两个变量，在Python里是很常见的，比如下面的代码：
for x, y in [(1, 2), (3, 4)]:
    print x, y

# 任何可迭代对象都可以作用于for循环，包括我们自定义的数据类型，只要符合迭代条件，就可以使用for循环。
