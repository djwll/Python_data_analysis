import json
import os
import matplotlib.pyplot as plt
import numpy as np
from textblob import TextBlob as tb
dirs = os.listdir("F:/programing/Python/201206_tweets/20120610-20120624_916ep3wdjr_2012_06_24_23_50_activities.json")
#dirs = os.listdir("F:/programing/Python/activities/test")
i = 0
friends_count = []
emotion_number = []
with open("F:/programing/Python/201206_tweets/20120610-20120624_916ep3wdjr_2012_06_24_23_50_activities.json/" + dirs[0],
          'r', encoding='utf8') as f1:
    for json_datastr1 in f1.readlines():
        # json_data0 = json.dumps(json_datastr1)
        if json_datastr1 == '\n': continue  # 遇到换行就跳出本次循环
        json_data1 = json.loads(json_datastr1)
        # print(type(json_data))
        # if len(json_data) == 0:continue
        print(type(json_data1))
        try:
            t = tb(json_data1['text']).sentiment.polarity
            #KeyError
        except:
            print("没有text")
            continue
        t = tb(json_data1['text']).sentiment.polarity
        emotion_number.append(t)
        print(t)
        print(json_data1['user']['friends_count'])
        friends_count.append(json_data1['user']['friends_count'])
        i = i+1
        print(i)
x = list(range(0, i))
print(len(x))
print(len(emotion_number))
#size = (friends_count/np.max(friends_count))*1000
#plt.scatter(x,emotion_number,s=size)
#plt.plot(x,friends_count,color='red')
plt.bar(x, friends_count, width=0.6)
plt.show()