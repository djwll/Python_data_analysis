import json
import os
dirs = os.listdir("F:/programing/Python/201206_tweets/20120610-20120624_916ep3wdjr_2012_06_24_23_50_activities.json")
#dirs = os.listdir("F:/programing/Python/activities/test")
i=0
for name in dirs:
    with open("F:/programing/Python/201206_tweets/20120610-20120624_916ep3wdjr_2012_06_24_23_50_activities.json/"+name, 'r', encoding='utf8') as f1:
        for json_datastr1 in f1.readlines(1):
            #json_data0 = json.dumps(json_datastr1)
            if json_datastr1 =='\n':continue#遇到换行就跳出本次循环
            json_data1 = json.loads(json_datastr1)
            #print(type(json_data))
            #if len(json_data) == 0:continue
            print(i, end=' text:')
            print(len(json_data1))
            #print(json_data1)
            print(json_data1.get("text"))
            i = i + 1
            #except UnicodeError:
                #continue

"""with open('activities_201206100000_201206100010.json','r',encoding='utf8') as f1:
            for json_datastr1 in f1.readlines():
                json_data1 = json.loads(json_datastr1)
                print(i, end=' text:')
                print(json_data1.get("text"))
                i = i + 1
with open('activities_201206100050_201206100100.json','r', encoding='utf8') as f1:
    for json_datastr1 in f1.readlines():
        json_data1 = json.loads(json_datastr1)
        print(i, end=' text:')
        print(json_data1.get("text"))
        i = i + 1

with open('activities_201206100100_201206100110.json', 'r', encoding='utf8') as f1:
    for json_datastr1 in f1.readlines():
        json_data1 = json.loads(json_datastr1)
        print(i, end=' text:')
        print(json_data1.get("text"))
        i = i + 1"""

"""with open('activities_201206100050_201206100120.json', 'r', encoding='utf8') as f1:
    for json_datastr1 in f1.readlines():
        json_data1 = json.loads(json_datastr1)
        print(i, end=' text:')
        print(json_data1.get("text"))
        i = i + 1

with open('activities_201206100050_201206100130.json', 'r', encoding='utf8') as f1:
    for json_datastr1 in f1.readlines():
        json_data1 = json.loads(json_datastr1)
        print(i, end=' text:')
        print(json_data1.get("text"))
        i = i + 1
with open('activities_201206100050_201206100140.json', 'r', encoding='utf8') as f1:
    for json_datastr1 in f1.readlines():
        json_data1 = json.loads(json_datastr1)
        print(i, end=' text:')
        print(json_data1.get("text"))
        i = i + 1
with open('activities_201206100050_201206100150.json', 'r', encoding='utf8') as f1:
    for json_datastr1 in f1.readlines():
        json_data1 = json.loads(json_datastr1)
        print(i, end=' text:')
        print(json_data1.get("text"))
        i = i + 1

with open('activities_201206100050_201206100200.json', 'r', encoding='utf8') as f1:
    for json_datastr1 in f1.readlines():
        json_data1 = json.loads(json_datastr1)
        print(i, end=' text:')
        print(json_data1.get("text"))
        i = i + 1
print(i)"""
"""for json_datastr2 in f2.readlines():
                       json_data2 = json.loads(json_datastr2)
                       text_list.append(json_data2['text'])
                       print(text_list[i])
                       print(len(text_list))
                       i=i+1"""


"""print(json_data["text"])
                  print(i, end=' place:')
                  print(json_data["place"]["full_name"])
                  i=i+1
                  print(len(text_list))"""
"""for json_datastr2 in f2.readlines():
                  json_data = json.loads(json_datastr2)
                  print(i, end=' text:')
                  print(json_data["text"])
                  text_list.append(json_data["text"])
                  print(i, end=' place:')
                  print(json_data["place"]["full_name"])
                  i=i+1
print(len(text_list))"""

"""with open('F:/programing/Python/activities/20170220-20170306_es8xkr6293_2017_02_20_00_00_activities.json', 'r', encoding ='utf8') as fp:
    i = 0
    for json_datastr in fp.readlines():
        json_data = json.loads(json_datastr)
        print(i, end=':')
        print(json_data["id"])
        print(i, end=' place:')"""
"""fp = open('F:/programing/Python/activities/activities_201206100130_201206100140.json','r',encoding='utf8')
i = 0
for json_datastr in fp.readlines():
      json_data= json.loads(json_datastr)
      if len(json_datastr) == 0:
            continue
      print(i, end=' text:')
      print(json_data["text"])
      print(i, end=' place:')
      print(json_data["place"]["full_name"])
      i=i+1
fp.close()"""