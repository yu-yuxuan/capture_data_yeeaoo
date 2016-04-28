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
    filename=input('Enter file name here: ') # "Task1"
    silentremove(filename)
    while True:
        htmlurl=input('Enter url(loop) here: ') # "http://www.yeeaoo.com/testlist/1-155-2006.html"
        if htmlurl == "":                       # If it is a blank line...
            break                               # ...break the loop""
        capture_web(htmlurl,filename)
