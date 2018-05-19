def power(x, n =2):  #默认参数为2，可以不写
    s = 1
    while n>0:
        n = n -1
        s = s*x
    return  s

print(power(3))
print(power(3,3))

def calc(*numbers):   #  可变参数，可以输入任意多的参数，实际上传进去一个tuple
    sum = 0
    for n in numbers:
        sum = sum + n
    return sum
print(calc(1,2,3,4))
print(calc(*[1,2,3,4]))   #需要传入tuple或者list时前面加*号

def person(name,age,**kw):   #定义关键字参数
    print("name:",name,"age:",age,"other:",kw)

person("Kanghui",18)
person("Kanghui",20,city = "Xian",job = "stu")


###在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
#对于任意函数# ，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

#作业
