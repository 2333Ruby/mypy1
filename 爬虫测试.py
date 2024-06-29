# import requests
# import json
#
# url = 'https://fanqienovel.com/'
# headers = {
#     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
# }
# res = requests.get(url=url, headers=headers)
# print(res.text)
# res.encoding = 'utf-8'
# print(res.json())
# print(res.status_code)

import requests
import csv
from time import sleep
import random


def main(page):
    url = f'https://weibo.com/ajax/statuses/mymblog?uid=2803301701&page={page}&feature=0&since_id=4824543023860882kp{page}'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'cookie': 'SINAGLOBAL=6330339198688.262.1661412257300; ULV=1661412257303:1:1:1:6330339198688.262.1661412257300:; PC_TOKEN=8b935a3a6e; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWoQDW1G.Vsux_WIbm9NsCq5JpX5KMhUgL.FoMNShMN1K5ESKq2dJLoIpjLxKnL1h.LB.-LxKqLBoBLB.-LxKqLBKeLB--t; ALF=1697345086; SSOLoginState=1665809086; SCF=Auy-TaGDNaCT06C4RU3M3kQ0-QgmTXuo9D79pM7HVAjce1K3W92R1-fHAP3gXR6orrHK_FSwDsodoGTj7nX_1Hw.; SUB=_2A25OTkruDeRhGeFJ71UW-S7OzjqIHXVtOjsmrDV8PUNbmtANLVKmkW9Nf9yGtaKedmyOsDKGh84ivtfHMGwvRNtZ; XSRF-TOKEN=LK4bhZJ7sEohF6dtSwhZnTS4; WBPSESS=PfYjpkhjwcpEXrS7xtxJwmpyQoHWuGAMhQkKHvr_seQNjwPPx0HJgSgqWTZiNRgDxypgeqzSMsbVyaDvo7ng6uTdC9Brt07zYoh6wXXhQjMtzAXot-tZzLRlW_69Am82CXWOFfcvM4AzsWlAI-6ZNA=='
    }
    resp = requests.get(url, headers=headers)
    data_list = resp.json()['data']['list']

    for item in data_list:
        created_time = item['created_at']  # 发布时间
        author = item['user']['screen_name']  # 作者
        title = item['text_raw']  # 帖子标题
        reposts_count = item['reposts_count']  # 转发数
        comments_count = item['comments_count']  # 评论数
        attitudes_count = item['attitudes_count']  # 点赞数
        csvwriter.writerow((created_time, author, title, reposts_count, comments_count, attitudes_count))
        print(created_time, author, title, reposts_count, comments_count, attitudes_count)
    print(f'第{page}页爬取完毕')


if __name__ == '__main__':
    # 创建保存数据的csv文件
    with open('06-2.csv', 'a', encoding='utf-8', newline='') as f:
        csvwriter = csv.writer(f)
        # 添加文件表头
        csvwriter.writerow(('发布时间', '发布作者', '帖子标题', '转发数', '评论数', '点赞数'))
        for page in range(1, 6):  # 爬取前5页数据
            main(page)
            sleep(5 + random.random())