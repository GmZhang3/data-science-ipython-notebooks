#coding=utf-8

import sys

last_key = None
sum_show = 0
sum_click = 0
key = None
last_value = None

if __name__ == "__main__":
    file = open("foo2.txt")
    # for line in sys.stdin:
    for line in file.readlines():
        print "line:",line
        var = line.strip().split("\t")
        (key, regression_value) = (var[0], var[1])

        if last_key != key :
            if key :
                print "%s\t%s\t%s" % (regression_value, key, "\t".join(var[2:]))

            last_key = key
            last_value = "\t".join(var[2:])