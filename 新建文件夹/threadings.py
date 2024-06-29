# from pythreading.threading import Thread
# import requests
from time import sleep
from queue import Queue
import threading

# headers = {
# 'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
# }


def work():
    #定义方法后以后要两个tab
    while not url_queue.empty():
        url = url_queue.get()
        sleep(3)
        print(url, end='\n')


if __name__ == '__main__':
    #定义主函数
    url_queue=Queue()
    #Queue后必要带（），不然不算是Queue类
    for i in range(1,15):
        url = f'https://www.bqgsa.cc/book/673/{i}.html'
        url_queue.put(url)

    for i in range(3):
        t1 = threading.Thread(target=work) #此时的方法后不能有（）
        t1.start()
        '''文件名和变量名或者是函数名不要与特殊名字重复（如函数、方法），否则会框框报错'''
        '''queue，threading都是内置函数'''
