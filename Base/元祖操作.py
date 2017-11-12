'1.元祖定义：有序不可变集合'''

# 1.1 元祖的定义
# l = (1,)
# print(type(l))

# tup = 1,2,3,4,'zb'
# print(tup)

# 1.2 列表转化从元祖
# nums = [1,2,3,4,5,6]
# result = tuple(nums)
# print(result,type(result))

'''2.元祖的操作，不可变，没有增删改'''

# 2.1 查询某个元素或者多个元素

items = (1,2,34,4,5,5,6,7,8,9)
print(items)
# print(items[2],items[:2:],items[::-1])

# 2.2 获取元祖值
# print(items.count(5))  # 元素的个数
# print(items.index(2))  # 元素对应的索引
# print(len(items),max(items),min(items))


# 2.3 判定 in not in
# print(1 in items)


# 2.4 拼接(乘法  家法)和拆包
#
# item2 = ('a','b','c')
# print(items + item2)
# print(item2 * 2)

# a,b = (10,20)
# a,b = (b,a)
# print(a,b)





