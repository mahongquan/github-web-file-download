import requests
from bs4 import BeautifulSoup
import os
tag="/master/"
repname="mahongquan/github-web-file-download"
reppath="https://raw.github.com/"+repname+tag
outputpath="."
soup=None
def getfile(pathf):
    print("get file:"+pathf)
    reppath="https://raw.githubusercontent.com/"+repname+tag
    print(reppath)
    print(reppath+pathf)
    input("pause")
    #raw_input("pause")
    res=requests.get(reppath+pathf)#"Classes/AppDelegate.h")
    ps=pathf.split("/")
    p="/".join(ps[:-1])
    p=outputpath+"/"+p
    if not os.path.exists(p):
        os.makedirs(p)
    open(p+"/"+ps[-1],"wb").write(res.content)
def getpath(path):
    print("getpath:"+path)
    if path=="":
        path="https://github.com/"+repname
        print(path)
        res=requests.get(path)
    else:
        print(reppath+path)
        res=requests.get(reppath+path)
    print(res.content)
    # content=open("files.html").read()
    soup = BeautifulSoup(res.content,"html.parser")
    rs=soup.find_all(attrs={"role":"row"})
    print(len(rs))
    fs=[]
    paths=[]
    for r in rs[1:]:
        cs=r.find_all(attrs={"role":"gridcell"})
        hds=r.find_all(attrs={"role":"rowheader"})
        if cs[0].svg!=None:
            cls=cs[0].svg['class']
            print("class="+str(cls))
            if cls==None:
                pass
            elif cls[1]==u"octicon-file-directory":
                f=hds[0].a['href']
                ps=f.split("/")
                childpath="/".join(ps[5:])
                print("ispath",childpath)
                paths.append(childpath)
            elif cls[1]=="octicon-alert":
                pass
            else:
                print("is file",hds[0].a['href'])
                fs.append(hds[0].a['href'])
    for f in fs:
        print(f)
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
	reppath="https://github.com/"+repname+"/tree"+tag
def main():
    setrepname("mahongquan/install_auto")
    #getpath("js/src")#all
    #getpath("assets/js/vendor")#assets/js/vendor
    getpath("")#assets/js/vendor
    #getpath("Resources")#all
if __name__=="__main__":
    main()
