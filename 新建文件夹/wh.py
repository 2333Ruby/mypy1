import requests
import re


headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

url ='https://sou.zhaopin.com/?jl=530&kw=%E7%89%A9%E6%B5%81&p=1'
content=requests.get(url=url,headers=headers).text
url_1=re.findall('positionURL":"(.*?)",',content)
print(url_1)