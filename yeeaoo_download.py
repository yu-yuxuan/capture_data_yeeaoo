#!/usr/bin/python3
# http://www.yeeaoo.com/

import requests
import bs4
import os, errno

def silentremove(filename):
    try:
        os.remove(filename)
    except OSError as e: # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT: # errno.ENOENT = no such file or directory
            raise # re-raise exception if a different error occured


def capture_web(weburl,file):
    response = requests.get(weburl)
    soup = bs4.BeautifulSoup(response.text)
    result=soup.select('div.tt a[href^=/test]')
    for res in result:
        infomation=str.join('___', (res.text, res.attrs.get('href')))
        # print(information)
        with open(file, "a") as myfile:
            myfile.write(infomation+ '\n')



# links = [a.attrs.get('href') for a in soup.select('div."onet" a[href^=/test]')]


# links = soup.select('div.onet a[href^=/video]')
# for node in soup.find('p'):
#     print ''.join(node.findAll(text=True))


if __name__ == "__main__":
    filename="Task1"
    silentremove(filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-155-2006.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-155-2007.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-155-2008.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-155-2009.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-155-2010.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-155-2011.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-155-2012.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-155-2013.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-155-2014.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-155-2015.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-155-2016.html"
    capture_web(htmlurl,filename)

    filename="Task2"
    silentremove(filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-158-2006.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-158-2007.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-158-2008.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-158-2009.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-158-2010.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-158-2011.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-158-2012.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-158-2013.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-158-2014.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-158-2015.html"
    capture_web(htmlurl,filename)
    htmlurl="http://www.yeeaoo.com/testlist/1-158-2016.html"
    capture_web(htmlurl,filename)
