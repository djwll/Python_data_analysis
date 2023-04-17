import csv
count = 0
with open("F:/programing/Python/201602_tweets/output.csv","r",encoding="utf-8-sig",) as f:
        datadict= csv.DictReader(f)
        for dict1 in datadict:
            count = count + 1
print(count)


