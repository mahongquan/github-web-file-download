import requests
from bs4 import BeautifulSoup
import os
repname="mahongquan/github-web-file-download"
reppath="https://raw.github.com/"+repname+"/master/"
outputpath="."
def getfile(pathf):
    print "get file:"+pathf
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
        res=requests.get(reppath+path)
    soup = BeautifulSoup(res.content)
    rs=soup.tbody.find_all('tr')
    fs=[]
    paths=[]
    for r in rs:
        cs=r.find_all('td')
        print cs[0].span['class']
        if cs[0].span['class'][1]==u"octicon-file-directory":
            print "ispath"
            f=cs[1].a['href']
            ps=f.split("/")
            childpath="/".join(ps[5:])
            print childpath
            paths.append(childpath)
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
	reppath="https://raw.github.com/"+repname+"/master/"
def main():
    print "Attention! New folder will be created in current path,download files  will be saved there,continue y/n?"
    input=raw_input()
    if input.lower()=="y":
        pass
    else:
        return
    setrepname("mahongquan/github-web-file-download")
    getpath("")#all
if __name__=="__main__":
    main()







