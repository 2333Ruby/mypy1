from bs4 import BeautifulSoup
import requests
headers = {
    "user-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
for i in range(1,6):
    url = f'https://www.qidian.com/all/page{i}/'
    data = requests.get(url,headers= headers)
    soup = BeautifulSoup(data.text,'html.parser')
    titles = soup.findAll('div',attrs={'class':'book-mid-info'})
    for title in titles:
        data = {
            '简介':title.get_text()
        }
        print(data)

# findAll和select方法返回的都是一个列表类型的数据