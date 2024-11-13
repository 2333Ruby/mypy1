import requests
from bs4 import BeautifulSoup
headers = {
"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
response = requests.get("https://www.qidian.com/all/", headers=headers)
html = response.text
soup = BeautifulSoup(html,"html.parser")
title = soup.select('#book-img-text > ul > li:nth-child(1) > div.book-mid-info > h2 > a')
titles =title.string
print(titles)

