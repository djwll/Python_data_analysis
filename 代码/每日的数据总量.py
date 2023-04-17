import csv
import matplotlib.pyplot as plt
from textblob import TextBlob as tb
from datetime import datetime
import numpy as np


count = 0
y = []
i = j = 0

"""打开读取文件，生成列表"""
with open("F:/programing/Python/201602_tweets/output.csv", "r", encoding="utf-8-sig", ) as f:
    datadict = csv.DictReader(f)#生成csv对象
    for dict1 in datadict:
        dd = datetime.strptime(dict1['TIME'], "%Y-%m-%d %H:%M:%S")#转化为detetime类型的对象
        if j == 23:
            stop = datetime.strptime("2016-02-%d %d:00:00"%(i+16,0), "%Y-%m-%d %H:%M:%S")
            begin = datetime.strptime("2016-02-%d %d:00:00"%(i+15,j), "%Y-%m-%d %H:%M:%S")
        elif i == 14:
            break
        else:
            stop = datetime.strptime("2016-02-%d %d:00:00"%(i+15,j+1), "%Y-%m-%d %H:%M:%S")
            begin = datetime.strptime("2016-02-%d %d:00:00"%(i+15,j), "%Y-%m-%d %H:%M:%S")
        count = count + 1
        a = dd.timestamp()#转化为数字
        if a > stop.timestamp():
            j = j+1
        if j == 24:
            i = i+1
            y.append(count)
            print(count)
            print(i)
            j = 0
            count = 0
""""#折线图
x = list(range(0, 13))
plt.plot(x, y, color='black')"""
print(y)
#直方图
plt.bar(np.arange(13), np.array(y),width=0.3)

#plt.plot(y,average_negative,color='blue')
plt.show()
