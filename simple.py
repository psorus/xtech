import sys
from compile import addfile,filterq,readsettings

from foldery import *

import os


def simplecompile(q):

    folder="/home/psorus/q/tex/plt"

    isplt,_,sett,_,kw=filterq(read(folder+"/general.txt"),"plt")

    m=readsettings(sett,folder)

    begin=read("pattern/docstart.txt")

    begin=begin.replace("###name###","quixtech")

    middle=addfile(m,q)

    back=read("pattern/docend.txt")

    return begin+"\n"+middle+"\n"+back


if __name__=="__main__":
    query="#x*3#"
    if len(sys.argv)>1:query=sys.argv[1]
    q=simplecompile(query)

    with open("output.tex","w") as f:
        f.write(q)

    os.system("pdflatex output.tex")
    os.system("google-chrome-beta output.pdf")
