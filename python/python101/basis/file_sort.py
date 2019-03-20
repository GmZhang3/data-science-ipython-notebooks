# -*- coding:UTF-8 -*-

#方法1
# 读取源文件，将所有数据放入列表，使用sorted函数执行列，进行排序；
#排序列表，写入到输出文件中。
f = open('test.csv')
output_file = open("test_out.csv","w")
tmp_list = []
for line in f.readlines():
    item = line.strip().split(",")
    tmp_list.append(item)
# print tmp_list
f.close()
sorted_list = sorted(tmp_list,key = lambda x:int(x[1]),reverse=True)
for row in sorted_list:
    row = [str(x) for x in row]
    output_file.write(",".join(row) + '\n')
output_file.close()

#方法2
print('\n'.join(sorted(open('test.csv'), key=lambda s: int(s.split(",")[1]),reverse=1)))
