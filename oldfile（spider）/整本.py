import requests
import re
import os

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
for i in range(1,10):
    url=f'https://m.biqugen.net/book/59265/index_{i}.html'
    # print(url)
    response= requests.get(url=url, headers=headers)
    # print(response.text)
    mulu = re.findall('<a href="(.*?)">',response.text)
    print(mulu)
    # index_url = 'https://m.biqugen.net/book/59265/'+

    # < li class ="even" > < a href="58469080.html" > 第四百章 全部灭杀 < /a > < /li >