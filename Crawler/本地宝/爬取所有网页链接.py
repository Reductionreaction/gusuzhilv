#https://suzhou.bendibao.com/xiuxian/jrhd/list2.htm

import  requests
from bs4 import  BeautifulSoup as bs


base_url='https://suzhou.bendibao.com/xiuxian/jrhd/list'

for i in range(1,10):
    url=base_url+str(i)+'.htm'
    response=requests.get(url)
    response.encoding=response.apparent_encoding
    soup=bs(response.text,'html.parser')
    links = []
    for dt in soup.find_all('dt'):
        a_tag = dt.find('a', href=True)  # 确保<a>标签有href属性
        if a_tag and 'http' in a_tag['href']:  # 检查是否是完整的链接
            links.append(a_tag['href'])

    # 打印所有链接
    for link in links:
        print(link)