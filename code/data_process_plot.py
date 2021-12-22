import pandas as pd
import numpy as np
import math
import matplotlib
import matplotlib.pyplot as plt
from correlation import Correlation
matplotlib.rcParams['font.sans-serif']=['SimHei']

class REITS():
    def __init__(self,config) -> None:
        self.root_path = ""  #"C:/Users/10266/Desktop/中信证券/公募reits课题/"
        self.day_range,self.shangzheng_index = self.read_data()
        self.all_win_ratios_table = {}
        self.config = config 

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
        day_list =  data.iloc[start_row_index:,0]
        day_processed = []
        for day in day_list:
            day_processed.append(f"{day.year}/{day.month}/{day.day}")
        plot_data["day"] = day_processed
        
        # print(plot_data["day"][20].year,plot_data["day"][20].month,plot_data["day"][20].day)
        # assert 0
        plot_data["平安广州广河REIT_收盘价_day"] = data.iloc[start_row_index:,1].tolist()
        plot_data["浙商沪杭甬REIT_收盘价_day"] = data.iloc[start_row_index:,5].tolist()
        plot_data["高速公路2(申万)"] = data.iloc[start_row_index:,3].tolist()

        plot_data["day"].reverse()
        plot_data["平安广州广河REIT_收盘价_day"].reverse()
        plot_data["浙商沪杭甬REIT_收盘价_day"].reverse()
        plot_data["高速公路2(申万)"].reverse()


        fig = plt.figure(figsize=(8,4))
        REITS_list = ["平安广州广河REIT_收盘价_day","浙商沪杭甬REIT_收盘价_day"]
        Industry_index ="高速公路2(申万)"
        for i,REIT_name in enumerate(REITS_list):
            #ax = fig.add_subplot(f"{len(REITS_list)}1{i+1}")
            ax = fig.add_subplot(len(REITS_list),1,i+1)
            ax.set_title('REITS收盘价走势')
            ax.set_xlabel('时间_day')
            ax.set_ylabel('收盘价')
            ax.plot(plot_data["day"],plot_data[REIT_name],"r",marker="o",label=REIT_name)
            ax.set_xticks([])
            ax2 = ax.twinx()
            ax2.plot(plot_data["day"],plot_data[Industry_index],"--",marker="*",label=Industry_index)
            ax2.set_ylabel("收盘价")
            ax.legend(bbox_to_anchor=(0.1,1.2),loc="upper center")
            ax2.legend(bbox_to_anchor=(1.1,1.1),loc="upper right")
            ax2.set_xticks([])
        if self.config.plot:
            plt.show()

        corr = Correlation()
        corr.predict_one_day(day_processed,"2021/9/28",plot_data["平安广州广河REIT_收盘价_day"],plot_data[Industry_index],reit_delay=2)
        start_day = self.config.start_day
        end_day = self.config.end_day
        for REIT_name in REITS_list:
            for reit_delay in  range(1,6):
                win_ratio = corr.predict_win_ratio_range_day_fix_reit_delay(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay=reit_delay)
                print(f"delay:{reit_delay}  {start_day}- { end_day } REIT:{REIT_name},  win_ratio:{win_ratio}")
                self.all_win_ratios_table.setdefault(REIT_name,{})
                self.all_win_ratios_table[REIT_name].setdefault(reit_delay,win_ratio)
            
            best_delay_win_ratio = corr.predict_win_ratio_range_day(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay_list=self.config.reit_delay_list,window_size=self.config.window_size,ratio_choice=1)
            self.all_win_ratios_table[REIT_name]["best_auto_delay_win_ratio_by_ratio1"] = best_delay_win_ratio
            best_delay_win_ratio2 = corr.predict_win_ratio_range_day(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay_list=self.config.reit_delay_list,window_size=self.config.window_size,ratio_choice=2)
            self.all_win_ratios_table[REIT_name]["best_auto_delay_win_ratio_by_ratio2"] = best_delay_win_ratio2

    def industrial_parks(self):
        parks_data = pd.read_excel(self.root_path+"data/reits_data.xlsx",sheet_name="产业园区")
        plot_data = {}
        start_row_index = 3
        
        day_list =  parks_data.iloc[start_row_index:,0]
        day_processed = []
        for day in day_list:
            day_processed.append(f"{day.year}/{day.month}/{day.day}")
        plot_data["day"] = day_processed

        plot_data["东吴苏园产业REIT_收盘价_day"] = parks_data.iloc[start_row_index:,1].tolist()
        plot_data["博时蛇口产园REIT_收盘价_day"] = parks_data.iloc[start_row_index:,3].tolist()
        plot_data["华安张江光大REIT_收盘价_day"] = parks_data.iloc[start_row_index:,5].tolist()
        plot_data["园区开发2(申万)"] = parks_data.iloc[start_row_index:,7].tolist()

        plot_data["day"].reverse()
        plot_data["东吴苏园产业REIT_收盘价_day"].reverse()
        plot_data["博时蛇口产园REIT_收盘价_day"].reverse()
        plot_data["华安张江光大REIT_收盘价_day"].reverse()
        plot_data["园区开发2(申万)"].reverse()
        
        fig = plt.figure(figsize=(8,4))
        REITS_list = ["东吴苏园产业REIT_收盘价_day","博时蛇口产园REIT_收盘价_day","华安张江光大REIT_收盘价_day"]
        Industry_index = "园区开发2(申万)"
        for i,REIT_name in enumerate(REITS_list):
            ax = fig.add_subplot(len(REITS_list),1,i+1)
            ax.set_title('REITS收盘价走势')
            ax.set_xlabel('时间_day')
            ax.set_ylabel('收盘价')
            ax.plot(plot_data["day"],plot_data[REIT_name],"r",marker="o",label=REIT_name)
            ax.set_xticks([])
            ax2 = ax.twinx()
            ax2.plot(plot_data["day"],plot_data[Industry_index],"--",marker="*",label=Industry_index)
            ax2.set_ylabel("收盘价")
            ax.legend(bbox_to_anchor=(0.1,1.2),loc="upper center")
            ax2.legend(bbox_to_anchor=(1.1,1.1),loc="upper right")
            ax2.set_xticks([])
        if self.config.plot:
            plt.show()

        corr = Correlation()
        start_day = self.config.start_day
        end_day = self.config.end_day
        for REIT_name in REITS_list:
            for reit_delay in  range(1,6):
                win_ratio = corr.predict_win_ratio_range_day_fix_reit_delay(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay=reit_delay)
                print(f"delay:{reit_delay}  {start_day}- { end_day } REIT:{REIT_name},  win_ratio:{win_ratio}")
                self.all_win_ratios_table.setdefault(REIT_name,{})
                self.all_win_ratios_table[REIT_name].setdefault(reit_delay,win_ratio)
            
            best_delay_win_ratio = corr.predict_win_ratio_range_day(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay_list=self.config.reit_delay_list,window_size=self.config.window_size,ratio_choice=1)
            self.all_win_ratios_table[REIT_name]["best_auto_delay_win_ratio_by_ratio1"] = best_delay_win_ratio
            best_delay_win_ratio2 = corr.predict_win_ratio_range_day(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay_list=self.config.reit_delay_list,window_size=self.config.window_size,ratio_choice=2)
            self.all_win_ratios_table[REIT_name]["best_auto_delay_win_ratio_by_ratio2"] = best_delay_win_ratio2

        
    def logistics(self):
        logistics_data = pd.read_excel(self.root_path+"data/reits_data.xlsx",sheet_name="物流")
        plot_data = {}
        start_row_index = 3
        day_list =  logistics_data.iloc[start_row_index:,0]
        day_processed = []
        for day in day_list:
            day_processed.append(f"{day.year}/{day.month}/{day.day}")
        plot_data["day"] = day_processed

        plot_data["中金普洛斯REIT_收盘价_day"] = logistics_data.iloc[start_row_index:,1].tolist()
        plot_data["红土盐田港REIT_收盘价_day"] = logistics_data.iloc[start_row_index:,3].tolist()
        plot_data["物流(申万)"] = logistics_data.iloc[start_row_index:,5].tolist()

        plot_data["day"].reverse()
        plot_data["中金普洛斯REIT_收盘价_day"].reverse()
        plot_data["红土盐田港REIT_收盘价_day"].reverse()
        plot_data["物流(申万)"].reverse()
        
        fig = plt.figure(figsize=(8,4))
        REITS_list = ["中金普洛斯REIT_收盘价_day","红土盐田港REIT_收盘价_day"]
        Industry_index = "物流(申万)"
        for i,REIT_name in enumerate(REITS_list):
            ax = fig.add_subplot(len(REITS_list),1,i+1)
            ax.set_title('REITS收盘价走势')
            ax.set_xlabel('时间_day')
            ax.set_ylabel('收盘价')
            ax.plot(plot_data["day"],plot_data[REIT_name],"r",label=REIT_name)
            ax.set_xticks([])
            ax2 = ax.twinx()
            ax2.plot(plot_data["day"],plot_data[Industry_index],"--",label=Industry_index)
            ax2.set_ylabel("收盘价")
            ax.legend(bbox_to_anchor=(0.1,1.2),loc="upper center")
            ax2.legend(bbox_to_anchor=(1.1,1.1),loc="upper right")
            ax2.set_xticks([])
        if self.config.plot:
            plt.show()

        corr = Correlation()
        start_day = self.config.start_day
        end_day = self.config.end_day

        for REIT_name in REITS_list:
            for reit_delay in  range(1,6):
                win_ratio = corr.predict_win_ratio_range_day_fix_reit_delay(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay=reit_delay)
                print(f"delay:{reit_delay}  {start_day}- { end_day } REIT:{REIT_name},  win_ratio:{win_ratio}")
                self.all_win_ratios_table.setdefault(REIT_name,{})
                self.all_win_ratios_table[REIT_name].setdefault(reit_delay,win_ratio)
            
            best_delay_win_ratio = corr.predict_win_ratio_range_day(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay_list=self.config.reit_delay_list,window_size=self.config.window_size,ratio_choice=1)
            self.all_win_ratios_table[REIT_name]["best_auto_delay_win_ratio_by_ratio1"] = best_delay_win_ratio
            best_delay_win_ratio2 = corr.predict_win_ratio_range_day(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay_list=self.config.reit_delay_list,window_size=self.config.window_size,ratio_choice=2)
            self.all_win_ratios_table[REIT_name]["best_auto_delay_win_ratio_by_ratio2"] = best_delay_win_ratio2

    def water(self):
        data = pd.read_excel(self.root_path+"data/reits_data.xlsx",sheet_name="水务")
        plot_data = {}
        start_row_index = 3
        
        day_list =  data.iloc[start_row_index:,0]
        day_processed = []
        for day in day_list:
            day_processed.append(f"{day.year}/{day.month}/{day.day}")
        plot_data["day"] = day_processed

        plot_data["富国首创水务REIT_收盘价_day"] = data.iloc[start_row_index:,1].tolist()
        plot_data["水务2(申万)"] = data.iloc[start_row_index:,3].tolist()

        plot_data["day"].reverse()
        plot_data["富国首创水务REIT_收盘价_day"].reverse()
        plot_data["水务2(申万)"].reverse()
        
        fig = plt.figure(figsize=(8,4))
        REITS_list = ["富国首创水务REIT_收盘价_day"]
        Industry_index ="水务2(申万)"
        for i,REIT_name in enumerate(REITS_list):
            ax = fig.add_subplot(len(REITS_list),1,i+1)
            ax.set_title('REITS收盘价走势')
            ax.set_xlabel('时间_day')
            ax.set_ylabel('收盘价')
            ax.plot(plot_data["day"],plot_data[REIT_name],"r",marker="o",label=REIT_name)
            ax.set_xticks([])
            ax2 = ax.twinx()
            ax2.plot(plot_data["day"],plot_data[Industry_index],"--",marker="*",label=Industry_index)
            ax2.set_ylabel("收盘价")
            ax.legend(bbox_to_anchor=(0.1,1.2),loc="upper center")
            ax2.legend(bbox_to_anchor=(1.1,1.1),loc="upper right")
            ax2.set_xticks([])
        if self.config.plot:
            plt.show()

        corr = Correlation()
        start_day = self.config.start_day
        end_day = self.config.end_day

        for REIT_name in REITS_list:
            for reit_delay in  range(1,6):
                win_ratio = corr.predict_win_ratio_range_day_fix_reit_delay(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay=reit_delay)
                print(f"delay:{reit_delay}  {start_day}- { end_day } REIT:{REIT_name},  win_ratio:{win_ratio}")
                self.all_win_ratios_table.setdefault(REIT_name,{})
                self.all_win_ratios_table[REIT_name].setdefault(reit_delay,win_ratio)
            
            best_delay_win_ratio = corr.predict_win_ratio_range_day(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay_list=self.config.reit_delay_list,window_size=self.config.window_size,ratio_choice=1)
            self.all_win_ratios_table[REIT_name]["best_auto_delay_win_ratio_by_ratio1"] = best_delay_win_ratio
            best_delay_win_ratio2 = corr.predict_win_ratio_range_day(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay_list=self.config.reit_delay_list,window_size=self.config.window_size,ratio_choice=2)
            self.all_win_ratios_table[REIT_name]["best_auto_delay_win_ratio_by_ratio2"] = best_delay_win_ratio2


    def environmental_protection(self):
        data = pd.read_excel(self.root_path+"data/reits_data.xlsx",sheet_name="环保")
        plot_data = {}
        start_row_index = 3
        
        day_list =  data.iloc[start_row_index:,0]
        day_processed = []
        for day in day_list:
            day_processed.append(f"{day.year}/{day.month}/{day.day}")
        plot_data["day"] = day_processed

        plot_data["中航首钢绿能_收盘价_day"] = data.iloc[start_row_index:,1].tolist()
        plot_data["环保工程及服务2(申万)"] = data.iloc[start_row_index:,3].tolist()
        
        plot_data["day"].reverse()
        plot_data["中航首钢绿能_收盘价_day"].reverse()
        plot_data["环保工程及服务2(申万)"].reverse()
        

        fig = plt.figure(figsize=(8,4))
        REITS_list = ["中航首钢绿能_收盘价_day"]
        Industry_index ="环保工程及服务2(申万)"
        for i,REIT_name in enumerate(REITS_list):
            ax = fig.add_subplot(len(REITS_list),1,i+1)
            ax.set_title('REITS收盘价走势')
            ax.set_xlabel('时间_day')
            ax.set_ylabel('收盘价')
            ax.plot(plot_data["day"],plot_data[REIT_name],"r",marker="o",label=REIT_name)
            ax.set_xticks([])

            ax2 = ax.twinx()
            ax2.plot(plot_data["day"],plot_data[Industry_index],"--",marker="*",label=Industry_index)
            ax2.set_ylabel("收盘价")
            ax.legend(bbox_to_anchor=(0.1,1.2),loc="upper center")
            ax2.legend(bbox_to_anchor=(1.1,1.1),loc="upper right")
            ax2.set_xticks([])

        if self.config.plot:
            plt.show()

        corr = Correlation()
        start_day = self.config.start_day
        end_day = self.config.end_day

        for REIT_name in REITS_list:
            for reit_delay in  range(1,6):
                win_ratio = corr.predict_win_ratio_range_day_fix_reit_delay(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay=reit_delay)
                print(f"delay:{reit_delay}  {start_day}- { end_day } REIT:{REIT_name},  win_ratio:{win_ratio}")
                self.all_win_ratios_table.setdefault(REIT_name,{})
                self.all_win_ratios_table[REIT_name].setdefault(reit_delay,win_ratio)
            
            best_delay_win_ratio = corr.predict_win_ratio_range_day(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay_list=self.config.reit_delay_list,window_size=self.config.window_size,ratio_choice=1)
            self.all_win_ratios_table[REIT_name]["best_auto_delay_win_ratio_by_ratio1"] = best_delay_win_ratio
            best_delay_win_ratio2 = corr.predict_win_ratio_range_day(day_processed,start_day,end_day,plot_data[REIT_name],plot_data[Industry_index],reit_delay_list=self.config.reit_delay_list,window_size=self.config.window_size,ratio_choice=2)
            self.all_win_ratios_table[REIT_name]["best_auto_delay_win_ratio_by_ratio2"] = best_delay_win_ratio2

def print_dict(one_dict,recursive_level):
	if recursive_level >=2:
		return str(one_dict)

	res = ""
	curtab = "\t"*(recursive_level+1)
	for k,v in one_dict.items():
		if type(v) == type({}):
			res += f'{curtab}"{k}":{print_dict(v,recursive_level+1)}\n'
		else:
			if type(v) == type([]):
				res += f'{curtab}"{k}":{v},\n'
			else:
				res += f'{curtab}"{k}":"{v}",\n'
	if recursive_level == 0:
		print("\n{\n"+res+"},")
	else:
		return "\n\t{\n"+res+"\t},"

class Config():
    def __init__(self):
        self.window_size = 6 
        self.reit_delay_list = [1,2,3,4,5]
        self.plot = True
        self.start_day = "2021/8/25"
        self.end_day = "2021/10/13"


if __name__ == "__main__":
    config = Config()
    reits = REITS(config)
    reits.highway()
    reits.industrial_parks()
    reits.logistics()
    reits.water()
    reits.environmental_protection()

    print_dict(reits.all_win_ratios_table,0)
    #highway()
    #industrial_parks()
    #logistics()
    #water()
    #environmental_protection()
