#coding:utf-8
# 解压缩
import gzip
def ungzip(data):
    try:
        print('正在解压')
        data = gzip.decompress(data)
        print('解压完毕')
    except :
        print('无需解压')
    return data

# 正则匹配
import re
def getXSRF(data):
    cer = re.compile('name="_xsrf" value="(.*)"', flags=0)
    strlist = cer.findall(data)
    return strlist[0]

# 发射post
from http import cookiejar
from urllib import request
from urllib import parse
def getOpener(head):
    cj = cookiejar.CookieJar()
    pro = request.HTTPCookieProcessor(cj)
    opener = request.build_opener(pro)
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

# 正式运行
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}
url = 'http://zhihu.com/'
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = ungzip(data)
_xsrf = getXSRF(data.decode('utf-8'))
print(_xsrf)

# 写下来
def saveFile(data):
    save_path = '/Users/fisland/Documents/GitHub/python3_base_scraping/chapter4/zhihu.html'
    with open(save_path, 'w') as f:
        f.write(data)

url += 'login/email'
user = 'whereisfisland@163.com'
password = 'Zjf9437879228.'
postDict = {
    '_xsrf' : _xsrf,
    'email' : user,
    'password' : password,
    'captcha_type' : 'cn'
}
postData = parse.urlencode(postDict).encode()
op = opener.open(url, postData)
data = op.read()
data = ungzip(data).decode('utf-8')

print(type(data))
saveFile(data)