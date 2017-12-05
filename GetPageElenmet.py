# import xlrd
# import xlwt
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
driver = webdriver.Firefox()
driver.get('')
def t (int):
    time.sleep(int)
def Refresh ():
    driver.refresh()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='firstname']").send_keys('123456@163.com') # u只是为了传入正确的中文。
driver.find_element_by_xpath(".//*[@id='secondname']").send_keys('123456')
# driver.find_element_by_xpath("html/body/div[2]/form/div/div[4]/label/input").click()
driver.find_element_by_xpath("html/body/div[2]/form/div/button").click()
t(3)
# 客服模式下的数据显示
# 获取页面第一行标签
'''
lineTag = driver.find_elements_by_class_name("top-box-title")
lineTag1 = driver.find_elements_by_class_name("top-box-data ng-binding")
lineTag2 = driver.find_elements_by_class_name("top-box-second")
lineTag3 = driver.find_elements_by_class_name("top-box-second-spn ng-binding")
i = []
for i in lineTag:
    if i.get_attribute("class") == "top-box-title":
        print(i.text)
        time.sleep(5)
'''

def First_value():
    #listClassO = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[1]/div/div[1]/p[1]").text
    listClassO2 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[1]/div/div[1]/p[2]").text
    #listClassT = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[2]/div/div[1]/p[1]").text
    listClassT2 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[2]/div/div[1]/p[2]").text
    #listClassS = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[3]/div/div[1]/p[1]").text
    listClassS2 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[3]/div/div[1]/p[2]").text
    #listClassF = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[4]/div/div[1]/p[1]").text
    listClassF2 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[4]/div/div[1]/p[2]").text
    #listClassC = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[5]/div/div[1]/p[1]").text
    listClassC2 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[5]/div/div[1]/p[2]").text
    #listFirst = [listClassO, listClassT, listClassS, listClassF, listClassC]
    listFirst2 = [listClassO2, listClassT2, listClassS2, listClassF2, listClassC2]
    #return listFirst
    return listFirst2
def Second_value():
    List1 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[1]/div/div[2]/p").text
    List11 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[1]/div/div[2]/p/span").text
    List2 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[2]/div/div[2]/p").text
    List22 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[2]/div/div[2]/p/span").text
    List3 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[3]/div/div[2]/p").text
    List33 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[3]/div/div[2]/p/span").text
    List4 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[4]/div/div[2]/p").text
    List44 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[4]/div/div[2]/p/span").text
    List5 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[5]/div/div[2]/p").text
    List55 = driver.find_element_by_xpath(".//*[@id='uiView']/div/div/div[1]/div[2]/div[5]/div/div[2]/p/span").text
    listSecond = [List1, List2, List3, List4, List5]
    listSecond2 = [List11, List22, List33, List44, List55]
    return listSecond2

#print(First_value())
#Second_value()
t(3)

First_value()

def PageSwithc():
    driver.find_element_by_xpath('html/body/div[1]/div/div/span/a').click()
    driver.find_element_by_xpath('html/body/div[1]/div/div/ul/a[2]').click()
# 会话
def Page1():
    # 挂起 在线
    driver.find_element_by_class_name('status').click()
    time.sleep(1)
    driver.find_element_by_id('dialog').click()
# 首页
def  Page2():
    driver.find_element_by_id('reportForm').click()
    time.sleep(1)
    # driver.refresh()


def xunhuan():
    time.sleep(1)
    PageSwithc()
    time.sleep(1)
    Page1()
    time.sleep(1)
    Page2()
    time.sleep(1)
    Page1()







#print(listFirst)
#print(listFirst2)
#list = [listFirst]

#print(list)

#driver.close()
#driver.quit()


'''
def write_Excel():
        wb = xlwt.Workbook(encoding='utf-8',style_compression=0) #创建文件
        Sheet = wb.add_sheet("zhangzhen") #改变sheet为zhangzhen
        Sheet.write(0, 0, "csid 客服id")
        Sheet.write(0, 1, "consulting_user 正在咨询用户数")
        Sheet.write(0, 2, "online_waiter 在线客服人数")
        Sheet.write(0, 3, "waiting 正在排队人数")
        Sheet.write(0, 4, "end_waiting 结束排队人数")
        Sheet.write(0, 5, "waiting_length waiting_length")
        Sheet.write(0, 6, "session 会话数量")
        Sheet.write(0, 7, "session_length 会话时长")
        wb.save("e:\zhangzhen.xls")  #保存文件
'''
'''
def write_Excel():
    MyBook = xlwt.Workbook(encoding='utf-8',style_compression=0)
    Sheet = MyBook.add_sheet("今日在线服务器数据趋势")
    list = ["正在咨询人数","正在排队人数","今日会话量","今日未接入会话量","今日满意度"]
    MyBook.save("f:\zhangzhen.xls")

write_Excel()

def read_Excel():
    wb2 =xlrd.open_workbook(r"e:\\originaldata.xlsx")
    Sheet1 = wb2.sheet_by_index(0) #第一个表(第一种)
    #Sheet2 = wb2.sheet_by_name(u'Sheet2') 第二种方法
    SheetName = wb2.sheet_names() #查看包含的工作表
    #print(Sheet2)
    #print(Sheet1)
    #print(SheetName[0])
    nrows = Sheet1.nrows #获取行数
    ncols = Sheet1.ncols #获取列数
    cell_value = Sheet1.cell_value(0,0)
    cell_value2 = Sheet1._cell_values
    print('nrows %d, ncols %d' % (nrows, ncols))
    #print(cell_value)
    #print(cell_value2)
    #print(len(cell_value2))
    for i in cell_value2:
       print(i)
'''



