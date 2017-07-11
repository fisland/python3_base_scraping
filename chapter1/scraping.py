#coding:utf-8
from urllib import request
url = 'http://baidu.com'
data = request.urlopen(url).read()
data = data.decode('utf-8')
print(data)