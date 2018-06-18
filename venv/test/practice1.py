#!/usr/bin/env python
# coding=utf-8

print "6666"

# birth = int(raw_input("birth:"))
birth = 1994
if birth < 2000:
    print "00前"
else:
    print "00后"

while False:
    print "dead lock"

# dict

# 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。
#
# 和list比较，dict有以下几个特点：
#
# 查找和插入的速度极快，不会随着key的增加而增加；
# 需要占用大量的内存，内存浪费多。
# 而list相反：
#
# 查找和插入的时间随着元素的增加而增加；
# 占用空间小，浪费内存很少。
# 所以，dict是用空间来换取时间的一种方法。


d = {"michael": 95, "Bob": 75, "Tracy": 85}
if "michael" in d:
    print d['michael']
    d["michael"] = 66
    print d["michael"]

value = d.get("michael", -2)
if value != -2:
    print value

# dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
#
# 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
#
# 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key：

# 这种赋值是报错  dict的key 不可以改变
# key =[1,2,3]
# d[key] = "a list"


# set
# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
#
# 要创建一个set，需要提供一个list作为输入集合：
s = set([1, 2, 3])
print s

s = set([1, 2, 2, 3, 3, 4, 4, 4, 4, 4, 44, 4, ])
s.add("55")
s.remove(44)
print  s
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print s1 & s2
print s1 | s2
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。
list = [1, 2, 3]
# 以下这个会报错 因为set里面不能够放置可变数据 比如list
# s3= set([list])
# 下面这个是模块，可以的
s3 = set(list)
print s3

# 同样下面的dict也会报错
# d1={(1, [2, 3]):1}
# print d1







