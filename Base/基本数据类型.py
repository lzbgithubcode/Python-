'1.数值-数学函数（内建函数 + 模块函数比如math）'''
#算数运算符
#复合运算符
#逻辑运算符 not and  or

'''1.1使用内建函数'''
# # 绝对值
# print(abs(-10))


# # 最小值
# print(min(1,-2,3,4))
# print(max([1,23,3,4,5]))


# #最大值
# print(max(1.2,-5,6,7,2,3))


# # 四舍五入
# print(round(3.14,3))

# #x 的 y次幂
# print(pow(2,4))

'''1.2非内建函数-模块函数需要导入模块'''

# 导入模块   使用方式 模块.函数名称（参数）

# 数学函数  math模块
# import math

#  ceil()  上取整数
# p1 = 3.5
# print(math.ceil(p1))

#  floor()  下取整数
# p1 = 3.5
# print(math.floor(p1))

# sqrt() 开平方
# print(math.sqrt(9))

# log(x,base) 以base为基数，x的对数
# print(math.log(1000,10))


# 随机函数  random模块
#import random

# random()  [0,1) 0到1的随机小数
# print(random.random())

# choice() 从序列中任意选择一个数值
# print(random.choice([1,2,4,6,3]))

# uniform(x,y) 取出[x,y]的随机小数
# print(random.uniform(2,4))


# randint(x,y) x到y 随机整数
# print(random.randint(2,6))

# randrange(self, start, stop=None, step=1, _int=int)  给定一个区间的随机整数 [start stop)
#print(random.randrange(1,5))


# 三角函数  math模块
import math

# sin(x) 正玄 x  x应该是弧度值  = 角度/180 *pi  === radians()
print(math.sin(math.radians(30)))







'''2.字符串 -- 成对出现 引号就近原则匹配'''
# name = "我是'zibin'"
# print(name)

# name = ("我是'zibin' "
#        "子彬")
# print(name)

'''2.1字符串的拼接'''
# # 方式一  str1 + str2
# result = "子彬" + "燕子"
# print(result)

# # 方式二  str1  str2  在一行就可以
# result = "子彬"  "燕子"
# print(result)

# # 方式三  占位符拼接
# result = "我是 %s,%d" % ("燕子",12)
# print(result)


# 方式四  字符串乘集
# result = "zibin\n"
# print(result *3)

'''2.2字符串的切片 - 获取字符串的某段字符'''

# 获取某一个字符   name[下标]
# name = "abcdefg"
# print(name[2])
# print(name[-1])


# 获取字符串多个字符  name[起始：结束：步长]   或者 name[起始：结束） 默认值起始=0 结束=len(str) 步长=1
# name = "abcdefghijk"
# print(name[0:3])
# print(name[::])
# print(name[:len(name):])
# print(name[3:1:-1])
# print(name[-1:-2:-1])
# print(name[::-1])  #翻转字符串










