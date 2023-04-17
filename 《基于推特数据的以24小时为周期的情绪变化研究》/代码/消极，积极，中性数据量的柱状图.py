import csv
from textblob import TextBlob as tb
import numpy as np
import matplotlib.pyplot as plt

polarity_count = 0
negative_count = 0
normal_count = 0
count = 0
x = [0, 0, 0]
with open("F:/programing/Python/201602_tweets/output.csv","r",encoding="utf-8-sig",) as f:
        datadict= csv.DictReader(f)
        for dict1 in datadict:
            t = tb(dict1['TEXT']).sentiment.polarity
            if t == 0:
                normal_count = normal_count + 1
            elif t > 0:
                negative_count = negative_count + 1
            else:
                polarity_count = polarity_count + 1
            count = count + 1
            print(count)
x[0] = polarity_count
x[1] = negative_count
x[2] = normal_count
plt.bar(np.arange(3), np.array(x),width=0.3)
plt.show()
