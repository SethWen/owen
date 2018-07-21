"""
    author: Shawn
    time  : 7/21/18 5:25 PM
    desc  : 采集猫眼评论信息
    update: Shawn 7/21/18 5:25 PM
"""

import requests
import json
import time
import random

agents = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'chrome/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ucbrowser/64.0.3282.140 Safari/537.36',
    'safri/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36',
    'ucbrowser/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) webkit/64.0.3282.140 Safari/537.36',
    'Mozilla',
]


# 下载第一页数据
def get_one_page(url):
    headers = {
        'Host': 'm.maoyan.com',
        'User-Agent': random.choice(agents)
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        print('body: %s' % response.text)
        return response.text

    return None


# 解析第一页数据
def parse_one_page(html):
    data = json.loads(html)['cmts']

    for item in data:
        yield {
            'comment': item['content'],
            'date': item['time'].split(' ')[0],
            'rate': item['score'],
            'city': item['cityName'],
            'nickname': item['nickName']
        }


# 保存数据到文本文档
def save_to_txt():
    for i in range(1, 1001):
        print('start...')
        url = 'http://m.maoyan.com/mmdb/comments/movie/248566.json?_v_=yes&offset=' + str(i)
        # url = 'http://www.baidu.com'
        html = get_one_page(url)
        print('正在保存第 %d 页。' % i)

        for item in parse_one_page(html):
            with open('old.txt', 'a', encoding='utf-8') as f:
                f.write(
                    item['date'] + ',' + item['nickname'] + ',' + item['city'] + ',' + str(item['rate']) + ',' + item[
                        'comment'] + '\n')

        # time.sleep(0.1 + float(random.randint(1, 100)) / 20)
        time.sleep(0.2)


if __name__ == '__main__':
    save_to_txt()
