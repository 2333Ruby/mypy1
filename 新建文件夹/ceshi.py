from selenium import webdriver
import chardet
from selenium.webdriver.edge.service import Service
from time import sleep
option=webdriver.EdgeOptions()
option.add_experimental_option('detach',True)
option.add_argument('--disable-blink-features=AutomationControlled')
service=Service('D:/32670/1python3.8\msedgedriver.exe')
driver=webdriver.Edge(options=option,service=service)
driver.get('https://jobs.zhaopin.com/CC135128370J00170482311.htm')
# encoding = 'utf-8'
source=driver.page_source.encode().decode('utf-8')

print(source)


# print(source)