# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import sys
sys.path.append('../qll.tool')
import LiRegression as li

lingre = li.LiRegression()
lingre.loadDataSet(3,1,100)  #在直线Y=kX+b附近生成100个随机点
lingre.train()  #求出回归直线的斜率和截距
lingre.draw(plt)  #显示效果