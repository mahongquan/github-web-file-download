import requests
from bs4 import BeautifulSoup
import os
outputpath="."
def getfile(path,pathf):
    print("get file:"+pathf)
    res=requests.get(path+pathf)#"Classes/AppDelegate.h")
    ps=pathf.split("/")
    p="/".join(ps[:-1])
    p=outputpath+"/"+p
    if not os.path.exists(p):
        os.makedirs(p)
    open(p+"/"+ps[-1],"wb").write(res.content)
def getpath(path):
    print("getpath:"+path)
    if path!="":
        res=requests.get(path)
    else:
        print("no path")
        return
    soup = BeautifulSoup(res.content)
    tbs=soup.find_all('table')
    #print(tbs)
    t=tbs[0]
    rs=t.find_all('tr')
    fs=[]
    paths=[]
    for r in rs:
        cs=r.find_all('td')
        if len(cs)==5:
            if cs[0].img['alt']=="[DIR]":
                pass
            else:
                getfile(path,cs[1].a['href'])
    return
def main():
    getpath("http://www.pygtk.org/pygtk2tutorial/examples/")#all
if __name__=="__main__":
    main()















