import pandas as pd
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
matplotlib.rcParams['font.sans-serif']=['SimHei']

class REITS():
    def __init__(self) -> None:
        self.root_path = "C:/Users/10266/Desktop/中信证券/公募reits课题/"
        self.day_range,self.shangzheng_index = self.read_data()

    def read_data(self):
        shangzheng_data = pd.read_excel(self.root_path+"data/reits_data.xlsx",sheet_name="大盘指数")
        start_row_index = 2
        day = shangzheng_data.iloc[start_row_index:,0]
        shangzheng_index = shangzheng_data.iloc[start_row_index:,1]
        return day,shangzheng_index
    def highway(self):
        data = pd.read_excel(self.root_path+"data/reits_data.xlsx",sheet_name="高速公路")
        plot_data = {}
        start_row_index = 4
        plot_data["day"] = data.iloc[start_row_index:,0]
        print(plot_data["day"])
        plot_data["平安广州广河REIT_收盘价_day"] = data.iloc[start_row_index:,1]
        plot_data["浙商沪杭甬REIT_收盘价_day"] = data.iloc[start_row_index:,5]
        plot_data["高速公路2(申万)"] = data.iloc[start_row_index:,3]
        fig = plt.figure(figsize=(8,4))
        REITS_list = ["平安广州广河REIT_收盘价_day","浙商沪杭甬REIT_收盘价_day"]
        Industry_index ="高速公路2(申万)"
        for i,REIT_name in enumerate(REITS_list):
            ax = fig.add_subplot(f"{len(REITS_list)}1{i+1}")
            ax.set_title('REITS收盘价走势')
            ax.set_xlabel('时间_day')
            ax.set_ylabel('收盘价')
            ax.plot(plot_data["day"],plot_data[REIT_name],"r",label=REIT_name)
            ax2 = ax.twinx()
            ax2.plot(plot_data["day"],plot_data[Industry_index],"--",label=Industry_index)
            ax2.set_ylabel("收盘价")
            ax.legend(bbox_to_anchor=(0.1,1.2),loc="upper center")
            ax2.legend(bbox_to_anchor=(1.1,1.1),loc="upper right")
        plt.show()   
        # plot_data["week"] = highway_data.iloc[start_row_index:,8]
        # plot_data["平安广州广河REIT_week"] = highway_data.iloc[start_row_index:,9]
        # plot_data["浙商沪杭甬REIT_week"] = highway_data.iloc[start_row_index:,10]
        # plot_data["高速公路2_week"] = highway_data.iloc[start_row_index:,11]
    def industrial_parks(self):
        parks_data = pd.read_excel(self.root_path+"data/reits_data.xlsx",sheet_name="产业园区")
        plot_data = {}
        start_row_index = 3
        plot_data["day"] = parks_data.iloc[start_row_index:,0]
        print(plot_data["day"])
        plot_data["东吴苏园产业REIT_收盘价_day"] = parks_data.iloc[start_row_index:,1]
        plot_data["博时蛇口产园REIT_收盘价_day"] = parks_data.iloc[start_row_index:,3]
        plot_data["华安张江光大REIT_收盘价_day"] = parks_data.iloc[start_row_index:,5]
        plot_data["园区开发2(申万)"] = parks_data.iloc[start_row_index:,7]
        
        fig = plt.figure(figsize=(8,4))
        REITS_list = ["东吴苏园产业REIT_收盘价_day","博时蛇口产园REIT_收盘价_day","华安张江光大REIT_收盘价_day"]
        for i,REIT_name in enumerate(REITS_list):
            ax = fig.add_subplot(f"{len(REITS_list)}1{i+1}")
            ax.set_title('REITS收盘价走势')
            ax.set_xlabel('时间_day')
            ax.set_ylabel('收盘价')
            ax.plot(plot_data["day"],plot_data[REIT_name],"r",label=REIT_name)
            ax2 = ax.twinx()
            ax2.plot(plot_data["day"],plot_data["园区开发2(申万)"],"--",label="园区开发2(申万)")
            ax2.set_ylabel("收盘价")
            ax.legend(bbox_to_anchor=(0.1,1.2),loc="upper center")
            ax2.legend(bbox_to_anchor=(1.1,1.1),loc="upper right")
        plt.show()
    def logistics(self):
        logistics_data = pd.read_excel(self.root_path+"data/reits_data.xlsx",sheet_name="物流")
        plot_data = {}
        start_row_index = 3
        plot_data["day"] = logistics_data.iloc[start_row_index:,0]
        print(plot_data["day"])
        plot_data["中金普洛斯REIT_收盘价_day"] = logistics_data.iloc[start_row_index:,1]
        plot_data["红土盐田港REIT_收盘价_day"] = logistics_data.iloc[start_row_index:,3]
        plot_data["物流(申万)"] = logistics_data.iloc[start_row_index:,5]
        
        fig = plt.figure(figsize=(8,4))
        REITS_list = ["中金普洛斯REIT_收盘价_day","红土盐田港REIT_收盘价_day"]
        Industry_index = "物流(申万)"
        for i,REIT_name in enumerate(REITS_list):
            ax = fig.add_subplot(f"{len(REITS_list)}1{i+1}")
            ax.set_title('REITS收盘价走势')
            ax.set_xlabel('时间_day')
            ax.set_ylabel('收盘价')
            ax.plot(plot_data["day"],plot_data[REIT_name],"r",label=REIT_name)
            ax2 = ax.twinx()
            ax2.plot(plot_data["day"],plot_data[Industry_index],"--",label=Industry_index)
            ax2.set_ylabel("收盘价")
            ax.legend(bbox_to_anchor=(0.1,1.2),loc="upper center")
            ax2.legend(bbox_to_anchor=(1.1,1.1),loc="upper right")
        plt.show()
    def water(self):
        data = pd.read_excel(self.root_path+"data/reits_data.xlsx",sheet_name="水务")
        plot_data = {}
        start_row_index = 3
        plot_data["day"] = data.iloc[start_row_index:,0]
        print(plot_data["day"])
        plot_data["富国首创水务REIT_收盘价_day"] = data.iloc[start_row_index:,1]
        plot_data["水务2(申万)"] = data.iloc[start_row_index:,3]
        
        fig = plt.figure(figsize=(8,4))
        REITS_list = ["富国首创水务REIT_收盘价_day"]
        Industry_index ="水务2(申万)"
        for i,REIT_name in enumerate(REITS_list):
            ax = fig.add_subplot(f"{len(REITS_list)}1{i+1}")
            ax.set_title('REITS收盘价走势')
            ax.set_xlabel('时间_day')
            ax.set_ylabel('收盘价')
            ax.plot(plot_data["day"],plot_data[REIT_name],"r",label=REIT_name)
            ax2 = ax.twinx()
            ax2.plot(plot_data["day"],plot_data[Industry_index],"--",label=Industry_index)
            ax2.set_ylabel("收盘价")
            ax.legend(bbox_to_anchor=(0.1,1.2),loc="upper center")
            ax2.legend(bbox_to_anchor=(1.1,1.1),loc="upper right")
        plt.show()
    def environmental_protection(self):
        data = pd.read_excel(self.root_path+"data/reits_data.xlsx",sheet_name="环保")
        plot_data = {}
        start_row_index = 3
        plot_data["day"] = data.iloc[start_row_index:,0]
        print(plot_data["day"])
        plot_data["中航首钢绿能_收盘价_day"] = data.iloc[start_row_index:,1]
        plot_data["环保工程及服务2(申万)"] = data.iloc[start_row_index:,3]
        
        fig = plt.figure(figsize=(8,4))
        REITS_list = ["中航首钢绿能_收盘价_day"]
        Industry_index ="环保工程及服务2(申万)"
        for i,REIT_name in enumerate(REITS_list):
            ax = fig.add_subplot(f"{len(REITS_list)}1{i+1}")
            ax.set_title('REITS收盘价走势')
            ax.set_xlabel('时间_day')
            ax.set_ylabel('收盘价')
            ax.plot(plot_data["day"],plot_data[REIT_name],"r",label=REIT_name)
            ax2 = ax.twinx()
            ax2.plot(plot_data["day"],plot_data[Industry_index],"--",label=Industry_index)
            ax2.set_ylabel("收盘价")
            ax.legend(bbox_to_anchor=(0.1,1.2),loc="upper center")
            ax2.legend(bbox_to_anchor=(1.1,1.1),loc="upper right")
        plt.show()
if __name__ == "__main__":
    reits = REITS()
    reits.highway()
    #highway()
    #industrial_parks()
    #logistics()
    #water()
    #environmental_protection()
