import requests
from bs4 import BeautifulSoup
import os
path="https://raw.github.com/mahongquan/OpenBird/master/"
def savefile(pathf):
    print path+pathf
    res=requests.get(path+pathf)#"Classes/AppDelegate.h")
    ps=pathf.split("/")
    p="/".join(ps[:-1])
    if os.path.exists(p):
        pass
    else:
        os.makedirs(p)
    open(p+"/"+ps[-1],"w").write(res.content)
    
# files=""

# res=requests.get("https://raw.github.com/mahongquan/OpenBird/master/Classes/AppDelegate.h")
# open("AppDelegate.h","w").write(res.content)
def getpath(path):
    res=requests.get("https://github.com/mahongquan/OpenBird/tree/master/"+path)
    #open("content.html","w").write(res.content)
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
        savefile("/".join(ps[5:]))
    for p in paths:
        getpath(p)
def main():
    getpath("proj.android/src")
#savefile("Resources/res/sfx_point.ogg")
#savefile("proj.ios_mac/FlappyBird.xcodeproj/mac/")
main()







