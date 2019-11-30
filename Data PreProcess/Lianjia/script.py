import json
import csv
import codecs

f = open('MyData.json')
data = json.load(f)
# print(data)
f.close()

f = codecs.open('test.csv', 'w', 'utf_8_sig')  # 解决写入csv时中文乱码
writer = csv.writer(f);
for item in data:
    writer.writerow([item['name'], item['type'], item['errMsg']])
f.close()