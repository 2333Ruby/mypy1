# from selenium import webdriver
#
# webdriver.Chrome()
#
# input()


import requests
import re
import os

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
url='http://ppip.cn/'
response=requests.get(url=url,headers=headers)
print(response.content)
# content=re.findall('\u003Cp\u003E(.*?)\u003C\u002Fp',response.text)
# print(content)
# <h2 class="chapter-title" data-v-e0864cb2>