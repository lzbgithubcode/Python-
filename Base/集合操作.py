'1.集合与其他的对比'''
# str1 = "abc"
# l = [1,2,3,4,5]
# t = (1,2,3)
# d = {'name':'zb','age':18}
#
# jihe = {1,2,3,4} #无序、不可随机访问、不可重复的集合 和数学里面应用差不多set 可变集合  frozenSet 不可变集合

'2.可变集合的定义方式'''
# s = {1,2,3}
#
# s = set() #set(可变类型)
#
# s = set(x * 2 for x in range(10) if x% 2 == 0)  #集合的类型推导

'3.不可变集合的定义'''
# fs = frozenset()  #frozenset(可变类型)
# print(frozenset([1,2,3]))
#
# fs = frozenset(x ** 2 for x in range(10) if x% 2 == 0) #集合的类型推导
# print(fs,type(fs))

# 注意：集合中的元素为不可变 - 可哈希值 可以用集合对列表去重

'''4.集合的操作'''
# 单一集合
#s = {1,2,3,4,5,6,7}

# 增加
# s.add('a')
# print(s,type(s))

# 删除
# result = s.remove(3)
# print(s,result,type(s))

# result = s.clear()
# print(s,result)

# result = s.pop()  #随机删除
# print(s, result)


# result = s.discard(10)  #随机元素 如果没有不报错
# print(s, result)

# 改  不能修改


# 查 不能通过key 索引查询 但是可以遍历

# for x in s:
#     print(x)

#s = frozenset([1,2,3,4])
# i = iter(s)
# for x in i:
#     print(x)


'''5.多集合操作'''

# 集合的交集 intersection &  intersection_update
#s1 = {1,2,3,4,5,6}
# s1 = frozenset([1,2,3,4,5])
# s2 = {4,5,6}
# result = s1.intersection(s2)  # s1 和s2 谁在前面 返回的类型 以左边为准
# print(result,type(result))

# result = s1 & s2
# print(result,type(result))

# result = s2.intersection_update(s1)
# print(result,type(result),s2)

# s1 = {'1','2','3','4','5'}
# print(s1.intersection(['1','2']))


# 集合的并集 union |   update
# s1 = frozenset([1,2,3,4,5])
# s2 = {4,5,6}
# result = s2.union(s1)
# print(result,type(result))




#集合的差集 difference -  update

# s1 = {1,2,3,4,5}
# s2 = {4,5,6}
# result = s2.difference(s1)
# print(result,type(result))

# 集合的判定
s1 = {1,2,3,4,5,6}
s2 = {4,5,6}

# 集合是否相交
# print(s1.isdisjoint(s2))

# 集合是否包含
print(s1.issuperset(s2))

# 集合是否包含
print(s2.issubset(s1))





