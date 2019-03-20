#!/usr/bin/python
# -*- coding: UTF-8 -*-

import numpy as np
from sklearn.cluster import DBSCAN
def distince(vect1,vect2):
    dist = (vect1-vect2)*((vect1-vect2).T)
    return dist[0,0]
if __name__ == "__main__":
    v1 = np.array([1,2])
    v2 = np.array([1,1])
    print v1 -v2
    print (v1 -v2).T
    vv = (v1 -v2)*((v1 -v2).T)
    print vv
    # print type(v1)
    # print v2
    # print distince(v1,v2)