import os





def subprep(pth,tit):
    images,texts=[],[]
    lis=True
    wmode=True
    for fil in os.listdir(pth):
        if fil=="title":
            with open(pth+"/"+fil,"r") as f:
                tit=f.read()
            continue

        if fil.endswith(".png") or fil.endswith(".jpg") or fil.endswith(".jpeg") or fil.endswith("pdf"):
            images.append(fil)
        elif fil.endswith(".txt") or fil=="q":
            texts.append(fil)
        elif fil=="nonl":
            lis=False
        elif fil=="hmode":
            wmode=False

    if len(tit)>0:
        tit=f'title="{tit}"'
    else:
        tit=""


    #images=[pth+"/"+zw for zw in images]
    images=["../"+pth[8:]+"/"+zw for zw in images]#bodge
    texts=[pth+"/"+zw for zw in texts]
    cont=""
    contlen=0
    for text in texts:
        with open(text,"r") as f:
            cont+=f.read()+"\n"
        contlen+=1
    cont=cont.split("\n")
    cont=[zw for zw in cont if len(zw)>0]
    if lis:cont=[f"<e>{zw}</e>" for zw in cont]
    cont="\n".join(cont)

    if wmode:
        images=[f'<i f="{zw}" wmode="True"></i>' for zw in images]
    else:
        images=[f'<i f="{zw}"></i>' for zw in images]
    imle=len(images)
    widd=1/(imle+0.1)
    imaqes=[f'<que w="{widd}">{zw}</que>' for zw in images]
    images="\n".join(images)
    imaqes="\n".join(imaqes)
    imaqes=f'''<split>
{imaqes}
</split>'''


    if imle>0:
        if contlen>0:
            ret=f"""<frame {tit}>
    <split>
    <que>
    <list>
    {cont}
    </list>
    </que>
    <que>
    {images}
    </que>
    </split>
    </frame>"""
        else:
            if imle>=2:
                ret=f"""<frame {tit}>
{imaqes}
</frame>"""
            else:
                ret=f"""<frame {tit}>
{images}
</frame>"""
    elif imle==0:
        ret=f"""<frame {tit}>
        <list>
        {cont}
        </list>
        </frame>"""

    if not lis:
        ret=ret.replace("<list>","").replace("</list>","")

    ret=ret.replace("<e><l2st></e>","<l2st>")
    ret=ret.replace("<e></l2st></e>","</l2st>")

    return ret

    



def namclean(q):
    q=q.replace("_"," ")
    while len(q)>0 and (q[0]=="0" or q[0]=="1" or q[0]=="2" or q[0]=="3" or q[0]=="4" or q[0]=="5" or q[0]=="6" or q[0]=="7" or q[0]=="8" or q[0]=="9"):
        q=q[1:]
    return q

def prep(pth):
    opth=pth+"/data"
    os.system("rm -rf "+opth)
    os.makedirs(opth)
    pth+="/prep"
    slides=[[namclean(zw),pth+"/"+zw] for zw in os.listdir(pth) if os.path.isdir(pth+"/"+zw)]
    print("sorts",[zw[0] for zw in slides])
    slides.sort(key=lambda x:x[1])

    for i,(nam,pth) in enumerate(slides):
        cur=subprep(pth,nam)
        with open(opth+"/"+str(i).zfill(3)+nam+".txt","w") as f:
            f.write(cur)





if __name__ == "__main__":
    prep("/home/psorus/d/x/tether")


