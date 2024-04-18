#这个脚本可以爬取单页面的信息
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_url = "https://baike.baidu.com"


url = 'https://suzhou.bendibao.com/xiuxian/202443/122873.shtm'
response = requests.get(url)
if response.encoding == 'ISO-8859-1':
    encodings = requests.utils.get_encodings_from_content(response.text)
    if encodings:
        response.encoding = encodings[0]
    else:
        response.encoding = response.apparent_encoding

soup = BeautifulSoup(response.text, 'html.parser')
for div in soup.find_all('div',class_='main-recommand'):
    div.decomposed()
# 获取标题
title = soup.title.string
content=soup.find('div',class_='article-content').get_text(strip=True)

print('标题:', title)
print('文本',content)



