from selenium import webdriver
from selenium.webdriver.chrome.options import Options
url = "https://www.qidian.com/chapter/1031940621/705235484/"
chrome_options = Options()
chrome_options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options = chrome_options)
driver.get(url)
content = driver.page_source
driver.quit()