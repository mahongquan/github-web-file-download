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
def main():
    res=requests.get("https://github.com/mahongquan/OpenBird/tree/master/proj.ios_mac/mac")
    #open("content.html","w").write(res.content)
    soup = BeautifulSoup(res.content)
    rs=soup.tbody.find_all('tr')
    fs=[]
    for r in rs:
        cs=r.find_all('td')
        fs.append(cs[1].a['href'])
    for f in fs:
        print f
        ps=f.split("/")
        savefile("/".join(ps[5:]))
#savefile("Resources/res/sfx_point.ogg")
#savefile("proj.ios_mac/FlappyBird.xcodeproj/mac/")
main()



