#F:/programing/Python/conference/Twitter_data_2017_02/20170220-20170306_es8xkr6293_2017_03_05_22_50_activities.json
import json
import os
dirs = os.listdir("F:/programing/Python/conference/Twitter_data_2017_02/20170220-20170306_es8xkr6293_2017_03_05_22_50_activities.json")
#dirs = os.listdir("F:/programing/Python/activities/test")
i=0
for name in dirs:
    with open("F:/programing/Python/conference/Twitter_data_2017_02/20170220-20170306_es8xkr6293_2017_03_05_22_50_activities.json/"+name, 'r', encoding='utf8') as f1:
        for json_datastr1 in f1.readlines():
            #json_data0 = json.dumps(json_datastr1)
            if json_datastr1 =='\n':continue#遇到换行就跳出本次循环
            json_data1 = json.loads(json_datastr1)
            #print(json_data1["actor"]["postedTime"])
            #print(json_data1["id"])
            #print(json_data1.get("actor"))
            actor = json_data1.get("actor")
            if actor== None:break;
            i=i+1
            print(i)
            #print(i,end=' activity:')
            #print(actor.get("summary"),end ='and time:')
            #print(actor.get("postedTime"))