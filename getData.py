# -*- coding: utf-8 -*- 
import sys
from getUrl import getUrl
import simplejson as json
from bs4 import BeautifulSoup 
import time
newscount = 30
ret = getUrl("http://toutiao.com/api/article/recent/?source=2&count=%s&category=news_finance&max_behot_time=%s&utm_source=toutiao&offset=0"%(newscount,time.time));
retjson = json.JSONDecoder().decode(ret)
num = len(retjson["data"])
print num
i = 1
for element in retjson["data"]: 
    print element["title"]
    print element["source_url"]
    #content = getUrl("http://toutiao.com/"+element["source_url"])
    
    print element["article_url"]
    content = getUrl(element["article_url"])
    #print content
    #soup = BeautifulSoup(content, "html.parser")
    soup = BeautifulSoup(content)
    print soup.title;
    print soup.find_all("div", class_="article-content  pgc_top_banner");
    #print soup.get_text()
    print "----------***********-----"
    print "----------***********-----:%d"%(i)
    #print content
    i = i + 1
