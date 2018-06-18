#!/usr/bin/env python
# coding=utf-8


# 面向对象编程

# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
# 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
# 而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。
# 我们以一个例子来说明面向过程和面向对象在程序流程上的不同之处。
# 假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：


student1 = {"name": "Michael", "score": 98}
student2 = {"name": "Bob", "score": 81}


# 而处理学生成绩可以通过函数实现，比如打印学生的成绩：
def print_score(student):
    print "%s:%s" % (student["name"], student["score"])


print_score(student1)


# 如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）。
# 如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。

class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print '%s:%s' % (self.name, self.score)


# 给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）。面向对象的程序写出来就像这样：

bart = Student("Bart Simpon", 59)
lisa = Student("Lisa Simpon", 87)

bart.print_score()
lisa.print_score()

# 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。
# Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，比如，Bart Simpson和Lisa Simpson是两个具体的Student：
# 所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。
# 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。

# 小结
# 数据封装、继承和多态是面向对象的三大特点，我们后面会详细讲解。


if __name__ == '__main__':
    print "调试代码"


# 类和实例
# 面向对象最重要的概念就是类（Class）和实例（Instance），必须牢记类是抽象的模板，
# 比如Student类，而实例是根据类创建出来的一个个具体的“对象”，每个对象都拥有相同的方法，但各自的数据可能不同。
# 仍以Student类为例，在Python中，定义类是通过class关键字：


class Student(object):
    pass


# class后面紧接着是类名，即Student，类名通常是大写开头的单词，紧接着是(object)，表示该类是从哪个类继承下来的，继承的概念我们后面再讲，
# 通常，如果没有合适的继承类，就使用object类，这是所有类最终都会继承的类。
# 定义好了Student类，就可以根据Student类创建出Student的实例，创建实例是通过类名+()实现的：


bar = Student()
print bar
# 可以看到，变量bar指向的就是一个Student的object，后面的0x10a67a590是内存地址，每个object的地址都不一样，而Student本身则是一个类。
# 可以自由地给一个实例变量绑定属性，比如，给实例bar绑定一个name属性：
bar.name = "Bart Simpson"

print bar.name


# 由于类可以起到模板的作用,因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

class Student_new(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
bob = Student_new("Bob", 99)
print  "name:%s,score:%s" % (bob.name, bob.score)


def print_score_new(student):
    print "name:%s,score:%s" % (student.name, student.score)


print_score_new(bob)


# 有了__init__方法，在创建实例的时候，就不能传入空的参数了，必须传入与__init__方法匹配的参数，但self不需要传，Python解释器自己会把实例变量传进去：


# 和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数。
# 除此之外，类的方法和普通函数没有什么区别，所以，你仍然可以用默认参数、可变参数和关键字参数


# 数据封装
# 面向对象编程的一个重要特征就是数据封装，在上面的student类上面，每个实例就拥有各自的name和score这些数据，我们通过函数来访问这些数据，比如打印一个学生的成绩

# >>> def print_score(std):
# ...     print '%s: %s' % (std.name, std.score)
# ...
# >>> print_score(bart)
# Bart Simpson: 59


# 但是，既然Student实例本身就拥有这些数据，要访问这些数据，就没有必要从外面的函数去访问，可以直接在Student类的内部定义访问数据的函数，这样，就把“数据”给封装起来了。这些封装数据的函数是和Student类本身是关联起来的，我们称之为类的方法：

class New_Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_score(self):
        return self.score

    def get_name(self):
        return self.name

    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"

    def get_student_info(self):
        return "name:%s,score:%s" % (self.name, self.score)


# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入：

Lisa = New_Student("Lisa", 98)

print Lisa.get_student_info()

# 这样一来，我们从外部看Student类，就只需要知道，创建实例需要给出name和score，而如何打印，都是在Student类的内部定义的，这些数据和逻辑被“封装”起来了，调用很容易，但却不用知道内部实现的细节。
# 封装的另一个好处是可以给Student类增加新的方法，比如get_grade：

print Lisa.get_grade()


# 小结
# 类是创建实例的模板，而实例则是一个一个具体的对象，各个实例拥有的数据都互相独立，互不影响；
# 方法就是与实例绑定的函数，和普通函数不同，方法可以直接访问实例的数据；
# 通过在实例上调用方法，我们就直接操作了对象内部的数据，但无需知道方法内部的实现细节。
# 和静态语言不同，Python允许对实例变量绑定任何数据，也就是说，对于两个实例变量，虽然它们都是同一个类的不同实例，但拥有的变量名称都可能不同：


# 访问限制

# 在Class内部，可以有属性和方法，而外部代码可以通过直接调用实例变量的方法来操作数据，这样，就隐藏了内部的复杂逻辑。
# 但是，从前面Student类的定义来看，外部代码还是可以自由地修改一个实例的name、score属性：

# >>> bart = Student('Bart Simpson', 98)
# >>> bart.score
# 98
# >>> bart.score = 59
# >>> bart.score
# 59


# 如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，
# 在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问，所以，我们把Student类改一改：


class Student_Private(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError("bad score")

    def set_name(self, name):
        if name == None or name == "":
            raise TypeError("bad param")
        else:
            self.__name = name

    def get_student_info(self):
        return "name:%s,score:%s" % (self.__name, self.__score)


white = Student_Private("Write simpon", 89)

print white.get_student_info()

# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：

# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：

# 如果又要允许外部代码修改score怎么办？可以给Student类增加set_score方法：


# 你也许会问，原先那种直接通过bart.score = 59也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数


white.set_name("sss")
white.set_score(99)


# 需要注意的是，在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，
# 特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。
# 有些时候，你会看到以一个下划线开头的实例变量名，比如_name，这样的实例变量外部是可以访问的，
# 但是，按照约定俗成的规定，当你看到这样的变量时，意思就是，“虽然我可以被访问，但是，请把我视为私有变量，不要随意访问”。
# 双下划线开头的实例变量是不是一定不能从外部访问呢？其实也不是。不能直接访问__name是因为Python解释器对外把__name变量改成了_Student__name，
# 所以，仍然可以通过_Student__name来访问__name变量：


# 但是强烈建议你不要这么干，因为不同版本的Python解释器可能会把__name改成不同的变量名。
# 总的来说就是，Python本身没有任何机制阻止你干坏事，一切全靠自觉。


# 继承 和多态

# 在OOP程序设计中，当我们定义一个class的时候，可以从某个现有的class继承，
# 新的class称为子类（Subclass），而被继承的class称为基类、父类或超类（Base class、Super class）。
# 比如，我们已经编写了一个名为Animal的class，有一个run()方法可以直接打印：
class Animal(object):
    def run(self):
        print "Animal is running"


# 当我们需要编写Dog和Cat类时，就可以直接从Animal类继承：
# 对于Dog来说，Animal就是它的父类，对于Animal来说，Dog就是它的子类。Cat和Dog类似。
# 继承有什么好处？最大的好处是子类获得了父类的全部功能。由于Animial实现了run()方法，因此，Dog和Cat作为它的子类，什么事也没干，就自动拥有了run()方法：

# 当然，也可以对子类增加一些方法，比如Dog类：


# 继承的第二个好处需要我们对代码做一点改进。你看到了，无论是Dog还是Cat，它们run()的时候，显示的都是Animal is running...，
# 符合逻辑的做法是分别显示Dog is running...和Cat is running...，因此，对Dog和Cat类改进如下：

class Dog(Animal):
    def run(self):
        print "Dog is running"

    def eat(self):
        print "eating meat"


class Cat(Animal):
    def run(self):
        print "Cat is running"

    def eat(self):
        print "eating fish"


dog = Dog()
dog.run()
dog.eat()

cat = Cat()
cat.run()
cat.eat()

# 当子类和父类都存在相同的run()方法时，我们说，子类的run()覆盖了父类的run()，在代码运行的时候，总是会调用子类的run()。
# 这样，我们就获得了继承的另一个好处：多态。
# 要理解什么是多态，我们首先要对数据类型再作一点说明。当我们定义一个class的时候，我们实际上就定义了一种数据类型。
# 我们定义的数据类型和Python自带的数据类型，比如str、list、dict没什么两样：

# a = list() # a是list类型
# b = Animal() # b是Animal类型
# c = Dog() # c是Dog类型


# 判断一个变量是否是某个类型可以用isinstance()判断：
# >>> isinstance(a, list)
# True
# >>> isinstance(b, Animal)
# True
# >>> isinstance(c, Dog)
# True

print isinstance(dog, Dog)

# 看来a、b、c确实对应着list、Animal、Dog这3种类型。
# 但是等等，试试：

print isinstance(dog, Animal)


# Dog可以看成Animal，但Animal不可以看成Dog。
# 要理解多态的好处，我们还需要再编写一个函数，这个函数接受一个Animal类型的变量：

def run_twice(animal):
    animal.run()
    animal.run()


# 当我们传入Animal的实例时，run_twice()就打印出：
run_twice(Animal())
# 当我们传入Dog的实例时，run_twice()就打印出：
run_twice(Dog())


# 看上去没啥意思，但是仔细想想，现在，如果我们再定义一个Tortoise类型，也从Animal派生：

class Tortoise(Animal):
    def run(self):
        print "Tortoise is running slowly"


run_twice(Tortoise())
# 你会发现，新增一个Animal的子类，不必对run_twice()做任何修改，实际上，任何依赖Animal作为参数的函数或者方法都可以不加修改地正常运行，原因就在于多态。
# 多态的好处就是，当我们需要传入Dog、Cat、Tortoise……时，我们只需要接收Animal类型就可以了，
# 因为Dog、Cat、Tortoise……都是Animal类型，然后，按照Animal类型进行操作即可。由于Animal类型有run()方法，
# 因此，传入的任意类型，只要是Animal类或者子类，就会自动调用实际类型的run()方法，这就是多态的意思：
# 对于一个变量，我们只需要知道它是Animal类型，无需确切地知道它的子类型，就可以放心地调用run()方法，
# 而具体调用的run()方法是作用在Animal、Dog、Cat还是Tortoise对象上，由运行时该对象的确切类型决定，
# 这就是多态真正的威力：调用方只管调用，不管细节，而当我们新增一种Animal的子类时，只要确保run()方法编写正确，不用管原来的代码是如何调用的。这就是著名的“开闭”原则：

# 对扩展开放：允许新增Animal子类
# 对修改封闭：不需要修改依赖Animal类型的run_twice()等函数。
# 继承还可以一级一级地继承下来，就好比从爷爷到爸爸、再到儿子这样的关系。
# 而任何类，最终都可以追溯到根类object，这些继承关系看上去就像一颗倒着的树。比如如下的继承树：


# 小结
# 继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写；
# 有了继承，才能有多态。在调用类实例方法的时候，尽量把变量视作父类类型，这样，所有子类类型都可以正常被接收；
# 旧的方式定义Python类允许不从object类继承，但这种编程方式已经严重不推荐使用。任何时候，如果没有合适的类可以继承，就继承自object类。


# 获取对象信息


# 当我们拿到一个对象的引用时，如何知道这个对象是什么类型、有哪些方法呢？
# 使用type()
# 首先，我们来判断对象类型，使用type()函数：
# 基本类型都可以用type()判断：
print type("1213ddd")

print type(123)

print type(None)

# 如果一个变量指向函数或者类，也可以用type()判断：
print type(abs)

print type(dog)

# 但是type()函数返回的是什么类型呢？它返回type类型。如果我们要在if语句中判断，就需要比较两个变量的type类型是否相同：
print  type(123) == type(456)
print type(123) == type("456")

# 但是这种写法太麻烦，Python把每种type类型都定义好了常量，放在types模块里，使用之前，需要先导入：
import types

print type(123) == types.IntType

print type("123") == types.StringType

print type([]) == types.ListType

print type(str) == types.TypeType

# 最后注意到有一种类型就叫TypeType，所有类型本身的类型就是TypeType，比如：
print type(int) == type(str) == types.TypeType

# 使用isinstance()
# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。
# 我们回顾上次的例子，如果继承关系是：
# object -> Animal -> Dog -> Husky

# 那么，isinstance()就可以告诉我们，一个对象是否是某种类型。先创建3种类型的对象：

# >>> a = Animal()
# >>> d = Dog()
# >>> h = Husky()

# >>> isinstance(h, Husky)
# True

print isinstance(dog, Animal)
# 没有问题，因为h变量指向的就是Husky对象。
# 再判断：

# >>> isinstance(h, Dog)
# True

# 同理，实际类型是Dog的d也是Animal类型：

# >>> isinstance(d, Dog) and isinstance(d, Animal)
# True
#

# 但是，d不是Husky类型：

# >>> isinstance(d, Husky)
# False

# 能用type()判断的基本类型也可以用isinstance()判断：
# >>> isinstance('a', str)
# True
# >>> isinstance(u'a', unicode)
# True
# >>> isinstance('a', unicode)
# False

# 并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是str或者unicode：
# >>> isinstance('a', (str, unicode))
# True
# >>> isinstance(u'a', (str, unicode))
# True

# 由于str和unicode都是从basestring继承下来的，所以，还可以把上面的代码简化为：
# >>> isinstance(u'a', basestring)
# True


# 使用dir()
# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print dir("ABXC")

# 类似__xxx__的属性和方法在Python中都是有特殊用途的，比如__len__方法返回长度。
# 在Python中，如果你调用len()函数试图获取一个对象的长度，实际上，在len()函数内部，它自动去调用该对象的__len__()方法，所以，下面的代码是等价的：

print len("ABC")

print "ABc".__len__()


# 我们自己写的类，如果也想用len(myObj)的话，就自己写一个__len__()方法：

class MyObject(object):
    def __len__(self):
        return 100


obj = MyObject()
print len(obj)

# 剩下的都是普通属性或方法，比如lower()返回小写的字符串：
print "ABC".lower()


# 仅仅把属性和方法列出来是不够的，配合getattr()、setattr()以及hasattr()，我们可以直接操作一个对象的状态：

class MyObject1(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj1 = MyObject1()

print hasattr(obj1, "x")
print hasattr(obj1, "y")

print setattr(obj1, "y", 9)
print hasattr(obj1, "y")

print getattr(obj1, "y")

print obj1.y



# 如果试图获取不存在的属性，会抛出AttributeError的错误：
# >>> getattr(obj, 'z') # 获取属性'z'
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'MyObject' object has no attribute 'z'


# 可以传入一个default参数，如果属性不存在，就返回默认值：

print getattr(obj1,"z",155)

# 也可以获得对象的方法：
print hasattr(obj1,"power")

print getattr(obj1,"power")

#小结
# 通过内置的一系列函数，我们可以对任意一个Python对象进行剖析，拿到其内部的数据。要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息。如果可以直接写：
# sum = obj.x + obj.y
# 就不要写：
# sum = getattr(obj, 'x') + getattr(obj, 'y')
# 一个正确的用法的例子如下：
# def readImage(fp):
#     if hasattr(fp, 'read'):
#         return readData(fp)
#     return None

# 假设我们希望从文件流fp中读取图像，我们首先要判断该fp对象是否存在read方法，
# 如果存在，则该对象是一个流，如果不存在，则无法读取。hasattr()就派上了用场。
# 请注意，在Python这类动态语言中，有read()方法，不代表该fp对象就是一个文件流，
# 它也可能是网络流，也可能是内存中的一个字节流，但只要read()方法返回的是有效的图像数据，就不影响读取图像的功能。



