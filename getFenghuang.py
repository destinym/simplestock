# -*- coding: utf-8 -*- 
import sys
from getUrl import getUrl
import simplejson as json
from bs4 import BeautifulSoup 
import time
newscount = 30
ret = getUrl("http://finance.ifeng.com/stock/");
#retjson = json.JSONDecoder().decode(ret)
#num = len(retjson["data"])
#print num
#i = 1
    #content = getUrl("http://toutiao.com/"+element["source_url"])
    
    #print content
    #soup = BeautifulSoup(content, "html.parser")
soup = BeautifulSoup(ret)
print soup.title;
print soup.find_all("a");
   #print soup.get_text()
