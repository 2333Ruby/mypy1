# import requests
# comic=open('comic.jpg','wb')
# url=[]
# res = requests.get(url)
# for chunk in res.iter_content(100000):
#     comic.write(chunk)

# import re
# text = '2024-5-1'
# text = re.sub('(\\w{4})-(\\w{1})-(\\w{1})', r'\3日\2月\1年', text)
# print(text)

# txt = '赵宏达是个傻逼'
# txt = re.sub('傻逼', '****', txt)
# print(txt)


# import pyautogui

# a = pyautogui.alert(text='are you OK?', title='OK',button='o')
# print(a)
'''此方法只有一个button无buttons属性'''
# b = pyautogui.confirm('select one', buttons=['A', 'B', 'C'], title='select')
# print(b)
# c = pyautogui.password('请输入：',title='请输入密码')
# print(c)
# d = pyautogui.prompt('请输入一个数字：',title='number')
# print(d)

# a = 0.01


# def main(x):
#     x = x+2*x
#     return x
#
#
# for i in range(29):
#     d = main(a)
#     a = d
#
#
# if __name__ == '__main__':
#
#     print(d)

# import pyautogui
# import random
# t = random.random()
# print(t)
# pyautogui.sleep(t)
# print(t)

# t = random.uniform(1, 2)
# print(t)
# pyautogui.sleep(t)
# print(t)


# import requests
from selenium import webdriver
import json
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.webdriver.common.by import By

# driver = webdriver.Chrome()
option = webdriver.ChromeOptions()
option.add_experimental_option('detach', True)
service = Service('D:/32670/1python3.8\chromedriver.exe')
driver = webdriver.Chrome(options=option, service=service)
driver.get('https://www.bilibili.com/')
driver.maximize_window()
# a = driver.find_element(by=By.LINK_TEXT, value='番剧')
# a.click()
a = driver.find_element(by=By.CLASS_NAME, value='nav-search-input')
a.send_keys('河野华')
a_1 = driver.find_element(by=By.CLASS_NAME, value='nav-search-btn')
a_1.click()

windows = driver.window_handles
driver.switch_to.window(windows[-1])


a_2 = driver.find_element(by=By.CLASS_NAME, value='bili-avatar')
a_2.click()
driver.switch_to.window(windows[0])
sleep(5)
driver.quit()


# sleep(10)
'''加载用json保存的cookies'''
# with open('Bibilicookies.txt', 'r') as f:
#     cookie_list = json.load(f)
#     for cookie in cookie_list:
#         driver.add_cookie(cookie)
# driver.refresh()

'''获取并保存cookies'''
# driver.implicitly_wait(10)
# cookie = driver.get_cookies()
# print(cookie)
# with open('Bibilicookies.txt', 'w') as f:
#     f.write(json.dumps(cookie))
#     f.close()
# driver.quit()
