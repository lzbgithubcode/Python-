#格式符输出
# name = 'zb'
# age = 18
# #我的名字是xxx,今年的年龄是xxx
# print('我的名字是%s,今年的年龄是%d'%(name,age))

#%[(name)][flags][width][.precision]typecode
#[]表示可以省略

#（name）表示根据key找到对应的值，格式化到字符串中
# mathScore = 20
# english = 40
# print("英语的分数%(es)d,数学的分数%(ms)d" % ({'es':english,'ms':mathScore}))

#width 占用的宽度  flags 对齐方式，默认是右边对齐(如果是- 是左对齐 0 表示填充0)
# print('%-10d' % mathScore)

# min = 5
# sec = 8
# # 05：08
# print('%02d:%02d' % (min,sec))

#precision小数点的精度