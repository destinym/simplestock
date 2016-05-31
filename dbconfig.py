
"""
    dbconfig  module 1.0
    author:mengliang1225@aliyun.com
    date:2013-11-21
"""

import MySQLdb as mdb
import socket

def readConf():
    hostname = socket.gethostname();
    if hostname.find('xad') != -1:
        file = open("db_dev.conf")
    else:
        file = open("db_net.conf")
    ret = {}
    for line in file:
        str = line.split('=') 
        ret[str[0].strip()] = str[1].strip(); 
    return ret;
        

def connectDB():
    ret = readConf()
    try:
        conn = mdb.connect(host=ret['server'], 
                           user=ret['user'], 
                           passwd=ret['password'],
                           db=ret['db'],
                           charset='utf8')
        print "connet success"
        return conn
    except mdb.Error, e:
        print "Mysql Error, %s,%s"%(e.args[0],e.args[1])
