#!/usr/bin/env python
# -*- coding:UTF-8 -*-
'''
Created on 2018年1月14日
@author: liuyazhuang
'''
# import sys
# #输入为标准输入stdin
# for line in sys.stdin:
#     #删除开头和结尾的空格
#     line = line.strip()
#     #以默认空格分隔行单词到words列表
#     words = line.split()
#     for word in words:
#         #输出所有单词，格式为“单词，1”以便作为Reduce的输入
#         print '%s\t%s' % (word, 1)

#IDE中实现mapper
file = open("input")
file2 = open("mapper_out","w")
for line in file.readlines():
    items = line.strip().split()
    if len(items) < 1:
        continue
    for item in items:
        # print "%s \t %s" % (item,1)
        # print "%s \t %s" % (item,1)
        file2.write(str(item) + "\t" + str(1) + "\n")
file.close()
file2.close()

