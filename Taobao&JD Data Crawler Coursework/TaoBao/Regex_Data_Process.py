import re
import pandas as pd

filenamestr = 'Raw_phones_data.csv'
df = pd.read_csv(filenamestr, encoding='utf-8')
restr = r'(huawei|iPhone|纽曼|华为|vivo|OPPO|红米|尼凯恩|小米|苹果|天语|Huawei|VOVG|' \
        r'诺基亚|vjvj|YEPEN|通皓轩|小米|Xiaomi|小辣椒|三星|Samsung|Meizu|releme|飞利浦|Nokia' \
        r'|索爱|天语|朵唯|一加七|meizu)([A-Za-z0-9\s])*'
# 2.对匹配项正则筛选
df['title'] = df['title'].apply(lambda x: re.search(restr, x).group(0) if re.search(restr, x) else '0')
df = df.drop(df[df.title == '0'].index)
df.to_csv("taobao_result.csv", encoding='gbk')
