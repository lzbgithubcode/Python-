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
# import math
#
# # sin(x) 正玄 x  x应该是弧度值  = 角度/180 *pi  === radians()
# print(math.sin(math.radians(30)))



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


'''2.3字符函数操作'''
# 2.3.1 查找计算
# name = "我是liuzibin\n"
# print(len(name))

# find(self, sub, start=None, end=None) 查找子串的下标位置
# 默认是 start = 0 end= len(str) 没有找到是-1  从左到右
# name = "我是liuzibin"
# num = name.find("i",4)
# print(num)

# rfind(self, sub, start=None, end=None)  从右到左 和find一样
# num = name.rfind("i")
# print(num)

#  index(self, sub, start=None, end=None)   从左到右 和find 一样 只是找不到会报错
# num = name.index("i",4)
# print(num)

#  rindex(self, sub, start=None, end=None)   从左到右 rfind 一样 只是找不到会报错

# count 计算子字符串出现的个数
# count = name.count("i")
# print(count)

# 2.3.2 转换

name = "wo shi ziBin shi wo "

# replace  replace(self, old, new, count=None) 替换字符串
print(name.replace('s','b',1))


# capitalize 把字符串首字符转化为大写
print(name.capitalize())

#  title  把字符串里面的子串转化为大写
print(name.title())

#  lower  把字符串全部转化为小写
print(name.lower())

#  upper  把字符串全部转化为大写
print(name.upper())

print(name)

# 2.3.3 填充压缩
# name = "lililiuzibinnnnn"
# ljust(self, width, fillchar=None) 指定字符串靠左填充字符串的长度
#    参数  width   结果字符串的长度
#         fillchar 填充字符串的字符串
# print(name.ljust(20,'1'))

#  center(self, width, fillchar=None) 填充字符串在中间
# print(name.center(20,'1'))

# lstrip(self, chars=None) 从左侧开始移除原来指定的字符串（默认是空白字符）
#print(name.lstrip("li"))
#print(name)


#  rstrip(self, chars=None)  从右侧开始移除原来指定的字符串（默认是空白字符）
# print(name.rstrip('n'))
# print(name)


# 2.3.4 分割拼接
# name = "liuzibin-sex-age-score-0830-1234567"
# split(self, sep=None, maxsplit=-1) 字符串的分割 sep分割符号  maxsplit最大的分割次数
# print(name.split('-'))
# print(name.split('-',4))


# partition(self, sep)  分割返回元祖 包括 左侧 + sep + 右侧内容  如果没有没有找到（"原字符串"，""，""）
# print(name.partition('-'))
# print(name.rpartition('-'))
# print(name)


# splitlines(self, keepends=None) 多行分割  根据的\n \r等分割符分割
# name = "wo \n shi  \r zibin"
# print(name.splitlines(False))
# print(name)


# join(self, iterable) 将给的的可迭代对象进行拼接 和 split反的
# name = "xxx"
# print(name.join('liuzibin'))


# 2.3.5 判定
#name = "liuzibin123.mp3"

# isalpha  字符串中是否全是字母
#print(name.isalpha())

# isdigit  字符串中是否全是数字
#print(name.isdigit())

# isalnum  字符串中是否全是数字或者字母
#print(name.isalnum())

# isspace  字符串中是否全是空白符号 空格 换行之类
#print(name.isspace())

# startswith(self, prefix, start=None, end=None) 判断字符是否什么前缀开头
#print(name.startswith("zi",3,8))

# endswith(self, prefix, start=None, end=None) 判断字符是否什么结尾开头
#print(name.endswith(".mp3"))


# in 字符串是否被包含
# print("zi" in "woshizibin")

















