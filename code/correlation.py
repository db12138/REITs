import pandas as pd
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt

def sigmoid(x):
    return 1 / (1+math.exp(-x))
#计算两个信号量之间的相关性
class Correlation():
    def __init__(self):
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
        if len(X) != len(Y):
            raise "not same size error"
        same_direction_cnt = 0
        ratio_cnt = 0
        for i in range(len(X)):
            if X[i] >= 0 and Y[i] >= 0:
                same_direction_cnt += 1
            elif X[i] < 0 and Y[i] < 0:
                same_direction_cnt += 1
            ratio_cnt += abs(X[i] - Y[i])
        ratio_cnt = ratio_cnt / len(X)
        #print(ratio_cnt)
        corr_ratio = 1 - sigmoid(ratio_cnt)
        
        return same_direction_cnt / len(X) , corr_ratio


    def time_latency_correlation(self,X,Y,day_index,x_latency,window_size=5,corr_function_type ="diy"):
        X_rose_fell = [0]
        Y_rose_fell = [0]
        for i in range(1,len(X)):
            X_rose_fell.append((X[i] - X[i-1]) / X[i-1])
            Y_rose_fell.append((Y[i] - Y[i-1]) / Y[i-1])

        x_data = X_rose_fell[day_index-window_size:day_index]
        y_data = Y_rose_fell[day_index-x_latency-window_size:day_index-x_latency]
        if corr_function_type == "pearson":
            return self.pearson(x_data,y_data)
        elif corr_function_type == "diy":
            return self.designed_correlation(x_data,y_data)
        else:
            raise "No such correlation index"

    def predict_one_day(self,day_list,day,X,Y,reit_delay):
        predict_day = day_list.index(day)
        rate1,rate2 = self.time_latency_correlation(X,Y,predict_day,x_latency=reit_delay,window_size=6)
        #print(rate1,rate2)
        predict_result = (Y[predict_day-reit_delay] - Y[predict_day-reit_delay-1]) / Y[predict_day-reit_delay-1]
        true_result = (X[predict_day] - X[predict_day-1]) / X[predict_day-1]
        if (true_result >=0 and predict_result >=0) or (true_result <0 and predict_result <0):
            # print("TRUE")
            return True
        else:
            return False

    def predict_win_ratio_range_day(self,day_list,start_day,end_day,X,Y,reit_delay=2):
        start_index = day_list.index(start_day)
        end_index = day_list.index(end_day)
        candicate_day_list  = day_list[start_index:end_index]
        win_ratio = 0
        for day in candicate_day_list:
            result = self.predict_one_day(day_list,day,X,Y,reit_delay)
            if result:
                win_ratio += 1

        win_ratio /= len(candicate_day_list)
        return win_ratio

if __name__ == "__main__":
    pass
    #read_data()
    #plot_function()
    #highway()

