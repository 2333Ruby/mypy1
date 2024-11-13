import tkinter as tk
import requests
import re
import webbrowser


# 创建一个窗口
root = tk.Tk()
#窗口大小＋距左上角的距离（长＋宽）
root.geometry('1000x510+300+300')
# 窗口标题
root.title('幽默')
url_1 = 'http://jiexi44.qmbo.cn/jiexi/?url='
url_2 = 'http://jiexi42.qmbo.cn/jiexi/?url='
url_3 = 'http://jiexi41.qmbo.cn/jiexi/?url='
def show():
    num_1=num.get()
    # 获取输入的内容
    word=input_va.get()
    if num_1 == 1:
        # print('接口1')
        # print('输入为：')
        link=url_1+word
        html_data = requests.get(url=link).text
        video_url = re.findall('<iframe id="baiyug" scrolling="no" scr="(.*?)"',html_data)[0]
        webbrowser.open(video_url)
    elif num_1 == 2:
        # print('接口2')
        link=url_2+word
        html_data = requests.get(url=link).text
        video_url = re.findall('<iframe id="baiyug" scrolling="no" scr="(.*?)"', html_data)[0]
        webbrowser.open(video_url)

    elif num_1 == 3:
        # print('接口3')
        link=url_3+word
        html_data = requests.get(url=link).text
        video_url = re.findall('<iframe id="baiyug" scrolling="no" scr="(.*?)"', html_data)[0]
        webbrowser.open(video_url)



# 设置图片
img=tk.PhotoImage(file='img//3.png')
# 布局图片（默认在最中间）
tk.Label(root, image=img).pack()
# 设置标签框
choose=tk.LabelFrame(root)
choose.pack(fill='both')  #pad距离pady表示设置Y轴距离，padx表示设置X轴距离,fill填充，用来去掉边边角角的框
tk.Label(choose,text='又来看剧了？牢底',font=('楷体',20)).pack(side=tk.LEFT)
# 设置可变变量
num=tk.IntVar()
# 设置默认选择（value的值）
num.set(1)
# 设置选择
tk.Radiobutton(choose,text='默认路线',font=('宋体',15),variable=num,value=1).pack(side=tk.LEFT)
tk.Radiobutton(choose,text='电视剧专线',font=('宋体',15),variable=num,value=2).pack(side=tk.LEFT)
tk.Radiobutton(choose,text='腾讯优酷',font=('宋体',15),variable=num,value=3).pack(side=tk.LEFT)
# 输入标签框
input_L =tk.LabelFrame(root)
input_L.pack(fill='both')
# 设置可变变量
input_va=tk.StringVar()

tk.Label(input_L,text='上链接吧！：',font=('楷体',20)).pack(side=tk.LEFT)
tk.Entry(input_L,width=200,relief='flat',textvariable=input_va).pack(side=tk.LEFT,fill='both')
# 设置解析的按钮
tk.Button(root,text='点击出发啦！牢底',font=('楷体',18),relief='flat',bg='#449d44',command=show).pack(fill='both')
# 让窗口持续在屏幕上
root.mainloop()
# <video class="dplayer-video dplayer-video-current" webkit-playsinline="" playsinline="" poster="//cdn.mazc.org/packs/yparse/packs/player/images/loading.gif" preload="auto" src="blob:https://jx.xxza.top/6222010d-9bd8-4e25-b0e5-9e299ade247d">
#
# </video>
# https://v.qq.com/x/cover/mzc00200dwdigel/r00461kkgv7.html
#  https://v6.shanshanku.com/202309/06/cfApaxwgVc1/video/original/hls/player0010.ts
# <video class="dplayer-video dplayer-video-current" webkit-playsinline="" playsinline="" poster="//cdn.mazc.org/packs/yparse/packs/player/images/loading.gif" preload="auto" src="blob:https://jx.xxza.top/f736b06b-5c4e-4333-bb61-12896b2c4fb4">
#
# </video>