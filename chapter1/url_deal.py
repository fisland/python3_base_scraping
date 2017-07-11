#coding:utf-8
import urllib
from urllib import request

data={}
data['work'] = 'cat'

url_values = urllib.parse.urlencode(data)
url = 'http://www.baidu.com/s?'
full_url = url+url_values

data = request.urlopen(full_url).read()
data = data.decode('UTF-8', 'ignore')
print(data)