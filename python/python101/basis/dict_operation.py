# -*- coding:UTF-8 -*-
#找出字典中value最大的键值对的键/值/或键值对
dict = {"one":1,"two":2,"three":3}
# 方法1
#lambda 是匿名函数，key是min的参数，告诉它按找第几个元素来比较
print max(dict.items(),key = lambda x:x[1])
#('three', 3)  键值对
print max(dict.items(),key = lambda x:x[1])[0]
# three 键
print max(dict.items(),key = lambda x:x[1])[1]
# 3 最大的值
##
# 方法2
#max(dict,key=dict.get)方法获得字典dict中value的最大值所对应的键的方法，
# max(dict, key)方法首先遍历迭代器，并将返回值作为参数传递给key对应的函数，
# 然后将函数的执行结果传给key，并以此时key值为标准进行大小判断，返回最大值。
dict = {1:1,2:2,3:3}
print int(max(dict,key=dict.get))
#testt