'1.函数参数'''

# 1.1 多个参数
# def testSum(a,b):
#     s = a + b
#     print(s)
# testSum(2,3)
# testSum(a= 3, b= 5)  #关键字参数


# 1.2 不定长参数

# 方式一  形参的前面 加一个 *  表示元祖
# def testASum(*t):
#     s = 0
#     for x in t:
#         s =  s + x
#     print(s)
# testASum(1,2,3,4,5,6,7)


# 方式二 形参的前面 加两个 **  表示字典  必须是关键字1 = 参数1，关键字2 = 参数2
# def testBSum(**kwargs):
#     print(kwargs,type(kwargs))
# testBSum(name = "zb", age = 26)


# 参数的装包 和 解包

# def testSum(a,b,c):
#     print(a+b+c)
#
# def test(*args):  #调用这个函数表示装包
#     print(args)
#     #拆包
#     print(*args)
#     testSum(*args)
# test(1,2,3)


# def testSum2(a,b):
#     print(a)
#     print(b)
#
# def test(**kwargs):
#     print(kwargs)
#     #拆包，不能打印，但是能使用
#     testSum2(**kwargs)
#
#
# test(a = 1,b = 2)

# 1.3 缺省参数 默认参数
# def hit(someBody = '李四'):
#     print(someBody)
#
# hit()


#1.4 函数参数传递默认都是地址传递  如果参数是可变类型，那么就是地址传递，会改变原来的值，如果参数是不可变类型  那么改变值，那就
# 会开辟一个新的内存空间，就是一个值传递

# 不可变类型
# def chang(num):
#     num = 666
#     print(id(num))
#     print(num)
#
# b = 10
# print(id((b)))
# chang(b)
# print(b)

# 可变类型
# def chang(num):
#     num.append(6)
#     print(id(num))
#     print(num)
#
# b = [1,2,3,4]
# print(id((b)))
# chang(b)
# print(b)


'''2.函数的返回值'''
# def computeSum(a,b =1):
#     """
#     函数文档描述
#     :param a: 数值1 基本类型 不可选 没有默认值
#     :param b: 数值1 基本类型 可选 默认值 = 1
#     :return:  返回计算结果  返回类型 元祖  example:(1,2)
#     """
#     result = a + b
#     cha = a - b
#     return  (result,cha)
# x,y = computeSum(1,2)
# print(x,y)
# help(computeSum)


'''3.偏函数'''

#方式一
# def test(a,b,c,d):
#     print(a+b+c+d)
#
# def test2(a,b,c=10,d=10):   # 这个函数就是偏函数
#     test(a,b,c,d)
# test2(1,1)

# 方式二 推荐  functools.partial(函数，特定参数 = 偏爱值)
# import  functools
# def test(a,b,c,d=10):
#     print(a+b+c+d)
#
# newtest = functools.partial(test,c=5)
# newtest(1,2)
# print(type(newtest))


# 使用场景
# numstr = "10010"
# result = int(numstr,base=2)
#
# import  functools
# int2 = functools.partial(int,base = 2)
# int10 = functools.partial(int,base = 10)
# print(result,int2(numstr),int10(numstr))


'''4.高阶函数'''
#定义：当一个函数A里面的参数是另一个函数时候，这个函数就是一个高阶函数

# l = [{"name":"lzb01","age":20},{"name":"lzb04","age":18},{"name":"lzb03","age":19},{"name":"lzb02","age":21}]
#
# def getKey(xdict):
#     return xdict["name"]
#
# result = sorted(l,key=getKey)
# print(result)


# 4.1 函数调用
# def caculater(num1,num2,caculaterFunc):
#     print(caculaterFunc(num1,num2))
#
# def jiafa(a,b):
#     return a + b
# def jianfa(a,b):
#     return a - b
# caculater(8,5,jiafa)
# caculater(8,5,jianfa)


# 4.2 返回函数
# def getFlagFunc(flag):
#     def sum(a,b,c):
#         return a + b + c
#     def sub(a,b,c):
#         return a - b - c
#     def nil(a,b,c):
#         return "参数不对"
#     if flag == "+":
#         return  sum
#     elif flag == "-":
#         return sub
#     else:
#         return nil
#
# resultFunc = getFlagFunc("]")
# print(resultFunc)
# res = resultFunc(10,2,3)
# print(res)

# 4.3 匿名函数lambda 参数1，参数：表达式就是返回值
# result = (lambda  x,y: x+y)(1,2)
# print(result)

# func = lambda x,y:x *y
# print(func(1,3))


# # 排序
# l = [{"name":"lzb01","age":20},{"name":"lzb04","age":18},{"name":"lzb03","age":19},{"name":"lzb02","age":21}]
# result = sorted(l,key=lambda xdict:xdict["name"])
# print(result)


'''5.闭包条件：A、内存函数引用外层函数的变量（包括参数）B、外层函数把内层函数当做返回值返回 C、函数嵌套'''

# 闭包的格式
# def testA(a):
#     b = 10
#     def testB():
#         print(a)
#         print(b)
#     return testB
#
# newfunc = testA(10)
# newfunc()

# 注意1 闭包内修改变量需要增加nonlocal 如果没有增加就是新增一个新的变量
# def line_config(content,length):
#     num = 10
#     def line():
#         print('-' * (length // 2) + content + '-' * (length // 2))
#         nonlocal num
#         num = 666
#         print(num)
#
#     print(num)
#     line()
#     print(num)
#     return line
#
# line1 = line_config('闭包',40)
# line1()


# 注意2：函数是被执行才会确定参数的值

# def test():
#     funcs = []
#     for i in range(1,4):
#         def test2():
#             print(i)
#         funcs.append(test2)
#     return funcs
#
# newfuncs = test()
# newfuncs[0]()
# newfuncs[1]()
# newfuncs[2]()

# def test():
#     funcs = []
#     for i in range(1,4):
#         def test2(num):
#             def inner():
#                 print(num)
#             return inner
#         funcs.append(test2(i))
#     return funcs
#
# newfuncs = test()
# newfuncs[0]()
# newfuncs[1]()
# newfuncs[2]()









