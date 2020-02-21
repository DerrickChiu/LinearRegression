# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:02:42 2020

@author: Administrator
"""

import numpy as np

def CreateSet(k,b,n):   #在直线Y=kX+b附近随机生成若干点
    x = np.linspace(0,5.0,n)
    y = []
    for i in range(n):
        sign = np.random.rand(1,1)
        if sign[0,0] > 0.5:
            sign = 1
        else:
            sign = -1
        eta = np.random.rand(1,1)[0,0]
        
        y.append(k*x[i] + b + eta*sign)
        
    data = np.ones((n,2))
    for j in range(n):
        data[j,:] = [x[j],y[j]]
     
    return data
    

def drawScatter(plt,data):      #绘制散点图
    plt.scatter(data[:,0],data[:,1],c='green')