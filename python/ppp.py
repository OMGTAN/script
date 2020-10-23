import re

import requests

# 知乎有反爬虫，加入http headers伪装浏览器
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36",
    "Connection": "keep-alive",
    "Accept": "text/html,application/json,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"}

# 知乎问题id
question_id = 406321189
interval = 20
offset = 0
rank = 100
novels_count = dict()

url = f'https://www.zhihu.com/api/v4/questions/{question_id}/answers?include=content&limit={interval}&offset={offset}&sort_by=default'
html = requests.get(url, headers=headers)
answers = html.json()['data']
print(answers)