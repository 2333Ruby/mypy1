# li = [i for i in range(1, 10)]
# index = li.index(3)
# print(li)
# print(li[index])









''' 正则表达式 '''
import re

text = '12345678@qq.com........xynuedu@xynu.edu.cn'
em = re.findall('\\d{6,10}@qq\\.com|\\w{6,12}@xynu\\.edu\\.cn', text)
print(em)


pw = '1234@Qqw.123'
if re.findall('[^\w|@|$|.|,]+', pw):
    print('密码不合法')
else:
    print('密码合法')
print(re.findall('[^\w|@|$|.|,]+', pw))


pw1 = '1234qw@@'
if re.findall('(\\d)+([a-zA-Z])+([@#!$%^&*(){}])+', pw1):
    print('强')
elif re.findall('(\\d|[a-zA-Z])+(\\d|[@#!$%^&*(){}])+([a-zA-Z]|[@#!$%^&*(){}])+', pw1):
    print('中')
elif re.findall('\\d+|[a-zA-Z]+|[@#!$%^&*(){}]+', pw1):
    print('弱')


mc = '00-01-0A-E4-12-12'
p = re.match('(([0-9a-fA-F]{2}-){5}[0-9a-fA-F]{2})', mc)
print(p.group())


def caesar_cipher(text, shift):
    def shift_letter(match):
        letter = match.group(0)
        start = ord('a') if letter.islower() else ord('A')
        # 计算偏移后的字母位置，并处理循环
        return chr((ord(letter) - start + shift) % 26 + start)

    # 使用正则表达式匹配所有字母字符，并替换它们
    encrypted_text = re.sub(r'[a-zA-Z]', shift_letter, text)
    return encrypted_text


# 使用示例
original_text = 'abcdefghijk'
shift = 3
encrypted = caesar_cipher(original_text, shift)
print('原 码 ：', original_text)
print("解码后：", encrypted)
