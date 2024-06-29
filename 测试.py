import requests
import re
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
url='https://www.biqugen.net/book/59265/57967084.html'
response = requests.get(url=url,headers=headers).text
title=re.findall('<meta name="keywords" content=(.*?) />',response)[0]
# content=re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',response)
print(title)
# print(content)