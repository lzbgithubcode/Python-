'文件：数据存放容器，是操作的一个单位'''
'''
文件内容: 1.文本文件  doc  text xls
         2.二进制文件  视频  、音频  、图片
文件操作流程 ： 打开 -> 操作编辑 --->关闭
              文件句柄类型（只读、只写、读写） 管道  
              open('文件'，'模式')
              
'''

'''1.打开文件'''

#open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True
'''
 file : 相对路径，相对当前文件目录
 mode ：控制模式，
 r 默认只能读,默认文件指针在文件开头，如果没有这个文件要报错
 w 只能写, 如果没有这个文件要创建这个文件，文件指针放在开头,覆盖全部的写
 a 只能写(追加) ，但是和W不一样的只是文件指针放在后面
 增加b：以二进制的形式进行文件操作rb rw ra
 增加+:代表把这个模式改为读写模型 r+ w+ a+ rb+ rw+ ra+ ,操作部分  r+只读，但是可以写，只是部分写
'''
# f = open('a.text',mode='a')


# content = f.read()
# print(content)

# f.write("1234567")

# f.close()

# 合并两张图片 第一张test01图片的上部分合成到test02的上部分
# f1 = open('test01.jpg',mode='rb')
# content1 = f1.read()
# f1.close()
#
# f2 = open('test02.jpg',mode='wb+')
#
# content = content1[0:len(content1)]
#
# f2.write(content)
# f2.close()

'''2.文件读写'''

# 2.1 定位 - 文件的指针seek(offset,参照点 = 0)，默认是参照点是开头 1，2只是针对二进制文件  tell() 当前的位置
#  参照点 0  开头    1 当前位置   2 结束

# f = open('a.text','rb')
#
# print(f.tell())
# f.seek(-2,2)
# print(f.tell())
# content = f.read()
#
# print(content)
# print(f.tell())


# 2.2 文件的读

# 2.2.1 read(文件长度) 从文件指针的开头一直默认读取到最后，内容是文件总长度,

# f = open('a.text','r')
# f.seek(2)
# content = f.read(2)
# print(content)
# print(f.tell())
# f.close()


# 2.2.2 readline(行数) 读取一行，默认读取一行,

# f = open('a.text','r')
# content = f.readline()
# print(content)
#
# content = f.readline()
# print(content)
#
# content = f.readline()
# print(content)
#
# f.close()


# 2.2.3 readlines(行数) 自动处理文件的换行符号，将处理好的数据通过list 返回
# f = open('a.text','r')
# content = f.readlines()
# print(content)
#
# # 结果 ：['12345678\n', '222222222\n', '3333333333\n', '44444444444\n', '5555555555\n', '666666666666\n', '7777777777777777\n', '8888888888888888\n', '9999999999']
#
# f.close()

# 2.2.4 遍历文件
# import collections
#
# f = open('a.text','r')  # 默认一个文件是一个迭代器，能一行一行的遍历
# result = isinstance(f,collections.Iterator)
#
# print("f是否是迭代器",result)
# for content in f:
#   print(content)
#
# # 结果 ： f是否是迭代器 True
# f.close()

# 2.2.5 判断文件是否可读readable

# import collections
#
# f = open('a.text','r')  # 默认一个文件是一个迭代器，能一行一行的遍历
# if f.readable():
#     result = isinstance(f,collections.Iterator)
#     print("f是否是迭代器",result)
#     for content in f:
#       print(content)
#
# f.close()

# 2.2.6 读取文件的选择
# f = open('a.text','r')
# # f.read()
# # f.readlines()    默认一次性加入内存 ，耗内存，提高性能
# # f.readline()     一行一行的读取 ，节约内存 ，性能差点，一般大文件用
# # for in


# # 3.文件的写write  返回写入内容的长度  writable 是否可写
# f = open('a.text','a')
# if f.writable():
#     resultLength = f.write('oooooo')
# print(resultLength)
# f.close()



'''3.文件关闭'''
'''
关闭原因：1、可以释放系统资源  2、会立即清空缓冲区的数据内容到次磁盘文件（写数据是暂时写到缓冲区，然后在写到磁盘内存中，可以通过断点调试看） 
flush() : 立即刷新缓存区数据到磁盘文件中
'''

# f = open('a.text','a')
# f.write('oooooo')
# f.flush()
# f.close()


# 以后的操作都是os模块中
'''4.文件的其他操作  重命名和删除、创建'''
# 4.1重命名  rename('源文件','目的文件') 相对路径

import os
# os.rename('a.text','aa.text')  # 改文件名，改过之后不能在改

# os.rename('First','one') #改文件夹名

# os.renames('two/two.txt','one/one.txt') #多级树状名称修改

# 4.2 删除文件或者删除目录
#os.remove('aa.text')  # 删除文件

# os.removedirs('one/one2') #递归删除空目录

# os.rmdir('one') #不递归删除目录 空目录


# 4.3 创建目录
# os.mkdir('a')  #创建目录 不支持多级创建

# os.mkdir('b',mode=0O777)  #数字权限  三种  读写可执行 421

# # 4.4 获取当前目录
# print(os.getcwd())


# 4.5切换当前目录
# os.chdir('a')
# open('aa.txt','w')

# 4.6获取目录内容列表
# ./ 当前目录   ../上层目录

# print(os.listdir('../'))


'''案例1：复制一份文件作为一个副本,注意编码'''
# import  os
# os.chdir('files')
#
# soure_file = open('souce.txt','r',encoding='utf-8')
# dst_file = open('dst_souce.txt','a',encoding='utf-8')
#
# content = soure_file.read()
# dst_file.write(content)
#
# dst_file.close()
# soure_file.close()

# 如果是大文件，需要慢慢读取

import  os
os.chdir('files')

soure_file = open('souce.txt','r',encoding='utf-8')
dst_file = open('dst_souce.txt','a',encoding='utf-8')

while True:
    content = soure_file.read(1024)
    print(len(content))
    if len(content) == 0:
        break
    dst_file.write(content)

dst_file.close()
soure_file.close()

'''案例2：文件的分类，不同后缀名的文件进行分类'''

# # 0.获取需要分类的文件目录下面的文件
# import  os
# import  shutil
#
# path = 'files'
#
# if not os.path.exists(path):
#     exit()
#
# os.chdir(path)
# file_list = os.listdir('./')
#
# # 1、遍历文件名称
# for file_name in file_list:
#
#     # 2、获取每一个文件的后缀名
#    index =  file_name.rfind('.')
#    if index == -1:
#        continue
#    extension = file_name[index+1:]
#
#    # 3.查看时候有同名的目录，如果有就直接移动，如果没有就创建之后在移动
#    if not os.path.exists(extension):
#        os.mkdir(extension)
#
#    shutil.move(file_name,extension)


'''案例3：将分好类的文件列出树状的列表清单'''

# 0.获取文件目录下的文件和子文件
import  os


def filelistWriteToTxt(dir,file):
    file_list = os.listdir(dir)
    for file_name in file_list:
        new_file_name = dir +"/"+ file_name
        #判断文件是否是目录还是文件
        if os.path.isdir(new_file_name):
            file.write(new_file_name + "\n")
            filelistWriteToTxt(new_file_name,file)
        else:
            file.write("\t"+ file_name+"\n")

    file.write("\n")





f = open('list.txt','a')
filelistWriteToTxt('files',f)
