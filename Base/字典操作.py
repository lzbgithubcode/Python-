'1.字典的定义,key不能重复，key 是任意不可变类型，hash 方式实现'''

#方式一
# person = {'name':'zb','age':18}
# print(person)
# print(person['name'])


#方式二 fromkeys
# d = dict.fromkeys('abc','1')
# print(d)


# num = 10
# print(id(num))   打印地址
# num = 12
# print(id(num))

# 字典的底层原理   key 通过哈希函数转化为数字，哈希值 --》 通过数字对数组取余，得到数字的索引---》通过索引找到对应的value


'''2.增、删、改、查、计算、判定'''
#2.1 增加
# d = dict.fromkeys("abc",'666')
# print(d)
# d["ddd"] = 8888
# print(d)

#2.2删除
# d = {"d":666,"a":666,"b":666,"c":666,}
# print(d)
#
# # del d['a']
# # print(d)
#
# # result = d.pop('b')
# # print(d)
#
# # 删除按升序排序后的第一个键值对,返回元祖
# result = d.popitem()
# print(result,d)
#
# # 删除所有的键值对
# d.clear()
# print(d)

# 2.3 修改值
# d = dict.fromkeys("abc",7777)
# print(d)
# d.update({'a':6,'b':6,'uuuu':0000})  #批量修改
# print(d)


# 2.4查询
# 2.4.1 查询单个值
# d = {'a':6,'b':5656,'uuuu':0000}
# # print(d['a'])
#
# # result  = d.get('aa',888) #取值不报错,如果娶不到就直接赋值8888
# # print(result)
#
# result  = d.setdefault('aa',888)  #取值不报错,如果娶不到就直接赋值8888,但是会改变原来的字典
# print(result,d)

# 2.4.2 查询所有的值
# d = {'name':'lzb','age':16,'address':'重庆'}
# kvs = d.items()
# for key,value in kvs:
#     print(key,value)



#2.5 字典的计算和判断
# d = {'name':'lzb','age':16,'address':'重庆'}
# print(len(d))
#
#
# print('name' in d)
# print(d)

