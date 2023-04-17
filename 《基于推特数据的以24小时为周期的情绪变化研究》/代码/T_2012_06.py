import json
import os
dirs = os.listdir("F:/programing/Python/201206_tweets/20120610-20120624_916ep3wdjr_2012_06_24_23_50_activities.json")
#dirs = os.listdir("F:/programing/Python/activities/test")
i=0
with open("F:/programing/Python/201206_tweets/20120610-20120624_916ep3wdjr_2012_06_24_23_50_activities.json/" + dirs[0],
          'r', encoding='utf8') as f1:
    for json_datastr1 in f1.readlines():
        # json_data0 = json.dumps(json_datastr1)
        if json_datastr1 == '\n': continue  # 遇到换行就跳出本次循环
        json_data1 = json.loads(json_datastr1)
        # print(type(json_data))
        # if len(json_data) == 0:continue
        for dict1 in json_data1.values():
            print(dict1)