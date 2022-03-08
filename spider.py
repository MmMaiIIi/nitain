
# -*- codeing = utf-8 -*-
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式，进行文字匹配`
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行excel操作

# findLink = re.compile(r'<a href="(.*?)">')  # 创建正则表达式对象，标售规则   影片详情链接的规则
# findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
#findJudge = re.compile(r'<span>(\d*)人评价</span>')
#findInq = re.compile(r'<span class="inq">(.*)</span>')
#findBd = re.compile(r'<p class="">(.*?)</p>', re.S)


findCountry = r'"country":"(.*?)"'
findper = r'"per_hundred":(.*?)}'

def main():
    baseurl = "https://news.ifeng.com/c/special/85mhVvWS5i4"  #要爬取的网页链接
    # 1.爬取网页
    html=askURL(baseurl)
    print(html)
    
    matches = re.finditer(findCountry, html, re.MULTILINE)
    countryList=[]
    for matchNum, match in enumerate(matches, start=1):
        for groupNum in range(0, len(match.groups())):
            groupNum = groupNum + 1
            countryList.append(match.group(1))
            #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(1)))
    print(countryList)
    
    matches = re.finditer(findper, html, re.MULTILINE)
    perlist=[]
    for matchNum, match in enumerate(matches, start=1):
            #print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
            for groupNum in range(0, len(match.groups())):
                groupNum = groupNum + 1
                perlist.append(match.group(1))
            #print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))Num, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))
    print(perlist)
    
    datalist=[]
    for n in range(0,210):
            datalist.append(countryList[n])
            datalist.append(perlist[n])
        
    print(datalist)

    savepath = "世界各国每百人接种剂数.xls"    #当前目录新建XLS，存储进去
    saveData(datalist,savepath)      #2种存储方式可以只选择一种
    


# 保存数据到表格
def saveData(datalist,savepath):
    print("save.......")
    book = xlwt.Workbook(encoding="utf-8",style_compression=0) #创建workbook对象
    sheet = book.add_sheet('世界各国每百人接种剂数', cell_overwrite_ok=True) #创建工作表
    col = ("国家","每百人接种剂数")
    for i in range(0,2):
        sheet.write(0,i,col[i])  #列名
    for i in range(0,139):
        sheet.write(i+1,0,datalist[2*i])
        sheet.write(i+1,1,datalist[2*i+1])
        
    book.save(savepath) #保存



# 得到指定一个URL的网页内容
def askURL(url):
    head = {  # 模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0; Win64; x64) AppleWebKit / 537.36(KHTML, like Gecko) Chrome / 80.0.3987.122  Safari / 537.36"
    }
    # 用户代理，表示告诉豆瓣服务器，我们是什么类型的机器、浏览器（本质上是告诉浏览器，我们可以接收什么水平的文件内容）

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html





if __name__ == "__main__":  # 当程序执行时
    # 调用函数
     main()
    # init_db("movietest.db")
     print("爬取完毕！")

