import requests
import chardet
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service
option=webdriver.EdgeOptions()
option.add_experimental_option('detach',True)
service=Service('D:/32670/1python3.8\msedgedriver.exe')
driver=webdriver.Edge(options=option,service=service)
driver.get('https://jobs.zhaopin.com/CC135128370J00170482311.htm')

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
url='https://www.qidian.com/chapter/1037068783/753437190/'
content=requests.get(url=url,headers=headers).content.decode('utf-8')
soup=BeautifulSoup(content,'html.parser')
print(soup)
# encoding = chardet.detect(content)['encoding']
# new_code=content.decode('unicode_escape')
# print(content)
# print(encoding)
# print(new_code)