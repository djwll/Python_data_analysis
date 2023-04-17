import pandas as pd #导入pandas包
import csv
import matplotlib.pyplot as plt
from textblob import TextBlob as tb
time = []
text = []
LAT = []
LON = []
count = 0

# Importing datetime.
from datetime import datetime
# Creating a datetime object so we can test.

# Converting a to string in the desired format (YYYYMMDD) using strftime
# and then to int.
"""a = int(a.strftime("%Y-%m-%d %H:%M:%S"))
print (type(a))"""

with open("F:/programing/Python/201602_tweets/output.csv","r",encoding="utf-8-sig",) as f:
        datadict= csv.DictReader(f)
        for dict1 in datadict:
            dd = datetime.strptime(dict1['TIME'], "%Y-%m-%d %H:%M:%S")
            time.append(dd)
            text.append(dict1['TEXT'])
            LAT.append(dict1['LAT'])
            LON.append(dict1['LON'])

#a = time[0].timestamp()
#print(a)
time_number = []
emotion_polarity_number = []
"""for time1 in time:
    count = count+1
    print(count, end=' : ')
    print(time1, end=' : ')
    a = time[count].timestamp()
    time_number.append(a)
    #print('\n',a,end ='\n')
    #print(type(time1))
    print(text[count-1], end=' polarity: ')
    emotion = tb(text[count-1])
    #print(emotion.sentiment.polarity)
    emotion_polarity_number.append(emotion.sentiment.polarity)
    #print(tuple.)"""
for time1 in time:#获取data_number
    a = time[count].timestamp()
    #a = time[count].time()
    #print(type(a))
    print(a)
    time_number.append(a)
    emotion = tb(text[count])
    emotion_polarity_number.append(emotion.sentiment.polarity)
    count = count+1
    #if count==500 :break
    print(count)
#这两组循环是同时进行的，因为他们之间互相并不冲突和干扰，时间上并不干扰
time_number1 = []
count = 0
max = max(time_number)#放在循环外面，不然运行时间直接起飞
min = min(time_number)
for number in time_number:
    #a = (number-max(time_number))/(max(time_number)-min(time_number))
    a = (number-min)/(max-min)
    time_number1.append(a)
    count = count+1
    print(count)
    #if count == 500: break"""

plt.scatter(time_number,emotion_polarity_number,s=0.01, c='blue', alpha=0.5)
plt.title('T_Trelation', fontsize='large', fontweight='bold')
plt.xlabel('time', fontsize='large', fontweight='bold')
plt.ylabel('polarity', fontsize='large', fontweight='bold')
plt.show()



