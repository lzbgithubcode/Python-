'1. 装饰器：给一个函数增加额外的功能'''

# 功能函数
# def ftp():
#     print("发图片")
# def fwz():
#     print("发文字")
# # 业务逻辑
# buttonIndex = 1
# if buttonIndex == 0:
#     ftp()
# else:
#     fwz()

#条件：在发送东西之前增加登录验证


#1.1 第一种方式 增加函数闭包
# # 功能函数
# def checkIsLogin(func):  # 闭包的使用
#     def inner():
#         print("登录验证......")
#         func()
#     return inner
#
# def ftp():
#     print("发图片")
#
# ftp = checkIsLogin(ftp)
#
# def fwz():
#     print("发文字")
#
# fwz = checkIsLogin(fwz)
# buttonIndex = 1
# if buttonIndex == 0:
#     ftp()
# else:
#     fwz()


'''2. 装饰器 语法糖'''

# # 功能函数
# def checkIsLogin(func):  # 闭包的使用
#     def inner():
#         print("登录验证......")
#         func()
#     return inner
#
# @checkIsLogin
# def ftp():
#     print("发图片")
#
# # ftp = checkIsLogin(ftp)
#
# @checkIsLogin
# def fwz():
#     print("发文字")
#
# # fwz = checkIsLogin(fwz)
#
# buttonIndex = 1
# if buttonIndex == 0:
#     ftp()
# else:
#     fwz()

'''3.装饰器的执行时间'''
#实现功能  为发说说函数增加额外的功能
# 1.以前的调用方式不变
# 2、增加额外的功能


# def check(func):
#     print("111111")
#     def inner():
#         print("发说说之前的额外功能实现")
#         func()
#     return inner
#
# @check      #写出装饰器语法糖的时候就已经执行check函数
# def fss():
#     print("发说说")
#
# fss()


'''4.装饰器的叠加'''
# 从函数的头部开始 向上装饰    执行 从代码的行数  从上到下

# def print_line(func):
#     print("------print_line-----")
#     def inner():
#         print("-----------")
#         func()
#         print("-----------")
#     return inner
#
#
# def print_star(func):
#     print("*****print_star******")
#     def inner():
#         print("***********")
#         func()
#         print("***********")
#     return inner
#
# @print_line  #print_content =  print_line（print_content）
# @print_star  # print_content =  print_star（print_content）
# def print_content():
#     print("刘子彬笔记")
#
#
# #*****print_star******
# # ------print_line-----
# # -----------
# # ***********
# # 刘子彬笔记
# # ***********
# # -----------
#
# print_content()

'''4.装饰器装饰有参数的函数'''

# #装饰器 装饰之后pnum 是指向inner 函数的地址  当执行inner函数的时候，传参数就是innner接受参数 执行func 就是执行pnum函数
#
# def zsq(func):
#     def inner(*args,**kwargs):
#         print("*" * 30)
#         func(*args,**kwargs)
#     return inner
#
# @zsq
# def pnum(num):
#     print('打印参数---',num)
#
# @zsq
# def pnum2(num1,num2,num3):
#     print('打印参数---',num1,num2,num3)
#
# pnum2(1122,33,num3=4)

'''5.装饰器自身有参数'''

def getzsq(c):
    def zsq(func):
        def innner(*args, **kwargs):
            print("装饰器")
            print(c * 30)
            res = func(*args, **kwargs)
            return res

        return innner
    return zsq


def zsq(func):
    def innner(*args,**kwargs):
        print("装饰器")
        print("+" * 30)
        res = func(*args,**kwargs)
        return res
    return innner




# @zsq # pnum = zsq(pnum)
# def pnum(num):
#     print(num)


@getzsq("===")  #主要保证回来的是一个装饰器就可以
def pnum(num):
    print(num)

pnum(3)








'''6.装饰器的返回值'''
#
# def computeSum(func):
#     def inner(*args,**kwargs):
#         print("检测参数")
#         print(args,kwargs)
#         res = func(*args,**kwargs)
#         return res
#     return inner
#
# @computeSum
# def pnum(num1,num2,num3):
#     return num1 + num2 + num3
#
# @computeSum
# def pnum2(num):
#     print("没有返回值",num)
#
#
# resut = pnum(1,2,num3=3)
# print(resut)
# pnum2(2)
