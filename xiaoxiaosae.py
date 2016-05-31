#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# File http_post.py
import urllib
import urllib2
import json
import time
    
def http_set_ref():
  url = 'http://m.zuikuapp.com/show/like/set'
  request = urllib2.Request(url)
  jdata = "itemLikeId=941"
  headers = { 'Referer' : "http://m.zuikuapp.com/a/68245_159355?from=singlemessage&isappinstalled=0" }        
  req = urllib2.Request(url, jdata, headers)
  i = 1; 
  while i<1998:  
    response = urllib2.urlopen(req)
    i = i + 1
 
  print "====update ok==== " 
  print  http_get_ref(uid)
  print "====update end==== " 
 
#941
def http_get_ref(uid):
  url = 'http://m.zuikuapp.com/show/like/get'
  request = urllib2.Request(url)
  jdata = "itemLikeId=%d"%(uid)
  headers = { 'Referer' : "http://m.zuikuapp.com/a/68245_159355?from=singlemessage&isappinstalled=0" }        
  req = urllib2.Request(url, jdata, headers)
  response = urllib2.urlopen(req)
  ret = response.read()
  retjson = json.JSONDecoder().decode(ret)
  return int(retjson["count"])

  #print response.read()
while 1:
    uid = 930
    maxNum = http_get_ref(941) 
    maxId = 941 
    while(uid < 1300):
        curNum = http_get_ref(uid)
        if (curNum > maxNum -1000 and uid != 941):
           print "====beyond==="
           print curNum  
           print uid
           maxId = uid
           http_set_ref()
        uid += 1
    #print "=====maxbegin"
    #print maxNum 
    #print maxId 
    #print "=====maxEnd"

    time.sleep(10)
#resp = http_get()
#print resp
