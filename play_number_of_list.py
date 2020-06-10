from bs4 import BeautifulSoup
import requests
import time
import datetime

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}

for i in range(0, 1330, 35):
    print(i)
    time.sleep(1)
    url = 'https://music.163.com/discover/playlist/?cat=欧美&order=hot&limit=35&offset=' + str(i)
    response = requests.get(url=url, headers=headers)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    # 获取包含歌单详情页网址的标签
    ids = soup.select('.dec a')
    # 获取包含歌单索引页信息的标签
    lis = soup.select('#m-pl-container li')
    print(len(lis))
    today = datetime.date.today()
    formatted_today = today.strftime('%y%m%d')
    for j in range(len(lis)):
        # 获取歌单详情页地址
        url = ids[j]['href']
        # 获取歌单播放量
        play = lis[j].select('.nb')[0].get_text()
        # 将信息写入CSV文件中
        with open('amoutOfPlaylist.csv', 'a+', encoding='utf-8-sig') as f:
            f.write(formatted_today + ',' + url + ',' + play + '\n')
