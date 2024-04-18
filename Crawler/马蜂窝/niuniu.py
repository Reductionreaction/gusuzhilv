from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pandas as pd
import time

#df = pd.DataFrame(columns =['name','description', 'transport', 'telephone', 'ticket', 'opening_hours', 'location', 'retime', 'inter_attr'])

data = []

links = ['https://www.mafengwo.cn/poi/3084.html',
 'https://www.mafengwo.cn/poi/16081.html',
 'https://www.mafengwo.cn/poi/6944.html',
 'https://www.mafengwo.cn/poi/639.html',
 'https://www.mafengwo.cn/poi/16205.html',
 'https://www.mafengwo.cn/poi/5684.html',
 'https://www.mafengwo.cn/poi/5426246.html',
 'https://www.mafengwo.cn/poi/5434859.html',
 'https://www.mafengwo.cn/poi/33682012.html',
 'https://www.mafengwo.cn/poi/3903460.html',
 'https://www.mafengwo.cn/poi/30383106.html',
 'https://www.mafengwo.cn/poi/5434780.html',
 'https://www.mafengwo.cn/poi/17510.html',
 'https://www.mafengwo.cn/poi/5426956.html',
 'https://www.mafengwo.cn/poi/23256.html',
 'https://www.mafengwo.cn/poi/3727362.html',
 'https://www.mafengwo.cn/poi/70047780.html',
 'https://www.mafengwo.cn/poi/6325144.html',
]



def get_data(html_content):
      # 启动浏览器
      # 设置Chrome浏览器为无头模式
      chrome_options = Options()
      chrome_options.add_argument("--headless")


      driver = webdriver.Chrome(options=chrome_options)

      # 破解反扒机制
      driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
          "source": """
        Object.defineProperty(navigator, 'webdriver', {
          get: () => undefined
        })
      """

      })

      driver.get(html_content)

      try:
          # 显式等待，等待class为title的div元素出现
          title = WebDriverWait(driver, 10).until(
              EC.presence_of_all_elements_located((By.CLASS_NAME, "title"))
          )

          des_element = driver.find_element(By.CSS_SELECTOR, 'div.summary')
          description = des_element.text
          print(description)

          tel_element = driver.find_element(By.CSS_SELECTOR, 'ul.baseinfo.clearfix li.tel div.content')
          telephone = tel_element.text
          print(telephone)

          time_element = driver.find_element(By.CSS_SELECTOR, 'ul.baseinfo.clearfix li.item-time div.content')
          recommended_time = time_element.text
          print(recommended_time)

          ticket_info_element = driver.find_element(By.XPATH, '//dt[contains(text(), "门票")]/following-sibling::dd')
          ticket_info = ticket_info_element.text
          print(ticket_info)

          traffic_info_element = driver.find_element(By.XPATH, '//dt[contains(text(), "交通")]/following-sibling::dd')
          traffic_info = traffic_info_element.text
          print(traffic_info)

          opening_hours_element = driver.find_element(By.XPATH, '//dt[contains(text(), "开放时间")]/following-sibling::dd')
          opening_hours = opening_hours_element.text
          print(opening_hours)

          # 爬取地址信息
          loc_element = driver.find_element(By.CSS_SELECTOR, 'div.mhd p.sub')
          location = loc_element.text
          print(location)

          # 查找所有的景点名称
          attraction_elements = driver.find_elements(By.CSS_SELECTOR, 'ul.mlist a')
          attraction_names = [elem.text for elem in attraction_elements if elem.text != '']
          print(attraction_names)

          for div in title:
              # 获取div中的文本
              text = div.text
              print(text)
              data.append(
                  [text, description, traffic_info, tel_element, ticket_info, opening_hours, location,
                   recommended_time,
                   attraction_names])

         # data.append(
         #     [title, description, traffic_info, tel_element, ticket_info, opening_hours, location, recommended_time,
           #    attraction_names])




          driver.quit()

      except:
          print('找不到')
          driver.quit()




for link in links:
    print(link)
    get_data(link)
    #time.sleep(5)



print(data)

with open('mafengwo.txt','w',encoding='utf-8')as file:
    for onedata in data:
        file.write(str(onedata)+'\n')