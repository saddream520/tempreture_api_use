import csv

# 读取CSV文件
data=[]
# 创建空列表
with open(r"B:\番茄钟音乐\转换导入\LocationList-master\LocationList-master\China-City-List-latest.csv", 'r', encoding='utf-8') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        data.append(row)  # 每行作为列表返回

string_location=input("请输入你查询的天气:")

for row in data:
        # row=row.strip()
        if row[2]==string_location:
            print(row[0])
            break

# text=['F35CF', 'Beigang Township', '北港镇', 'TW', 'Taiwan, Province of China', '中国台湾省', 'Taiwan, Province of China', '台湾省', 'Yunlin County', '云林县', 'Asia/Taipei', '23.5920', '120.2940', '710000']
# print(text[2])