#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import hashlib
import math

# config
deli1 = '\001'
deli2 = '\t'

def get_sha1(src):
	return hashlib.sha1(src).hexdigest()


#show click feature_1 ... feature_n = n+2

#train_data=open('train_data', 'w')
if __name__ == "__main__":
    feature_start = 1
    file = open("foo.txt")
    file2 = open("foo2.txt","w")
    # for line in sys.stdin:
    for line in file.readlines():
        # print "line:",line
        try:
            items = line.strip().split(r"^A")
            if len(items) == 1:
                items = line.strip().split(deli2)
            target_value = items[0]

            sign = get_sha1("*".join(items[feature_start:]))

            print "%s\t%s\t%s" % (sign, target_value, "\t".join(items[feature_start:]))
            out_str = str(sign) + "\t" + str(target_value) + "\t" + "\t".join(items[feature_start:]) + "\n"
            file2.write(out_str)
        except:
            sys.stderr.write('error: %s\n' % line)
            continue
    file.close()
    file2.close()
