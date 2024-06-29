import requests
import re
from selenium import webdriver
import os
driver=webdriver.Edge()
driver.get('https://www.mhua5.com/index.php/chapter/1771139')
source=driver.page_source
# print(source)
comic_url=re.findall('<img src="(.*?)" alt',source)
# print(comic_url)

url=[]
l=len(comic_url)-1
for i in range(2,l):
    url.append(comic_url[i])
# print(url)
c_url='\n'.join(url)
print(c_url)
for b in range(len(c_url)):
    img = open(f'comic/{b}.jpg','wb')
    for a in c_url:
        res=requests.get(a)
        for chunk in res.iter_content(100000):
            img.write(chunk)
    # with open('"D:/1Pycharm，启动！\pythonProject1\新建文件夹\comic"',mode='wb',encoding='utf-8') as f:
    #     f.write(res)
    '''需要给你新下载的文件命名以基础的图片格式结尾，否则会报错'''