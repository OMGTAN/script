# -*- coding:utf-8 -*-
import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import bs4
import os


def get_html(url, header=None):
    """请求初始url"""
    response = requests.get(url, headers=header)
    try:
        if response.status_code == 200:
            # print(response.status_code)
            # print(response.text)
            return response.text
        return None
    except RequestException:
        print("请求失败")
        return None


def parse_html(html, list_data):
    """提取img的名称和图片url，并将名称和图片地址以字典形式返回"""
    soup = BeautifulSoup(html, 'html.parser')
    img = soup.find_all('img')
    for t in img:
        if isinstance(t, bs4.element.Tag):
            # print(t)
            name = t.get('alt')
            img_src = t.get('src')
            list_data.append([name, img_src])
    dict_data = dict(list_data)
    return dict_data

def get_image_content(url):
    """请求图片url，返回二进制内容"""
    print("正在下载", url)
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.content
        return None
    except RequestException:
        return None


def main(num=None, depth=None):
    base_url = 'https://www.dbmeinv.com/index.htm?'
    for i in range(1, depth):
        url = base_url + 'cid=' + str(num) + '&' + 'pager_offset=' + str(i)
        # print(url)
        header = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q = 0.9, image/webp,image/apng,*/*;q='
                      '0.8',
            'Accept-Encoding': 'gzip,deflate,br',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Host': 'www.dbmeinv.com',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0(WindowsNT6.1;Win64;x64) AppleWebKit/537.36(KHTML, likeGecko) Chrome/'
                          '70.0.3538.102Safari/537.36 '
        }
        list_data = []
        print(url)
        html = get_html(url)
        # print(html)
        dictdata = parse_html(html, list_data)
        # print(list_data)
        # print(dict(list_data))
        # print(data)
        # for url in data.values():
        #     download_image(url)
        root_dir = os.path.dirname(os.path.abspath('.'))
        save_path = root_dir + '/pics/'
        for t in dictdata.items():
            file_path = '{0}/{1}.{2}'.format(save_path, t[0], 'jpg')
            if not os.path.exists(file_path):  # 判断是否存在文件，不存在则爬取
                with open(file_path, 'wb') as f:
                    f.write(get_image_content(t[1]))
                    f.close()
                    print('文件保存成功')


if __name__ == '__main__':
    # t = main(2)
    # print(t)  # 这样打印之所以为None，是因为main函数中没有任何内容返回出来，尴尬了。。。
    main(2, 2)