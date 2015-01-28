import requests
from bs4 import BeautifulSoup
import os
repname="mahongquan/github-web-file-download"
reppath="https://raw.github.com/"+repname+"/master/"
outputpath="."
def getfile(pathf):
    print "get file:"+pathf
    reppath="https://raw.githubusercontent.com/"+repname+"/master/"
    #print reppath+pathf
    #raw_input("pause")
    res=requests.get(reppath+pathf)#"Classes/AppDelegate.h")
    ps=pathf.split("/")
    p="/".join(ps[:-1])
    p=outputpath+"/"+p
    if not os.path.exists(p):
        os.makedirs(p)
    open(p+"/"+ps[-1],"w").write(res.content)
def getpath(path):
    print "getpath:"+path
    if path=="":
        path="https://github.com/"+repname
        res=requests.get(path)
    else:
        print reppath+path
        res=requests.get(reppath+path)
    # print res
    # print dir(res)
    # f=open("res.html","w")
    # f.write(res.content)
    # f.close()
    # raw_input()
    soup = BeautifulSoup(res.content)
    #soup = BeautifulSoup(open("res.html","r").read())
    tbs=soup.find_all('table')
    t=tbs[0].tbody
    rs=t.find_all('tr')
    fs=[]
    paths=[]
    for r in rs:
        cs=r.find_all('td')
        cls=cs[0].span['class']
        print "class="+str(cls)
        if cls==None:
            pass
        elif cls[1]==u"octicon-file-directory":
            print "ispath"
            f=cs[1].a['href']
            ps=f.split("/")
            childpath="/".join(ps[5:])
            print childpath
            paths.append(childpath)
        elif cls[1]=="octicon-alert":
            pass
        else:
            print "is file"
            fs.append(cs[1].a['href'])
    for f in fs:
        print f
        ps=f.split("/")
        getfile("/".join(ps[5:]))
    for p in paths:
        getpath(p)
def setrepname(nm):
	global repname
	global reppath
	global outputpath
	repname=nm
	outputpath=nm.split("/")[1]
	reppath="https://github.com/"+repname+"/tree/master/"
def main():
    #print "Attention! New folder will be created in current path,download files  will be saved there,continue y/n?"
    #input=raw_input()
    #if input.lower()=="y":
    #    pass
    #else:
    #    return
    setrepname("dkstar88/lemonade-jack")
    getpath("Classes")#all
    #getpath("Resources")#all
if __name__=="__main__":
    main()















