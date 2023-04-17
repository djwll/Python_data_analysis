import csv
import matplotlib.pyplot as plt
from textblob import TextBlob as tb
from datetime import datetime
import numpy as np
positive_number = 0
negative_number = 0
normal_number = 0
count = 0
x_positive = []
x_negative = []
x_normal = []
x_rate = []
i = j = 0
count_negative = 0
count_positive = 0
count_normal = 0
"""打开读取文件，生成列表"""
with open("F:/programing/Python/201602_tweets/output.csv", "r", encoding="utf-8-sig", ) as f:
    datadict = csv.DictReader(f)#生成csv对象
    for dict1 in datadict:
        dd = datetime.strptime(dict1['TIME'], "%Y-%m-%d %H:%M:%S")#转化为detetime类型的对象
        if j == 23:
            stop = datetime.strptime("2016-02-%d %d:00:00" % (i+16, 0), "%Y-%m-%d %H:%M:%S")
            begin = datetime.strptime("2016-02-%d %d:00:00" % (i+15, j), "%Y-%m-%d %H:%M:%S")
        elif i == 14:
            break
        else:
            stop = datetime.strptime("2016-02-%d %d:00:00" % (i+15, j+1), "%Y-%m-%d %H:%M:%S")
            begin = datetime.strptime("2016-02-%d %d:00:00" % (i+15, j), "%Y-%m-%d %H:%M:%S")

        a = dd.timestamp()#转化为数字
        t = tb(dict1['TEXT']).sentiment.polarity
        if a < stop.timestamp():
            if t > 0:
                positive_number = positive_number+1
            elif t < 0:
                negative_number = negative_number+1
            elif t == 0:
                normal_number = normal_number+1
        elif a > stop.timestamp():
            j = j+1
            count_normal = count_normal + normal_number
            count_positive = count_positive + positive_number
            count_negative = count_negative + negative_number
            x_negative.append(negative_number)
            x_positive.append(positive_number)
            x_normal.append(normal_number)
            x_rate.append(negative_number/(negative_number+positive_number))
            positive_number = 0
            negative_number = 0
            normal_number = 0

        if j == 24:
            i = i+1
            print(i)
            j = 0
            break

y = np.array(['positive_emotion', 'negative_emotion', 'normal_emotion'])
x = np.array([x_positive[0], x_negative[0], x_normal[0]])
"""数据可视化"""
plt.pie(x, labels=y, radius=1.5, autopct='%3.lf%%', shadow='black')
plt.show()