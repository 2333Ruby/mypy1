import regex
text = '18336121479=zhaohongda=wwwwwwww=shishabi'
result = regex.findall(r'ww{,2}', text)
# result = regex.search(r'zhao(hong)?da',text)
print(result)
# text = text.split('=')
# for i in range(0,3):
#     print( text.split('=')[i])
# print(text.split('='))
