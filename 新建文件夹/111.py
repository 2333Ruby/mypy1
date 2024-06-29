from datetime import datetime
from random import choices

dt = datetime.now()
print(dt)
tt = datetime(2024, 4, 20, 15,  59, 00, 000000)
# print(dt.date())
# print(dt.time())
# ddt = datetime.now()
#
while dt < tt:
    dt = datetime.now()
    print(dt)
print('结束')

# d = choices([1, 2, 3, 4, 5], k=2)
# print(d)
