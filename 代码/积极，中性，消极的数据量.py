import csv
from textblob import TextBlob as tb
polarity_count = 0
negative_count = 0
normal_count = 0
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
print(polarity_count)
print(negative_count)
print(normal_count)


