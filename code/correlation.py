import pandas as pd
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1+math.exp(-x))
#计算两个信号量之间的相关性
class Correlation():
    def __init__():
        pass 

    def pearson(self,X,Y): #https://zh.wikipedia.org/wiki/%E7%9A%AE%E5%B0%94%E9%80%8A%E7%A7%AF%E7%9F%A9%E7%9B%B8%E5%85%B3%E7%B3%BB%E6%95%B0
        if len(X) != len(Y):
            raise "Not same size error"
        avg_x = sum(X) / len(X)
        avg_y = sum(Y) / len(Y)
        cov_x_y = 0
        for i in range(len(X)):
            cov_x_y += (X[i] - avg_x) * (Y[i] - avg_y)
        
        deltaX = 0
        deltaY = 0
        for i in range(len(X)):
            deltaX += (X[i] - avg_x)**2
            deltaY += (Y[i] - avg_y)**2
        deltaX = math.sqrt(deltaX)
        deltaY = math.sqrt(deltaY)

        return cov_x_y / (deltaX * deltaY)
    def designed_correlation(self,X,Y):
        X_rose_fell = []
        Y_rose_fell = []
        for i in range(1,len(X)):
            X_rose_fell.append((X[i] - X[i-1]) / X[i])
            Y_rose_fell.append((Y[i] - Y[i-1]) / Y[i])
        
        same_direction_cnt = 0
        ratio_cnt = 0
        for i in range(len(X_rose_fell)):
            if X_rose_fell[i] >= 0 and Y_rose_fell[i] >= 0:
                same_direction_cnt += 1
            elif X_rose_fell[i] < 0 and Y_rose_fell[i] < 0:
                same_direction_cnt += 1
            ratio_cnt += abs(X_rose_fell[i] - Y_rose_fell[i])
        ratio_cnt = ratio_cnt / len(X_rose_fell)
        corr_ratio = 1 - sigmoid(ratio_cnt)
        
        return same_direction_cnt / len(X_rose_fell) , corr_ratio


    def time_latency_correlation(self,X,Y,x_latecy):
        X = X[x_latecy:]
        return self.pearson(X,Y)




if __name__ == "__main__":
    pass
    #read_data()
    #plot_function()
    #highway()

