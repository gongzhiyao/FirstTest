#!/usr/bin/env python
#coding=utf-8


# 面向对象编程

# 面向对象编程——Object Oriented Programming，简称OOP，是一种程序设计思想。OOP把对象作为程序的基本单元，一个对象包含了数据和操作数据的函数。
# 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
# 而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。
# 在Python中，所有数据类型都可以视为对象，当然也可以自定义对象。自定义的对象数据类型就是面向对象中的类（Class）的概念。
# 我们以一个例子来说明面向过程和面向对象在程序流程上的不同之处。
# 假设我们要处理学生的成绩表，为了表示一个学生的成绩，面向过程的程序可以用一个dict表示：


student1 = {"name":"Michael","score":98}
student2 = {"name":"Bob","score":81}


# 而处理学生成绩可以通过函数实现，比如打印学生的成绩：
def print_score(student):
    print "%s:%s" %(student["name"],student["score"])

print_score(student1)


# 如果采用面向对象的程序设计思想，我们首选思考的不是程序的执行流程，而是Student这种数据类型应该被视为一个对象，这个对象拥有name和score这两个属性（Property）。
# 如果要打印一个学生的成绩，首先必须创建出这个学生对应的对象，然后，给对象发一个print_score消息，让对象自己把自己的数据打印出来。

class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def print_score(self):
        print '%s:%s'%(self.name,self.score)


#给对象发消息实际上就是调用对象对应的关联函数，我们称之为对象的方法（Method）。面向对象的程序写出来就像这样：

bart = Student("Bart Simpon",59)
lisa = Student("Lisa Simpon",87)

bart.print_score()
lisa.print_score()


# 面向对象的设计思想是从自然界中来的，因为在自然界中，类（Class）和实例（Instance）的概念是很自然的。
# Class是一种抽象概念，比如我们定义的Class——Student，是指学生这个概念，而实例（Instance）则是一个个具体的Student，比如，Bart Simpson和Lisa Simpson是两个具体的Student：
# 所以，面向对象的设计思想是抽象出Class，根据Class创建Instance。
# 面向对象的抽象程度又比函数要高，因为一个Class既包含数据，又包含操作数据的方法。

# 小结
# 数据封装、继承和多态是面向对象的三大特点，我们后面会详细讲解。



if __name__ == '__main__' :
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
bar.name ="Bart Simpson"

print bar.name

# 由于类可以起到模板的作用,因此，可以在创建实例的时候，把一些我们认为必须绑定的属性强制填写进去。
# 通过定义一个特殊的__init__方法，在创建实例的时候，就把name，score等属性绑上去：

class Student_new (object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
# 注意到__init__方法的第一个参数永远是self，表示创建的实例本身，因此，在__init__方法内部，就可以把各种属性绑定到self，因为self就指向创建的实例本身。
bob = Student_new("Bob",99)
print  "name:%s,score:%s"%(bob.name,bob.score)
def print_score_new(student):
    print "name:%s,score:%s"%(student.name,student.score)


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
    def __init__(self,name,score):
        self.name =name
        self.score = score


    def get_score(self):
        return self.score

    def get_name(self):
        return self.name

    def get_grade(self):
        if self.score>=90:
            return "A"
        elif self.score >=60:
            return "B"
        else:
            return "C"

    def get_student_info(self):
        return "name:%s,score:%s"%(self.name,self.score)

# 要定义一个方法，除了第一个参数是self外，其他和普通函数一样。要调用一个方法，只需要在实例变量上直接调用，除了self不用传递，其他参数正常传入：

Lisa = New_Student("Lisa",98)

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
    def __init__(self,name,score):
        self.__name = name
        self.__score= score


    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score


    def set_score(self,score):
        if 0<=score <=100:
            self.__score= score
        else:
            raise ValueError("bad score")

    def set_name(self,name):
        if name == None or name=="":
            raise TypeError("bad param")
        else:
            self.__name = name

    def get_student_info(self):
        return "name:%s,score:%s"%(self.__name,self.__score)

white = Student_Private("Write simpon",89)

print white.get_student_info()

# 改完后，对于外部代码来说，没什么变动，但是已经无法从外部访问实例变量.__name和实例变量.__score了：

# 这样就确保了外部代码不能随意修改对象内部的状态，这样通过访问限制的保护，代码更加健壮。
# 但是如果外部代码要获取name和score怎么办？可以给Student类增加get_name和get_score这样的方法：

# 如果又要允许外部代码修改score怎么办？可以给Student类增加set_score方法：


#你也许会问，原先那种直接通过bart.score = 59也可以修改啊，为什么要定义一个方法大费周折？因为在方法中，可以对参数做检查，避免传入无效的参数


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
        





























































