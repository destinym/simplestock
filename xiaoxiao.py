#!/usr/bin/env python
#  -*- coding:utf-8 -*-
# File http_post.py
import urllib
import urllib2
import json
import time
    
 
url = 'http://a.vpimg4.com/upload/merchandise/433130/PAI-6957229386917-5_320x320_80.jpg'
user_agent = 'User-agent:gzip'# 将user_agent写入头信息
values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(req)
the_page = response.read() 
print the_page
print response
