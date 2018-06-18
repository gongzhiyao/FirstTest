#!/usr/bin/env python
# coding=utf-8
print(u"哈哈哈")
classmates = ['Michael', 'Bob', 'Tracy']
print classmates

print len(classmates)

print classmates[0]
print classmates[1]
print classmates[2]

# 取最后一个
print classmates[-1]

classmates.append("Adam")
print classmates

classmates.insert(1, "Jack")
print  classmates

print classmates.pop(1)
classmates[0] = "Tom"
print classmates

L = ["apple", 123, True]

p = ["asp", 'php']

s = ["pytyon", "java", p, "scheme"]

print s[2][1]

classmates = ("michael", "Bob", "Tracy")
print classmates[2]

# 这个是简单的赋值
# t = (1)

# 为了消除歧义  这个是tuple 不可变数组
# t = (1,)
# 以下代码会执行失败
# t[0] = 11

# 表面上看，tuple的元素确实变了，
# 但其实变的不是tuple的元素，而是list的元素。
# tuple一开始指向的list并没有改成别的list，
# 所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
# 即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！

t = ("a", "b", ["A", "B"])
t[2][0] = "X"
t[2][1] = "Y"
print t

# age=20
# if age>=18:
#     print "your age is",age
#     print "adult"
# else:
#     print "your age is",age
#     print "young man"

# age = input("young man ,tell me you age")
age = 19
if age >= 18:
    print u"oh！ you are a real man"
elif age >= 6:
    print "you are a teeger"
else:
    print "you are a kid"

x = 1
if x:
    print "666"

list = [1, 2, 3]
for item in list:
    print item

# for 运算
sum = 0
numList = [12, 33, 21, 45, 56, 34, 2]
for num in numList:
    sum = sum + num
print sum

sum = 0
for i in range(101):
    print sum, "+", i, "=", sum + i
    sum = sum + i

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum
