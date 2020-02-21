# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:29:35 2020

@author: Administrator
"""

import numpy as np
import sys
sys.path.append('qll.tool')

import Function as fun

class LiRegression(object):    #线性回归类
    def __init__(self):
        self.k = 1        #保存预测斜率
        self.b = 0        #保存预测截距
        self.dataSet = np.ones((1,1))
        
    def loadDataSet(self,k,b,n):  #此处k,b是为了生成随机点，也可用于最后评估预测准确度
        self.dataSet = fun.CreateSet(k,b,n)
        
    def train(self):
        x = self.dataSet[:,0]   #横坐标向量
        y = self.dataSet[:,1]   #纵坐标向量
        
        n = len(x)
        
        x_ = np.mean(x)         #横坐标均值
        y_ = np.mean(y)        #纵坐标均值
        self.k = (np.sum(np.multiply(x,y)) - n*x_*y_)/(np.sum(np.multiply(x,x)) - n*x_*x_)
        self.b = y_ - self.k*x_
        
        print(self.k,self.b)
        
    def draw(self,plt):
        fun.drawScatter(plt,self.dataSet) #画散点图
        x = self.dataSet[:,0]
        y = self.k*x + self.b
        plt.plot(x,y,linewidth=2,color='red')
        plt.show