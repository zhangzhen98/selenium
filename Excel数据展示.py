
from xlutils.copy import copy
from CIM自动化package import GetPageElenmet
import xlrd
import time
list = GetPageElenmet.First_value()
list2 = GetPageElenmet.Second_value()
rb = xlrd.open_workbook("f:\\zhangzhen.xls")
# MyBook1 = xlwt.Workbook(encoding='utf-8',style_compression=0)
wb = copy(rb)
# Sheet = wb.get_sheet(0)
'''
def value():
    Sheet.write(0, 0,"正在咨询人数")
    Sheet.write(1,0,list[0])
    Sheet.write(0, 1,"正在排队人数")
    Sheet.write(1,1,list[1])
    Sheet.write(0, 2,"今日会话量")
    Sheet.write(1,2,list[2])
    Sheet.write(0, 3,"今日未接入会话量")
    Sheet.write(1,3,list[3])
    Sheet.write(0, 4,"今日相对满意度")
    Sheet.write(1,4,list[4])
    MyBook.save("f:\zhangzhen.xls")
def form():
    Sheet.write(2,0,"排队量")
    Sheet.write(3,0,list[1])
    Sheet.write(2,1,"已接入会话量")
    Sheet.write(3,1,list[0])
    Sheet.write(2,2,"未接入会话量")
    Sheet.write(3,2,list[3]+list[2])
    Sheet.write(2,3,"总会话量")
    Sheet.write(3,3,)
    now = time.strftime("%H%M%S")
    Sheet.write(0,4,now)
    MyBook.save("f:\zhangzhen.xls")
value()
form()
'''
Sheet = wb.get_sheet("Sheet1")
'''
nrows =Sheet.nrows #行
ncols =Sheet.ncols #列
print(ncols)
print(nrows)
'''
print(list)
print(list2)
sh = rb.sheet_by_name("Sheet1")
ncols = sh.ncols  # 获取列数
print(ncols)
tag = ["正在咨询人数", "正在排队人数", "今日会话量", "今日未接入会话量", "今日相对满意度"]
tag2 = ["当前在线客服数", "今日平均排队时长", "今日平均会话时长", "接入率", "参评率"]
'''
def shijian():
    now = time.strftime("%H%M%S")
    M = time.strftime("%M")
    if M == 00:
        Sheet.write(0,7,"时间")
        Sheet.write(1,7,now)
'''
def sleeptime(hours, min, sec):
    return hours*3600+min*60+sec

def write_xls(now, ncol, ncol2):
    #第一栏数据
    for i in range(0, len(list)):
        Sheet.write(now, i, list[i])
    #第一栏标签
    for Tag in range(0, len(tag)):
        Sheet.write(1, Tag, tag[Tag])

    #第二栏标签
    for Tag2 in range(0, len(tag2)):
        Sheet.write(0, ncol, tag2[Tag2])
        ncol += 1

    #第二栏数据
    for value in range(0,len(list2)):
        Sheet.write(now,ncol2,list2[value])
        ncol2+=1
        wb.save("f:\zhangzhen.xls")

ncol = ncols+1
ncol2 = ncols+1
now=2
min = sleeptime(0,0,30)
while True:
    GetPageElenmet.PageSwithc()
    time.sleep(1)
    GetPageElenmet.Page1()
    write_xls(now,ncol,ncol2)
    now += 1
    time.sleep(min)
    # 首页
    GetPageElenmet.Page2()
    time.sleep(1)
    list = GetPageElenmet.First_value()
    list2 = GetPageElenmet.Second_value()
    time.sleep(1)
    #会话
    GetPageElenmet.Page1()



    #if(now>1000):
        #break







