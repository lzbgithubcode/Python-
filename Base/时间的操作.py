'时间日历的处理'''
# 三个模块
# time模块
# calendar 模块
# datetime 模块

'''1.time模块'''
import  time

# # 1.1 获取时间戳
# result =time.time()
# years = result/(24 * 60 * 60 * 365) + 1970
# print(result,years)

# 1.2 获取时间元祖
# result = time.localtime()
# print(result)

# 1.3 获取格式时间日期
# 秒 ----》可读时间
# t = time.time()
# result = time.ctime(t)
# print(result)


# 时间元祖---》可读时间
# tt = time.localtime()
# resutl = time.asctime(tt)
# print(resutl)


#1.4 格式化日期 < --- > 时间戳

# 时间元祖 ----> 格式化日期time.strftime(时间格式，时间元祖)
# result = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
# print(result)

# # 格式化日期 --> 时间元祖 time.strptime(日期格式字符串,日期格式)
# pt =  time.strptime("2017-11-21 22:20:39","%Y-%m-%d %H:%M:%S")
# resutl = time.mktime(pt)
# print(pt,'\n',resutl)

#1.5 获取CPU当前时间，统计代码执行时间time.clock()
# startTime = time.clock()
# for x in range(1,100000):
#     print(x)
# endTime = time.clock()
# print(endTime - startTime)

# 1.6 休眠n秒

# while True:
#     print(time.time())
#     time.sleep(1)

'''2.calendar 模块'''
# import  calendar
#
# #获取某月的日历信息
# print(calendar.month(2017,6))

'''3.datetime 模块，标准库'''

import  datetime

# 3.1 获取当前的日期
# print(datetime.datetime.now())
# print(datetime.datetime.today())
# t = datetime.datetime.now()
# print(t.year,t.month,t.day)


# 3.2 计算的N天之后的日期
# curretDate = datetime.datetime.today()
# result = curretDate + datetime.timedelta(days=7)
# print(curretDate,result)

# 3.3计算两个日期时间差
firstDate = datetime.datetime(2017,11,23,12,00,00)
secondDate = datetime.datetime(2017,11,22,12,00,00)
dela = firstDate - secondDate
print(dela,type(dela))
print(dela.total_seconds())









