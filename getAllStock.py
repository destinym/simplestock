# -*- coding: utf-8 -*- 
import sys
from getUrl import getUrl
from getUrl import getUrl2
import simplejson as json
from bs4 import BeautifulSoup 
import time
import MySQLdb as mdb
import dbconfig
reload(sys)
sys.setdefaultencoding( "utf-8" ) 
page = 1 
ret = getUrl2("http://money.finance.sina.com.cn/d/api/openapi_proxy.php/?__s=[[\"hq\",\"hs_a\",\"\",0,%d,40]]"%(page));
#print ret
retjson = json.JSONDecoder().decode(ret)
stockCount  = retjson[0]["count"]
print stockCount
pages = stockCount / 40 + 1 

conn = dbconfig.connectDB()
cur = conn.cursor()
cur.execute("SET NAMES utf8")
cur.execute("SET CHARACTER_SET_CLIENT=utf8")
cur.execute("SET CHARACTER_SET_RESULTS=utf8")


values = ""
curDay = time.strftime('%Y-%m-%d',time.localtime(time.time() ))
curDay += " 16:00:00"
timeArray = time.strptime(curDay, "%Y-%m-%d %H:%M:%S")
curTime = int(time.mktime(timeArray))
curTimestamp = str(curTime)
while page <= pages:
    ret = getUrl2("http://money.finance.sina.com.cn/d/api/openapi_proxy.php/?__s=[[\"hq\",\"hs_a\",\"\",0,%d,40]]"%(page));
    #print ret
    retjson = json.JSONDecoder().decode(ret)
    num = len(retjson[0]["items"])
    print num
    stockIdStr = ""
    for element in retjson[0]["items"]: 
        values +="("
        i = 0
        while i < 22 :
           values += "\'"+ str(element[i]) +"\',"
           i = i + 1
        pe = float(element[15])
        pe_d = float(element[16])
        pb = float(element[18])
        print element[2] 
        if pb <= 0 or  pe <=0  :
            gvi = str(0)
        else: 
            gvi = str( (1.0/ pb) * (1 + (pb/pe) )**5)

        if pb <= 0 or  pe_d <=0  :
            gvi_d = str(0)
        else: 
            gvi_d = str( (1.0/ pb) * (1 + (pb/pe_d) )**5)
        #print  str(float(element[16]) *(float(1 + element[18])**5))
        print gvi 
        print  "======"
        values += gvi 
        values += ","
        values += gvi_d
        values += ","
        values += "from_unixtime(%s)"%curTimestamp
        values += "),"
    page = page + 1

values = values[0: -1]
sql = "insert into stockDaliy(symbol,code,name,trade,pricechange,changepercent,buy,sell,settlement,open,high,low,volume,amount,ticktime,per,per_d,nta,pb,mktcap,nmc,turnoverratio,gvi,gvi_d,createTime) values %s"%(values);

#print sql
cur.execute(sql)
conn.commit()
    

