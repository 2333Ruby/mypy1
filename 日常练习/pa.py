import requests
import re
import os

urls=[]
file='神印王座II\\'
if not os.path.exists(file):
    os.mkdir(file)
headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
for i in range(1,9):
    url = f'https://www.biqugen.net/book/59265/index_{i}.html'
    response = requests.get(url=url,headers=headers).text
    cap=re.findall('<dd><a href="(.*?)">',response)
    for a in range(1,len(cap)):
        urls_c='https://www.biqugen.net/book/59265/'+cap[a]
        urls.append(urls_c)
for b in range(1,len(urls)):
    url_new=urls[b]
    response_new=requests.get(url=url_new,headers=headers)
    title=re.findall('<meta name="keywords" content=(.*?) />',response_new.text)[0]
    content=re.findall('&nbsp;&nbsp;&nbsp;&nbsp;(.*?)<br />',response_new.text)
    content_ture='\n'.join(content)
    # with open(file + title+'.txt',mode='a',encoding='utf_8') as f:
    with open(r'D:/1Pycharm，启动！\pythonProject1\file.txt',mode='a',encoding='utf_8') as f:
        # f.write(title)
        # f.write('\n')
        f.write(content_ture)
        f.write('\n')
    print(f'第{b}章下载完成！')
