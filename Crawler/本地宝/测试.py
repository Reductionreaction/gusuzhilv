#http://suzhou.bendibao.com/xiuxian/2023424/112575.shtm

import requests
from bs4 import BeautifulSoup as bs

url="http://suzhou.bendibao.com/xiuxian/2023424/112575.shtm"

response=requests.get(url)
response.encoding=response.apparent_encoding
soup=bs(response.text,'html.parser')
niuniu=soup.find('div',id='add_ewm_content')
niuniu.decompose()
content=soup.find('div',class_='article-content')
print(content)