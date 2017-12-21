'作用域'''
'''
命名空间

LEGB
L - Local 函数内的命名空间，作用范围整个函数
E - Enclosing function local 外部嵌套函数的命名空间  作用范围：闭包
G - Global 全局命名空间  作用于单前文件
B - Builtin 内建模块命名空间 作用范围：所有模块

内部查找顺序：L -> E - > G - > B 

注意：没有块级作用域

'''

'''1.局部变量'''

# def test():
#     a = 1
#     b = 2
#     def test2():
#        # nonlocal  a   #函数内可以操作a,改变a的值，只是适用于闭包里面
#         a = 10  # 新定义的a 值，不是修改原来的a
#         print(a)
#
#     test2()
#     print(a)
# test()

'''2.全局变量'''
a = 999

def test():
    a = 10   #定义一个新的a，不是外面的a, 如果要使用外面的a,需要申明global
    b = 11
    def test2():
       # nonlocal  a  使用闭包里面的a = 10,修改他的值
        a = 100   #定义一个新的a
        print(a)
    test2()
    print(a)
    print(locals()) #打印局部变量

print(a)
test()
print(a)
print(globals()) #获取全局变量