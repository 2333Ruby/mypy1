import requests
import re
import os

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
url = 'https://m.biqugen.net/book/59265/18238874.html'
index_url='https://m.biqugen.net/book/59265/'
response=requests.get(url=url, headers=headers)
title = re.findall('<h1 class="nr_title" id="nr_title">(.*?)</h1>',response.text)[0]
content = re.findall('<div id="nr1">(.*?)</div>',response.text,re.S)[0].replace(' &nbsp;&nbsp;&nbsp;&nbsp;','\n').replace('<br /><br />',' ')
# all_url=re.findall('<link rel="canonical" href="(.*?)"/><meta name="applicable-device"')

# print(title)
print(content)
# print(response.text)
# <h1 class="nr_title" id="nr_title">引子：皓月当空</h1>
# with open(title+'.txt',mode='a',encoding='utf-8')as f:
#     f.write(title)
#     f.write('\n')
#     f.write(content)
#     f.write('\n')


    # class ="info" > < h1 > 神印王座II皓月当空 < /h1 > < p > 作者： < a href="/modules/article/search.php?searchtype=author&amp;searchkey=%CC%C6%BC%D2%C8%FD%C9%D9" > 唐家三少 < /a > < /p > < p > 类别： < a href="/list/3_1.html" > 都市小说 < /a > < /p > < p > 状态：连载中 < /p > < p > 更新：2024-02-07 09:35: 45 <
    #
    # / p > < p > 最新： < a
    # href = "58476449.html" > 第四百零八章
    # 灵魂之石的奥秘 < / a > < / p > < / td >