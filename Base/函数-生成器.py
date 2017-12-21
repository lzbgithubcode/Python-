'1.生成器：一个特殊的迭代器generator'''
'''
迭代器特性：1.惰性计算数据，节省内存
          2.能记录状态，并通过next()函数执行下一个状态
          3.具有可迭代性 
'''

'''2.生成器创建'''
# 2.1 创建方式1 把列表推导式的 []  改为（）
# l = [i for  i in range(0,10000) if i %2 == 0]
# print(l)

# l = (i for  i in range(0,10000) if i %2 == 0)
# print(next(l))
# print(next(l))
# print(l.__next__()) # l.__next__(） =  next(l)

# 2.2创建方式1 生成器函数 包括yield 返回是一个生成器  yield阻断 函数执行，当调用者执行next 或者 __next__的时候 从上一个yield之后
#开始执行 ，执行到下一个yield 阻断 ,注意 next 最后一个可能crash

# def test():
#     print('xxxx')
#     yield 1
#     print(11)
#
#     yield 2
#     print(22)
#
#     yield 3
#     print(33)
#
#     yield 4
#     print(44)
#
# g = test()
# print(g)
#
# print(g.__next__())
# print(next(g))

'''3.生成器的访问'''

# def test():
#     for i in range(1, 100):
#         print('''xxxxx''')
#         yield i
#
# g = test()
# print(g)
# print(g.__next__())
# print(g.__next__())

'''4.生成器的send()方式'''
#send() 方法有一个参数，指定的是上一次被挂起的yield 的返回值
# 与__next__()相比，可以给yield 传值send(None) ==  __next__()
# def test():
#     res1 = yield 1
#     print(res1)
#
#     res2 = yield 2
#     print(res2)
#
# g = test()
# print(g.__next__())  #send(None) = __next__()
# print(g.send('0000'))


'''5.生成器的注意点'''
# 1.当生成器里面有 return  只要有return  会抛出异常
# 2.当生成器只能被迭代一次  如果要多次 就重新创建生成器

def test():
    yield  1
    print('a')

    yield  2
    print('b')

    yield 3
    print('c')

# g = test()
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

g1 = test()
for i in g1:
    print(i)

print('======')
g1 = test()
for i in g1:
    print(i)

'''6.递归函数 函数A里面调用函数A  传递和回归'''

# 求9的阶层  9 * 8 * 7 * ....1

# 先分解 ，如果知道结果就直接返回
def jiecheng(n):
    if n == 1:
        return 1
    # n ！= 1
    return n * jiecheng(n- 1)


result = jiecheng(4)
print(result)