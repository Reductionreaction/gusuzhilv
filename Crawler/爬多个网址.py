import requests
from bs4 import BeautifulSoup

# 读取包含标题和网址的txt文件
with open('output.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 创建一个新的txt文件来存储提取的文本信息
output_file = open('extracted_text.txt', 'w', encoding='utf-8')

# 遍历每一行，提取网页内容
for line in lines:
    parts = line.strip().split(': ')
    title = parts[0]
    url = parts[1]

    # 发起HTTP请求获取网页内容
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # 提取目标<div>标签中的文本信息
    target_div = soup.find('div', class_='lemmaSummary_JrJb4 J-summary')
    if target_div:
        text_content = target_div.get_text()
        output_file.write(f"{title}: {text_content}\n")

output_file.close()
