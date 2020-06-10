from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from sklearn import preprocessing


# 去重
# df = pd.read_csv('founder_info.csv',  error_bad_lines=False)
# print(df)
# df = df.drop_duplicates(subset=['founder'], keep='first', inplace=False)  # 去重
# print(df)
# # 排序
# # df = df.sort_values('play_num', ascending=False)
# # print(df)
# df.to_csv('founder_info1.csv', encoding='utf_8_sig')


data = pd.read_csv("founder_info.csv")
select_num = 40

# 离差标准化
# data_list = []
# for c in ['event_count', 'follow_count', 'fan_count']:
#     sf_max = (data[c][:select_num]).max()
#     sf_min = data[c][:select_num].min()
#     res = (data[c][:select_num] - sf_min) / (sf_max - sf_min)
#     # print(res)
#     data_list.append(res)


# z-score标准化  适用于最大值和最小值未知的情况
sf1 = data['founder'][:select_num]
res1 = preprocessing.scale(data['event_count'][:select_num])
res2 = preprocessing.scale(data['follow_count'][:select_num])
res3 = preprocessing.scale(data['fan_count'][:select_num])
print(res1, res2, res3)


# 写入csv
# test = pd.DataFrame({'founder': data['founder'][:select_num], 'event_count': data_list[0], 'follow_count': data_list[1], 'fan_count': data_list[2]})
test = pd.DataFrame({'founder': sf1, 'event_count': res1, 'follow_count': res2, 'fan_count': res3})
print(test)
# test.to_csv('founder_info_standard.csv')
test.to_csv('founder_info_zscore.csv')
