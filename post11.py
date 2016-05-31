# -*- coding: utf-8 -*- 
import sys
from getUrl import getUrl
from getUrl import postUrl
import simplejson as json
from bs4 import BeautifulSoup 
import time
newscount = 30
postDict = {
    'txtUser'       : "冲脸小黑牛",
    'txtPassWord'      : "4853518",
    '__VIEWSTATE'      : "/wEPDwUJMzQ5MzcyODQwZGTQBI8d6P0FtfETW",
    '__EVENTVALIDATION'  :  "/wEWBALv+OPMCQLB2tiHDgK1qbSWCwL07qXZBifT2Pr1NYfmEW2lS0RG/PDgKKMA" ,
	'butLogin'      : '',   
};
ret = postUrl("http://register.5211game.com/reg/login.aspx", postDict);
#retjson = json.JSONDecoder().decode(ret)
print ret
