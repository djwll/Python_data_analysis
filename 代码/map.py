import pandas as pd
from mpl_toolkits.basemap import Basemap
import csv
import matplotlib.pyplot as plt
from textblob import TextBlob as tb
import numpy as np

emotion_positive_number = []
emotion_negative_number = []
lat_positive=[]
lat_negative=[]
lon_positive=[]
lon_negative=[]
count = 0
"""打开读取文件，生成列表"""
with open("F:/programing/Python/201602_tweets/output.csv", "r", encoding="utf-8-sig", ) as f:
    datadict = csv.DictReader(f)#生成csv对象
    for dict1 in datadict:
        t = tb(dict1['TEXT']).sentiment.polarity
        if t>=0.125:
            emotion_positive_number.append(t)
            lat_positive.append(dict1['LAT'])
            lon_positive.append(dict1['LON'])
        else:
            emotion_negative_number.append(t)
            lon_negative.append(dict1['LON'])
            lat_negative.append(dict1['LAT'])
        print(len(emotion_positive_number)+len(emotion_negative_number))
        if len(emotion_positive_number)+len(emotion_negative_number)==1000:break


plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False
posi = pd.read_csv(r"F:/programing/Python/201602_tweets/output.csv")

#map = Basemap(projection='stere', lat_0=posi['LAT'][1], lon_0=posi['LON'][1], llcrnrlat=23.41, urcrnrlat=45.44, llcrnrlon=-118.67,urcrnrlon=-64.52,rsphere=6371200.,resolution='i',area_thresh=10000)
#map = Basemap(projection='stere', lat_0=posi['LAT'][1], lon_0=posi['LON'][1])
map = Basemap(width=12000000, height=9000000, projection='lcc',resolution='c', lat_0=posi['LAT'][1], lon_0=posi['LON'][1])
map.drawmapboundary()
map.drawstates()
map.drawcoastlines()
map.drawcountries()

"""parallels = np.arange(0.,90,10.)
map.drawparallels(parallels,labels=[1,0,0,0],fontsize=10)
#posi = pd.read_csv(r"F:/programing/Python/201602_tweets/output.csv")
meridians = np.arange(-110.,-60.,10.)
map.drawmeridians(meridians,labels=[0,0,0,1], fontsize=10)"""
#lat = np.array(posi['LAT'])
#lon = np.array(posi['LON'])
#pop = np.array(posi["pop"][0:500],dtype=float#
lat = np.array(np.array(lat_negative))
lon = np.array(np.array(lon_negative))
#size = (pop/np.max(pop))*1000
x,y = map(lon,lat)#将x,y化为map对象
#消极情绪
map.scatter(x, y,s=0.1,color='blue')
#积极情绪
a,b=map(np.array(np.array(lon_positive)),np.array(np.array(lat_positive)))
map.scatter(a, b, s=0.1,color='red')
#map.scatter(np.array(lat_negative) , np.array(lon_negative), s=10000,color='blue')
plt.title('英国')
plt.show()
