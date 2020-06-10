from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

df = pd.read_csv('founders.csv', header=None, error_bad_lines=False, names=['founder', 'founder_url', 'play_num'])

print(df)
df = df.drop_duplicates(subset=['founder'], keep='first', inplace=False)  # 去重
print(df)
df = df.sort_values('play_num', ascending=False)
print(df)

# df = pd.read_csv('music_message1.csv', header=None, error_bad_lines=False, names=['title','tag', 'text','collection_ten_thousand','play_million','songs','comments_hundred'])
# df.to_csv('music_message1_1.csv')

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

for i in df['founder_url']:
    time.sleep(1)
    url = 'https://music.163.com' + i
    response = requests.get(url=url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    founder = soup.select('.tit.f-ff2.s-fc0.f-thide')[0].get_text()
    event_count = soup.select('#event_count')[0].get_text()
    follow_count = soup.select('#follow_count')[0].get_text()
    fan_count = soup.select('#fan_count')[0].get_text()

    print(founder, event_count, follow_count, fan_count)

    with open('founder_info.csv', 'a+', encoding='utf-8-sig') as f:
        f.write(founder + ',' + event_count + ',' + follow_count + ',' + fan_count + '\n')
