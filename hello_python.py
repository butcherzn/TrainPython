#!/usr/bin/env python
# -*-coding: utf-8 -*-

# 练习python
print 'HelloPython'

# python 为动态语言，所以不需要显示的指定数据的类型
# 整数 浮点数 字符串 布尔值
print 'I\'m OK, \n Sorry'
print 100
print 1.555

# 运算符 and or not
print 1 and 2
# ->2

print True and False
# ->False

# python 中的空值 None
print None

# 字符编码

# 最早的python 内部只支持ASCII？
print '中文'
# 结果为乱码

# 标准函数 ord chr
print ord('A')
# 输出 65

print chr(65)
# 输出 A

# u'...'，代表为unicode，python3 已经修改
print u'中文'
# 输出 中文

# encode 函数
print 'ABC'.encode('utf-8')
# 输出为ABC

print u'中文'.encode('utf-8')
# 输出结果 和 上文中的 print '中文'一样

print 100 == 100


# 解码为unicode
print '\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# WTF 发现编码还是没搞懂

print '%x'%0xab
# 输出Hex %x 进制数字

# list和3目测没区别
# 常量用UP PRE_CASE Style
# 要不会被pylint 警告
# 为何使用大写
CLASSMATES = ['A', 'B', 'C']
print CLASSMATES

# 下标 0 永远是第一个
print CLASSMATES[0]

# 下标 -1 为最后一个
print CLASSMATES[-1]
print CLASSMATES[-3]

# append 添加一个元素到最后的位置
CLASSMATES.append('D')
print CLASSMATES

# insert 添加元素到指定位置
# 添加到第二位置
CLASSMATES.insert(1, 'AA')
print CLASSMATES

# pop 删除末尾元素
CLASSMATES.pop()
print CLASSMATES

# 重新添加D
CLASSMATES.append('D')

# 删除指定位置元素
temp = CLASSMATES.pop(1)
print CLASSMATES
print 'temp = %s'%temp

# 添加回去
CLASSMATES.insert(1, "AA")
print CLASSMATES

# 长度
print len(CLASSMATES)


# tuple
CLASSMATES_TUPLE = ('A', 'B', 'C')
print CLASSMATES_TUPLE

# 条件语句, Trailing Whitespace
A = 10
if A > 8:
    print u'大于8'
else:
    print u'小于等于8'


