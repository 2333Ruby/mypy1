import requests
import re
from openpyxl import Workbook
from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
option=webdriver.ChromeOptions()
option.add_experimental_option('detach',True)
option.add_argument('--disable-blink-features=AutomationControlled')
service=Service('D:/32670/1python3.8\chromedriver.exe')
# driver=webdriver.Chrome(options=option,service=service)#初始化浏览器

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
url_all=[]
s1=[]
s2=[]
s3=[]
s4=[]
s5=[]
s6=[]
s7=[]
s8=[]
m=0

name=['公司全名','工作地点(省)','岗位名字','岗位描述','岗位职责','要求工作年限','学历要求','薪资范围','链接']
for b in range(1,4):
    url =f'https://sou.zhaopin.com/?jl=763&kw=%E7%89%A9%E6%B5%81&p={b}'
    content=requests.get(url=url,headers=headers).text

    url_1=re.findall('positionURL":"(.*?)",',content)
    for i in url_1:
        urls=i
        url_all.append(i)
        driver = webdriver.Chrome(options=option, service=service)  # 初始化浏览器
        driver.get(i)
        sleep(1)
        source = driver.page_source.encode().decode('utf-8')
        soup = BeautifulSoup(source, 'html.parser')
        try:
            title = soup.select('#root > div:nth-child(5) > div.app-main__right > div > div.company > a.company__title') # 公司名
            local = re.findall('workCity":"(.*?)"', source)[0]  # 城市名
            gw = re.findall('<h3 class="summary-plane__title">(.*?)<!----></h3>', source)[0]  # 岗位名
            dis = re.findall('<span class="describtion__skills-item">(.*?)</span>', source)[0]  # 岗位描述

            res = soup.select('#root > div:nth-child(5) > div.app-main__left > div.job-detail > div.describtion > div.describtion__detail-content > p')
            c=''.join('%s'%d for d in res)
            # res = re.findall('岗位职责：</p><p>(.*?)</p><p>任职要求', source)[0]  # 岗位职责
            year = re.findall('"positionWorkingExp":"(.*?)",', source)[m]  # 工作年限
            edu = re.findall(',"education":"(.*?)",', source)[0]  # 要求学历
            salary = re.findall('<span class="summary-plane__salary">(.*?)</span>', source)[0]  # 薪资范围
        except IndexError:
            print('出错')
            continue
        driver.quit()

        print(title[0].string)
        # m+=1
        s1.append(title[0].string)
        s2.append(local)
        s3.append(gw)
        s4.append(dis)
        s5.append(c)
        s6.append(year)
        s7.append(edu)
        s8.append(salary)
all_list=[]
all_list.append(s1)
all_list.append(s2)
all_list.append(s3)
all_list.append(s4)
all_list.append(s5)
all_list.append(s6)
all_list.append(s7)
all_list.append(s8)
all_list.append(url_all)
wb=Workbook()
ws=wb['Sheet']
ws.append(['公司全名','工作地点(省)','岗位名字','岗位描述','岗位职责','要求工作年限','学历要求','薪资范围','链接'])
for i in range(len(all_list[0])):
    d=all_list[0][i],all_list[1][i],all_list[2][i],all_list[3][i],all_list[4][i],all_list[5][i],all_list[6][i],all_list[7][i],all_list[8][i]
    ws.append(d)
wb.save(r'广州.xlsx')

