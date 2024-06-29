import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
option=webdriver.ChromeOptions()
from time import sleep
n=[]
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
option.add_experimental_option('detach',True)
option.add_argument('--disable-blink-features=AutomationControlled')
service=Service('D:/32670/1python3.8\chromedriver.exe')
driver=webdriver.Chrome(options=option,service=service)
driver.get('http://jobs.zhaopin.com/CC000632371J90250029000.htm')

# encoding = 'utf-8'
sleep(3)
# driver.get('https://jobs.zhaopin.com/CC135128370J00170482311.htm')
source=driver.page_source.encode().decode('utf-8')
soup= BeautifulSoup(source,'html.parser')
# title=soup.select('#root > div:nth-child(5) > div.app-main__right > div > div.company > a.company__title')
# title=re.findall('<div class="company__description">(.*?)1',source)#公司名
# local=re.findall('workCity":"(.*?)"',source)#城市名
# local=soup.select(source,'#root > div.job-summary > div > div > div.summary-plane__bottom.clearfix > div.summary-plane__left > ul')
# gw=re.findall('<h3 class="summary-plane__title">(.*?)<!----></h3>',source)#岗位名
# gw=soup.select(source,'#root > div.job-summary > div > div > h3')
# dis=re.findall('<span class="describtion__skills-item">(.*?)</span>',source)#岗位描述
dis=soup.select('#root > div:nth-child(5) > div.app-main__left > div.job-detail > div.describtion > div.describtion__skills > div')
# dis=soup.select('#root > div:nth-child(5) > div.app-main__left > div.job-detail > div.describtion > div.describtion__detail-content > p')
# c=''.join('%s'%d for d in dis)
# c=''.join(n)
# res=re.findall('岗位职责：</p><p>(.*?)</p><p>任职要求',source)[0]#岗位职责
# year=re.findall('"positionWorkingExp":"(.*?)",',source)#工作年限
# edu=re.findall(',"education":"(.*?)",',source)#要求学历
# salary=re.findall('<span class="summary-plane__salary">(.*?)</span>',source)#薪资范围
# print(source)
# print(title)
# print(local)
print(dis.string)
# print(gw)
# print(res)
# print(year)
# print(edu)
# print(salary)
