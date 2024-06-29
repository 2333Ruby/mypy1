import jieba

jieba.setLogLevel(jieba.logging.INFO)

txt = open("检索.txt", "r", encoding='utf-8', errors='ignore').read()
words = jieba.lcut(txt)     # 使用精确模式对文本进行分词
counts = {}  # 通过键值对的形式存储词语及其出现的次数

for word in words:
    if len(word) == 1:  # 单个词语不计算在内
        continue
    else:
        counts[word] = counts.get(word, 0) + 1  # 遍历所有词语，每出现一次其对应的值加 1

items = list(counts.items())  # 将键值对转换成列表
items.sort(key=lambda x: x[1], reverse=True)  # 根据词语出现的次数进行从大到小排序

for i in range(100):
    word, count = items[i]
    print("{0:<10}{1:>10}".format(word, count))

