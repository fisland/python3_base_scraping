import re
import urllib
from urllib import request

from collections import deque

queue = deque()
visited = set()

url = 'http://news.dbanotes.net'
queue.append(url)
cnt = 0

while queue:
    url = queue.popleft()
    visited |= {url}

    print('已经抓取：'+str(cnt)+'   正在抓取<----' + url)
    cnt += 1
    urlop = request.urlopen(url, timeout=2)
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    # 避免异常， 使用try
    try:
        data = urlop.read().decode('utf-8')
    except :
        continue

    linkre = re.compile(r'class="title".+?href="(.+?)"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print('加入队列 --->' + x)
        