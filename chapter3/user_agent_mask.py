# first

from urllib import request
url = 'http://baidu.com'
'''
req = request.Request(url, headers={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})
oper = request.urlopen(req)
data = oper.read().decode('utf-8')
print(data)
'''
# second
def saveFile(data):
    save_path = '/Users/fisland/Documents/GitHub/use_python3_webscraping/chapter3/test.html'
    with open(save_path, 'w') as f:
        f.write(data)

import http.cookiejar
def makeMyOpener(head={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
}):
    cj = http.cookiejar.CookieJar()
    opener = request.build_opener(request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

oper = makeMyOpener()
uop = oper.open(url, timeout=1000)
data = uop.read().decode('utf-8')
saveFile(data)
print('ok')
