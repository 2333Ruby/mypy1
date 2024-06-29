from openpyxl import Workbook
a=['1','2','3']
b=['4','5','6']
c=[]
c.append(a)
c.append(b)
# for i in range(10):
#     a.append(i)
#     b.append(i)
# c=list(zip(a,b))
print(c)
wb=Workbook()
ws=wb['Sheet']
ws.append(['第一列','第二列'])
for i in range(len(c[0])):
    d=c[0][i],c[1][i]
    ws.append(d)
wb.save(r'text.xlsx')#只有Workbook（）对象才能保存
