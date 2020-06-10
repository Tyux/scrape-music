from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

df = pd.read_csv('playlist.csv', header=None, error_bad_lines=False, names=['url', 'title', 'play', 'user'])

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

for i in df['url']:
    time.sleep(2)
    url = 'https://music.163.com' + i
    response = requests.get(url=url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')

    # 获取创建者url
    founder = soup.select('.s-fc7')[0].get_text()
    # print(founder)
    founder_url = soup.select('.s-fc7')[0]['href']
    play_num = soup.select('#play-count')[0].get_text()

    print(founder, founder_url, play_num)

    with open('founders.csv', 'a+', encoding='utf-8-sig') as f:
        f.write(founder + ',' + founder_url + ',' + play_num + '\n')
