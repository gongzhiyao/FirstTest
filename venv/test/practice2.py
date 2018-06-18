#!/usr/bin/env python
# coding=utf-8

# 函数
r1 = 12.34
r2 = 9.08
r3 = 73.1
s1 = 3.14 * r1 * r1
s2 = 3.14 * r2 * r2
s3 = 3.14 * r3 * r3

# 内置函数
print abs(100)
print abs(-20)
# 传参不对 报错
# print abs(1,1)


print cmp(1, 2)
print cmp(-1, -3)
print cmp(0, 0)

# 数据类型转换
print int("123")

print int(12.334)

print float("12.34")

print str(1.233)

print unicode(100)

print unicode("fff")

print bool(1)

print bool("")

a = abs
print a(-100)


# 自定义函数


def my_abs(x):
    if x > 0:
        return x
    else:
        return -x


print my_abs(-25)


# 定义空函数
def nop():
    pass


# 或者在代码中  没有想好下步怎么写  也可以pass

def test(x):
    if x > 100:
        pass


# 加上了入参判断
def my_new_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError("bad operand type")
    if x >= 0:
        return x
    else:
        return -x


print my_new_abs(-25)

# 定义函数时，需要确定函数名和参数个数；
#
# 如果有必要，可以先对参数的数据类型做检查；
#
# 函数体内部可以用return随时返回函数结果；
#
# 函数执行完毕也没有return语句时，自动return None。
#
# 函数可以同时返回多个值，但其实就是一个tuple。


import math


def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


print move(100, 100, 60, math.pi / 6)
x, y = move(100, 100, 60, math.pi / 6)
print x, y


def power(x):
    if isinstance(x, (int, float)):
        return x * x
    else:
        raise TypeError("error")


print power(100)


def power_new(x, n=2):
    if isinstance(x, (int, float)) and isinstance(n, (int, float)):
        result = 1
        while n > 0:
            result = result * x
            n = n - 1
        return result


print power_new(10, 4)

print power_new(10)


def enroll(name, gender, age=6, city="beijing"):
    print "name:", name
    print "gender:", gender
    print "age:", age
    print "city:", city


enroll("Sarah", "F")
enroll('Bob', 'M', 7)
# 这个可以可选的修改某个默认字段
enroll('Adam', 'M', city='Tianjin')


def add_end(L=[]):
    L.append("END")
    return L


print  add_end([1, 2, 3])
print add_end(["hello"])
print add_end()
print add_end()


# 多次调用会出现 L 数组变化的情况   每次执行 都会把L进行计算 然后默认参数内容就会变化
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！
# 要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end_new(O=None):
    if O is None:
        O = []
    O.append("END")
    return O


print add_end_new()
print add_end_new()


# 为什么要设计str、None这样的不变对象呢？因为不变对象一旦创建，对象内部的数据就不能修改，这样就减少了由于修改数据导致的错误。此外，由于对象不变，多任务环境下同时读取对象不需要加锁，同时读一点问题都没有。我们在编写程序时，如果可以设计一个不变对象，那就尽量设计成不变对象。


# 可变参数
# ，可变参数就是传入的参数个数是可变的，可以是1个、2个到任意个，还可以是0个。

def calc(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print calc([1, 2, 3])
print calc([])


# 我们把函数的参数改为可变参数：
# 定义可变参数和定义list或tuple参数相比，仅仅在参数前面加了一个*号。在函数内部，参数numbers接收到的是一个tuple，因此，函数代码完全不变。但是，调用该函数时，可以传入任意个参数，包括0个参数
def calc_new(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print calc_new(1)
print calc_new(1, 2)
print calc_new()

nums = [1, 2, 3]
print calc_new(nums[1], nums[0])

print calc_new(*nums)


# 关键字参数
def person(name, age, **ext):
    print "name:", name, "age:", age, "other:", ext


person("michael", 18)
person("Bob", 35, city="beijing")
person("Adom", 30, gender="F", city="qingdao")
# 关键字参数有什么用？它可以扩展函数的功能。比如，在person函数里，我们保证能接收到name和age这两个参数，但是，如果调用者愿意提供更多的参数，我们也能收到。试想你正在做一个用户注册的功能，除了用户名和年龄是必填项外，其他都是可选项，利用关键字参数来定义这个函数就能满足注册的需求。

# 还有一种写法就是先组装成dict,然后根据dict 取key 和value 然后再传进去
kw = {"city": "Beijing", "job": "Enginner"}
person("Jack", 24, city=kw["city"], Job=kw["job"])

# 还有一种最便捷的写法  就是直接把 dict 传进去
person("676666", 29, **kw)


# 参数组合
# 在Python中定义函数，、
# 可以用必选参数、默认参数、可变参数和关键字参数，这4种参数都可以一起使用，
# 或者只用其中某些，但是请注意，
# 参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

def func(a, b, c=0, *args, **kw):
    print "a=", a, "b=", b, "c=", c, "args=", args, "kw=", kw


func(1, 2)
func(1, 2, c=3)
func(1, 2, 3, 4, 5, 6)
func(1, 2, 3, 3, 4, 5, 6, 67, x=99)

# 使用tuple 和 dict 都可以进行调用
t = (99, 98, 97)
d = {"name": 6666}

func(1, 2, 4, *t, **d)


# 小结
# Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。
#
# 默认参数一定要用不可变对象，如果是可变对象，运行会有逻辑错误！
#
# 要注意定义可变参数和关键字参数的语法：
#
# *args是可变参数，args接收的是一个tuple；
#
# **kw是关键字参数，kw接收的是一个dict。
#
# 以及调用函数时如何传入可变参数和关键字参数的语法：
#
# 可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；
#
# 关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。
#
# 使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。


# 递归函数
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
#
# 举个例子，我们来计算阶乘n! = 1 x 2 x 3 x ... x n，用函数fact(n)表示，可以看出：
#
# fact(n) = n! = 1 x 2 x 3 x ... x (n-1) x n = (n-1)! x n = fact(n-1) x n
#
# 所以，fact(n)可以表示为n x fact(n-1)，只有n=1时需要特殊处理。
#
# 于是，fact(n)用递归的方式写出来就是：
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)


print fact(1)
print fact(2)
print fact(5)
print fact(100)


# print fact(500)


# 使用递归函数需要注意防止栈溢出。
# 在计算机中，函数调用是通过栈（stack）这种数据结构实现的，
# 每当进入一个函数调用，
# 栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。
# 由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。可以试试fact(1000)：
# 确实报错了
# print fact(1000)


# 使用尾递归优化来防止 栈溢出
# 解决递归调用栈溢出的方法是通过尾递归优化，事实上尾递归和循环的效果是一样的，所以，把循环看成是一种特殊的尾递归函数也是可以的。
#
# 尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。


# 使用尾递归  减少栈的使用
def fact_new(result, n):
    if n == 1:
        return result
    result = result * n
    # print "result:",result
    return fact_new(result, n - 1)


print fact_new(1, 100)

# 使用递归函数的优点是逻辑简单清晰，缺点是过深的调用会导致栈溢出。
#
# 针对尾递归优化的语言可以通过尾递归防止栈溢出。尾递归事实上和循环是等价的，没有循环语句的编程语言只能通过尾递归实现循环。
#
# Python标准的解释器没有针对尾递归做优化，任何递归函数都存在栈溢出的问题。


example_empty_dict = {}
example_empty_dict["age"] = 16
print example_empty_dict
example_empty_dict["name"] = "Jack"
example_empty_dict["sex"] = "man"
print example_empty_dict

del example_empty_dict["sex"]
print example_empty_dict

example_empty_dict["birth"] = 2012
print example_empty_dict

print example_empty_dict.pop("name")
print example_empty_dict

# 遍历字典
dict_test = {
    "First_name": "Alex",
    "Last_name": "shaw",
    "Age": "27"
}

for key, value in dict_test.items():
    print "key:", key, "value:", value, "\n"

for items in dict_test.keys():
    print items
    print items.title()

print "*********************************"
# 按顺序遍历字典表中的所有键
sorted(dict_test)
for items in sorted(dict_test.keys()):
    print items.title()

# 遍历字典表中的所有value
for items in dict_test.values():
    print items.title()

# 集合set

print dict_test

dict_test["Age"] = 27
print dict_test

print "#######################################"
# 这个此时的Age已经被覆盖了
dict_new = {'First_name': 'Alex', 'Last_name': 'shaw', 'Age': '27', 'Age': 2}
for items in set(dict_new.keys()):
    print items.title()

for items in set(dict_new.values()):
    print (items)

print dict_new.values()

print dict_new

# 嵌套
# 1.字典列表
dict_test1 = {"First_name": "Alex", "Last_name": "Shaw", "Age": 27}
dict_test2 = {"First_name": "Poison", "Last_name": "Ash", "Age": 27}
list_people = [dict_test1, dict_test2]
for dict in list_people:
    print dict

# 自动生成列表中的字典元素
list_people = []
for people_info in range(30):
    new_people = {"First_name": "Alex", "Last_name": "Shaw", "Age": 20}
    list_people.append(new_people)

for people_info in list_people[:5]:
    print people_info

# 在字典中存储列表：
student = {"First_name": ["Alex"], "Last_name": ["Shaw"], "Score": ["99", "98", "88"],
           "like": ["moive", "skate", "sing", "coding"]}
print "the", student["First_name"], "\'s score is:\n"

# 循环字典中的列表
for keys, values in student.items():
    print "the item is :", keys.title(), "\n"
    for value in values:
        print "\t", value

# 在字典中存储字典
students = {
    "Alex": {
        "First_name": "Alex",
        "Last_name": "Shaw",
        "score": "97",
        "like": ["music", "skate"]
    },
    "poison": {
        "First_name": "Poison",
        "Last_name": "Polaris",
        "score": "77",
        "like": ["dancing"],
        "else": []
    }
}

# 定义一个字典，其中包含两个key：'Alex' and 'Poison'；与每个key相关联的
# value都是一个字典。此处嵌套的两个字典结构大致相同，python中没有要求字典结构
# 必须相同，但结构相同更方便for进行处理
print "#######################################"
for username, user_info in students.items():
    print "\nusername:", username
    print "\nuserInfo:", str(user_info)
    full_name = user_info["First_name"] + user_info["Last_name"]
    score = user_info["score"]
    print "\tFull_name:", full_name
    print "\tscore:", score
