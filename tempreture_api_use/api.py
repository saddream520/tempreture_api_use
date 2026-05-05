import requests
import os
import csv
# 和风天气API
# 请求url
api_key="12dbfc155af5452bb60265c62fdee6ab"
url="https://nt6tuqt4db.re.qweatherapi.com/v7/weather/now"

# params={
#     "location":"101010100",
#     "key":api_key,
# }


params={
    "location":"101010100",
    "key":api_key,
} 

# def get_locationTemptrue():
response=requests.get(url,params=params)
# 解析json数据
data=response.json()
print(data)
# if data["code"]=="200":
#             now=data["now"]
#             print(f"当前温度：{now['temp']}℃")
#             print(f"当前天气：{now['text']}")
#             print(f"体感温度：{now['feelsLike']}℃")
#             print(f"湿度：{now['humidity']}%")
#             print(f"风速：{now['windScale']}级")
#             print(f"风向：{now['windDir']}")
# print(response.status_code)
# print(response.text)