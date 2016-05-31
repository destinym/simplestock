# -*- coding: utf-8 -*- 
import sys
from getUrl import getUrl
import simplejson as json
from bs4 import BeautifulSoup 
import time
import MySQLdb as mdb
import dbconfig
reload(sys)
sys.setdefaultencoding( "utf-8" ) 

conn = dbconfig.connectDB()
cur = conn.cursor()
cur.execute("SET NAMES utf8")
cur.execute("SET CHARACTER_SET_CLIENT=utf8")
cur.execute("SET CHARACTER_SET_RESULTS=utf8")

curDay = time.strftime('%Y-%m-%d',time.localtime(time.time()))
curDay += " 16:00:00"
timeArray = time.strptime(curDay, "%Y-%m-%d %H:%M:%S")
curTime = int(time.mktime(timeArray))
curTimestamp = str(curTime)

#CAST(field as DECIMAL(10,5))
sql = "select * from stockDaliy  where pb > 0 and per_d> 0 and pb_mul_pe < 40 order by per_d asc limit 200"


print sql
cur.execute(sql)
result = cur.fetchall()
print result
#conn.commit()
    
#ret1 = getUrl("http://hq.sinajs.cn/?func=getData._hq_cron();&list=%s"%(stockIdStr))

