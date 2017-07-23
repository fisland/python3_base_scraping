#!/usr/bin/env python
#coding:utf-8

import requests
from bs4 import BeautifulSoup
import html5lib
import os
import time

preview_page_cnt = 70
parser = 'html.parser'
cur_path = os.getcwd() + '/'

url = 'http://www.mmjpg.com/home/'

header = {
    'User-Agent':'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

# 保存图片
def save_file(data, pic_name):
    save_path = pic_name
    if os.path.exists(save_path):
        print('Photo exists')
    else:
        with open(save_path, 'wb') as f:
            f.write(data)

# 创建目录
def create_dir(pic_dir, pic_detail_name):
    pic_path = cur_path+pic_detail_name #dir_name+
    if os.path.exists(pic_path):
        print('Directory Exist!')
    else:
        os.mkdir(pic_path)
    return pic_path

# 图片下载
def image_src_Downlaod(url, headers, try_nums=2):
    '''下载，可以重连，默认次数为2
    '''
    print('开始下载', url)
    try:
        html = requests.get(url, header)
    except expression as e:
        html = None
        if try_nums > 0:
            downlaod(url, header, try_nums -1)
    return html

for cur_page in range(1, int(preview_page_cnt+1)):
    cur_url = url+str(cur_page)
    cur_page = requests.get(cur_url, headers=header)
    html_doc=str(cur_page.content,'utf-8')
    # print(cur_page.text)
    soup = BeautifulSoup(html_doc, parser)
    links = soup.find_all('div', class_='pic')[0].find_all('a', target='_blank')[1::2]

    for link in links:
        dir_detail_name = link.get_text()
        link = link['href']
        dir_name = link.strip('http://www.mmjpg.com/mm/').replace('?','')
        print(link, dir_name)
        # 获取图片数量
        pri_cnt = soup.find('div', class_='page').find_all('a')[5].get_text()
        # 创建目录
        pic_path = create_dir(dir_name, dir_detail_name)
        # 进入目录，开始下载
        os.chdir(pic_path)
        print('下载'+dir_name+'...')
        # 遍历获取每页图片的地址
        for pic_index in range(1, int(pri_cnt)+1):
            pic_link = link+'/'+str(pic_index)
            # cur_page = requests.get(pic_link, headers = header)
            
            cur_page = image_src_Downlaod(pic_link, header)
            soup = BeautifulSoup(cur_page.text, parser)
            try:
                pic_src = soup.find('div', class_='content').find('img')['src']
            except AttributeError as e:
                print(e)

            pic_name = pic_src.split('/')[-1]

            save_file(requests.get(pic_src, headers = header).content, pic_name)

            print(pic_src)
            time.sleep(0.1)

        os.chdir(cur_path)
    print('爬虫完成')
