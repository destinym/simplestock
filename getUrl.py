import urllib2
import urllib
from getEncoding import get_encoding
from getEncoding import decode_html

def getUrl2(site):
     response = urllib2.urlopen(site)
     html=response.read()
     return html

def getUrl(site):
    #hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    #   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    #   'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    #   'Accept-Encoding': 'none',
    #   'Accept-Language': 'en-US,en;q=0.8',
    #   'Connection': 'keep-alive'}
    hdr = {'User-Agent':'gzip','Accept-Encoding':'gzip','Connection':'keep-alive'}
    req = urllib2.Request(site, headers=hdr)
    #req = urllib2.Request(site)
    print site;
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()

    html = page.read()  
    #charset=BeautifulSoup.CHARSET_RE.search(response.headers['content-type']) 
    #charset=charset and charset.group(3) or None 
    #page=BeautifulSoup(response.read(),fromEncoding=charset)
    #print html;
    #coder = get_encoding(html)
    return decode_html(html) 


def postUrl(site, postDict):
    postData = urllib.urlencode(postDict)
    req = urllib2.Request(site, postData)
    req.add_header('Content-Type', "application/x-www-form-urlencoded")
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()

    html = page.read()  
    #charset=BeautifulSoup.CHARSET_RE.search(response.headers['content-type']) 
    #charset=charset and charset.group(3) or None 
    #page=BeautifulSoup(response.read(),fromEncoding=charset)
    coder = get_encoding(html)
    return decode_html(html) 
