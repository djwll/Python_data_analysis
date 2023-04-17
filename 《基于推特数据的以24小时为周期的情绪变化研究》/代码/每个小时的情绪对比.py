import csv
import matplotlib.pyplot as plt
from textblob import TextBlob as tb
from datetime import datetime
from scipy import interpolate
import numpy as np
positive_number = 0
negative_number = 0
normal_number =0
count = 0
x_positive = []
x_negative = []
x_normal = []
i=j=0
x_negative_average = []
x_positive_average = []
average_positive = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
average_negative = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x_rate=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
x_all = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
"""打开读取文件，生成列表"""
with open("F:/programing/Python/201602_tweets/output.csv", "r", encoding="utf-8-sig", ) as f:
    datadict = csv.DictReader(f)#生成csv对象
    for dict1 in datadict:
        dd = datetime.strptime(dict1['TIME'], "%Y-%m-%d %H:%M:%S")#转化为detetime类型的对象
        if j==23:
            stop = datetime.strptime("2016-02-%d %d:00:00"%(i+16,0), "%Y-%m-%d %H:%M:%S")
            begin = datetime.strptime("2016-02-%d %d:00:00"%(i+15,j), "%Y-%m-%d %H:%M:%S")
        elif i==14:
            break
        else:
            stop = datetime.strptime("2016-02-%d %d:00:00"%(i+15,j+1), "%Y-%m-%d %H:%M:%S")
            begin = datetime.strptime("2016-02-%d %d:00:00"%(i+15,j), "%Y-%m-%d %H:%M:%S")

        a = dd.timestamp()#转化为数字
        t = tb(dict1['TEXT']).sentiment.polarity
        #time.append(a)
        if a < stop.timestamp():
            if t > 0:
                positive_number = positive_number+1
            elif t < 0:
                negative_number = negative_number+1
            elif t == 0:
                normal_number = normal_number+1
        elif a > stop.timestamp():
            average_positive[j] = average_positive[j]+positive_number/14
            average_negative[j] = average_negative[j]+negative_number/14
            x_rate[j] = average_negative[j]/(average_positive[j]+average_negative[j])
            x_all[j] = x_all[j] + (average_positive[j]+average_negative[j])/14
            j = j+1
            x_negative.append(negative_number)
            x_positive.append(positive_number)
            x_normal.append(normal_number)
            #x_rate.append(negative_number/(negative_number+positive_number))
            positive_number = 0
            negative_number = 0
            normal_number = 0

        if j == 24:
            i = i+1
            print(i)
            j = 0
            #if i == 3: break

plt.bar(np.arange(335), +np.array(x_positive),width=0.6)
plt.bar(np.arange(335), -np.array(x_negative),width=0.6)
plt.show()