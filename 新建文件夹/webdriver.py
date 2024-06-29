from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.keys import Keys
import time
option=webdriver.EdgeOptions()
option.add_experimental_option('detach',True)
service=Service('D:/32670/1python3.8\msedgedriver.exe')
driver=webdriver.Edge(options=option,service=service)
driver.get('https://www.bilibili.com/')
elem=driver.find_element('class name','nav-search-input')
elem.send_keys('村花770')
# <div class="nav-search-content">'
elem_button=driver.find_element('class name','nav-search-btn')
elem_button.click()
'''切换到新打开的窗口'''
windows=driver.window_handles
driver.switch_to.window(windows[-1])
zio=driver.find_element('class name','bili-avatar')
zio.click()
time.sleep(5)
driver.switch_to.window(windows[-1])

# zio.send_keys(Keys.SPACE)
# # pip --default-timeout=100 install selenium==4.1.1 http://pypi.tuna.tsinghua.edu.cn/simple
'''pip install -i http://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.douban.com tensorflow==2.0.0'''
'''<button data-v-1cd59021 class="vui_button vui_button--blue"> + 关注 </button>'''
'''<div class="bili-avatar" style="width: 86px;height:86px;transform: translate(0px, 0px);"><div class="user-actions d_inline_block" data-v-1cd59021>'''
'''//*[@id="search-wrap"]/div[2]/button'''