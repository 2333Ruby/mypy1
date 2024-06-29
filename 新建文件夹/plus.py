import requests
import re
import os
import bs4
from selenium import webdriver
import chardet
headers={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
url='https://www.qidian.com/chapter/1031940621/705235484/'
response=requests.get(url=url,headers=headers,timeout=5)#.text
# encoding = chardet.detect(response)['encoding']
response.encoding=chardet.detect(response.content)['encoding']
print(response.text)




# browser.get(url)

