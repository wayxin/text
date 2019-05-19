
import  xlrd
def shuju():
    shuj=[]
    f=xlrd.open_workbook(r'H:\PycharmProjects\untitled\jiekou_kuangjia\data\b.xls')
    sheet=f.sheets()[0]
    for i in range(sheet.nrows):
        shuj.append(sheet.row_values(i))
    # print(shuj)
    return shuj
shuju()