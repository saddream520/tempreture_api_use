import requests
import os
import csv

# 地址编码转化
def trans_place():
 data=[]
 with open(r"B:\番茄钟音乐\转换导入\LocationList-master\LocationList-master\China-City-List-latest.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)  # 每行作为列表返回
    string_location=input("请输入你查询的天气:")
    for row in data:
        # row=row.strip()
        if row[2]==string_location:
            row[0]=str(row[0])
            pass
            return str(row[0])
            
def check_now_temptrue():
   p=trans_place()
   API_key="12dbfc155af5452bb60265c62fdee6ab"
   url="https://nt6tuqt4db.re.qweatherapi.com/v7/weather/now"
   params={
      "location":p,
      "key":API_key,
   }
   response=requests.get(url,params=params)
   temp_data=response.json()
   if temp_data["code"]=="200":
            now=temp_data["now"]
            print(f"更新时间:{now['obsTime']}")
            print(f"当前温度：{now['temp']}℃")
            print(f"当前天气：{now['text']}")
            print(f"体感温度：{now['feelsLike']}℃")
            print(f"湿度：{now['humidity']}%")
            print(f"风速：{now['windScale']}级")
            print(f"风向：{now['windDir']}")

check_now_temptrue()