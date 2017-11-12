'1.列表基本概念：有序可变的元素集合'''
'1.1列表的定义'''
# 方式一
# list = [1,2,4,6]
# list2 =[]
# list3 =['z',2,7,"23"]
# print(type(list))

# 方式二  列表生成式 range(start,stop,step) 开始 结束 步长
# list = range(1,100,2)  # 不是立即生成列表，只有使用的时候才会生成
# for x in list:
#     print(x)


# 方式三  列表推导式  多个->推导出多个   多个推导出->部分 [表达式 for in ]
# nums = [1,2,3,4,5]
# result = [x * x  for x in nums]
# print(result)
#
# result2 = [x * x for x in nums if x % 2==1]
# print(result2)
#
# result3 = [x2 * x2 for x in nums for x2 in nums]
# print(result3)


'2.列表的操作'''
nums = [1,2,3,4]
print(nums)
'2.1增'''
# append  增加在最后 ,修改原来的列表
# nums.append(5)
# print(nums)

#insert(self, index, p_object)  插入到index之后
# nums.insert(2,5)
# print(nums)

# extend() 追加后面的可迭代序列  iterable  字符串 列表 元祖
# nums.extend([6,7,8])
# print(nums)

# 乘法  加法 运算
# print(nums *3)
# print(nums + [6,7,8])


'2.2删'''

# del 语句  删除整个列表 或者某个元素
# del nums[2]
# print(nums)
#
# del  nums
# print(nums)


# pop  删除列表的元素 默认是最后一个  返回被删除的数据
# result = nums.pop()
# print(nums,result)

# remove（object） object  删除某个元素
# num = [1,2,3,4,4,2,2,3,4,2]
# print(num)
# for x  in num:
#     if 2 in num:
#         num.remove(2)
# print(num)

'2.3改'''
# nums[1] = 222
# print(nums)


'2.4查'''

# # 获取当个元素
# print(nums[2])
#
# # 获取元素的索引
# print(nums.index(3))
#
#
# #多个元素切片 item[start:end:step]
# print(nums[1:3])


# 根据元素遍历 for item in items
items = ["a","a","d","a","c"]
print(items)
# currentIndex = 0
# for x in items:
#     print(items.index(x,currentIndex))
#     currentIndex += 1


# 根据索引遍历

# # 1.创建一个索引列表
# count = len(items)
# indexs = range(count)
#
# # 2.遍历索引列表
# for index in indexs:
#     print(index,items[index])

# 根据列表创建枚举对象（enumerate）, 枚举对象直接被遍历

# result = list(enumerate(items))
# print(result)
# for idx,value  in enumerate(items):
#     print(idx,value)


# 迭代的概念
'''
迭代：按照一定的顺序访问集合中的每一个元素，或者叫遍历

可迭代对象：能被迭代的对象 for in

判断可迭代对象: isinstance(判断对象，collections.Iterable)

迭代器：能否作用于next()  isinstance(判断对象，collections.Itertor)，适合大型的集合，不能多次迭代

'''

# 使用迭代器遍历,
# itemiter = iter(items)
# for value in itemiter:
#     print(value)



'2.4其他'''

# 2.4.1判断列表 in not in
# print("a" in items)

# 2.4.2 比较列表  == >   <

# 2.4.3 排序 sort(self, key=None, reverse=False) key = 排序关键字  reverse = yes 默认是升序

# print(sorted(items,reverse= True))

# infos = [("zb",18),("xi",32),("fb",12),("zd",18),("zx",21),("zc",23)]
# print(infos)
#
# # 方式1 内建函数
# def getkey(x):
#     return  x[1]
#
# result = sorted(infos,key=getkey,reverse=True)
# print('方式一排序 - %s' % result)
#
#
# resut = infos.sort(key=getkey,reverse=True)
# print('方式二排序 - %s -- %s' % (resut,infos))


# 乱序 和翻转
l = [1,2,3,4,5,6,7,8]
# import random
# result = random.shuffle(l)
# print(result,l)

print(l.reverse(),l)
print(l[::-1])
