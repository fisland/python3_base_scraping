import requests
from bs4 import BeautifulSoup
import html5lib
# 保存首页
def save_file(data,pic_name):
    save_path = 'pic_name'
    with open(save_file, 'w') as f:
        f.write(data)


url = 'http://www.mzitu.com/page/'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
}

# 爬的预览页面数量
preview_page_cnt = 1
parser = 'html.parser'
for cur_page in range(1, int(preview_page_cnt)+1):
    cur_url = url + str(cur_page)
    cur_page = requests.get(cur_url, headers = header)
    # 解析网页

    soup = BeautifulSoup(cur_page.text, parser)
    preview_link_list = soup.find(id='pins').find_all('a', target='_blank')[1::2]
    for link in preview_link_list:
        link = link['href']
        # print(link)
        soup = BeautifulSoup(requests.get(link).text, parser)
        pri_cnt = soup.find('div', class_='pagenavi').find_all('a')[4].get_text()
        for pic_index in range(1, int(pri_cnt)+1):
            pic_link = link+'/'+str(pic_index)
            cur_page = requests.get(pic_link, headers = header)
            soup = BeautifulSoup(cur_page.text, parser)
            pic_src = soup.find('div', 'main-image').find('img')['src']
            
            print(pic_src)

# main_page = requests.get(url, header)
# print(main_page.encoding)
# save_file(main_page.text)

