import requests
import re
import os

headers = {
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
file='离婚后她惊艳了世界\\'
if not os.path.exists(file):
    os.mkdir(file)
for i in range(10,21):
    url=f'https://www.qimao.com/shuku/222767-164809174000{i}/'
    response=requests.get(url=url,headers=headers)
    title=re.findall('<h2 class="chapter-title" data-v-e0864cb2>(.*?)</h2>',response.text)[0]
    content=re.findall('\u003Cp\u003E(.*?)\u003C\u002Fp',response.text)
    content='\n'.join(content)
    with open(file + title+'.txt',mode='a',encoding='utf-8') as f:
        f.write(title)
        f.write('\n')
        f.write(content)
        f.write('\n')
    print(f'第{i}章下载成功！')






# <a data-v-a83ae066="" href="/shuku/222767-16480917400001/" target="book_222767"><!----> <span data-v-a83ae066="" class="txt">
#                     第1章  阿尧是谁
#                 </span></a>
#https://www.qimao.com/shuku/222767-16480917400001/
# <h2 class="chapter-title" data-v-e0864cb2="">第1章  阿尧是谁</h2>