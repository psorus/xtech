import numpy as np
import json

from strg import *
from foldery import *
from special import special
from formula import *

from os.path import isfile, isdir

from c import *

from advangle import byangles#(angles,saveas,title="")
from overlay import genoverlay 


class setting:
  def __init__(self,**kwargs):
    for key in kwargs.keys():
      setattr(self,key,kwargs[key])

def nl():
  return '''
'''
def addformula(q,**w):
  if w["mode"]:
    return gostec(q)
  else:
    return gotec(q)

def addtwoimg(fnam,fnam2,label,caption="",wid="0.9"):
  # wid="0.49"
  q=""
  if len(caption)>0:
    q=read("pattern/twoimagep.txt")
  else:
    q=read("pattern/twoimagenc.txt")
  q=q.replace("###wid###",str(float(wid)))
  q=q.replace("###file###",fnam)
  q=q.replace("###file2###",fnam2)
  q=q.replace("###caption###",caption)
  q=q.replace("###label###",label)
  
  global allsec
  allsec.append({"typ":"img2","files":[fnam,fnam2],"label":label,"caption":caption,"where":acfile})

  return q
def addthreeimg(fnam,fnam2,fnam3,label,caption="",wid="0.9"):
  # wid="0.49"
  q=""
  if len(caption)>0:
    q=read("pattern/threeimagep.txt")
  else:
    q=read("pattern/threeimagenc.txt")
  q=q.replace("###wid###",str(float(wid)/3))
  q=q.replace("###file###",fnam)
  q=q.replace("###file2###",fnam2)
  q=q.replace("###file3###",fnam3)
  q=q.replace("###caption###",caption)
  q=q.replace("###label###",label)
  
  global allsec
  allsec.append({"typ":"img3","files":[fnam,fnam2,fnam3],"label":label,"caption":caption,"where":acfile})

  
  return q
def addfourimg(fnam,fnam2,fnam3,fnam4,label,caption="",wid="0.9"):
  # wid="0.49"
  q=""
  if len(caption)>0:
    q=read("pattern/fourimagep.txt")
  else:
    q=read("pattern/fourimagenc.txt")
  q=q.replace("###wid###",str(float(wid)/4))
  q=q.replace("###file###",fnam)
  q=q.replace("###file2###",fnam2)
  q=q.replace("###file3###",fnam3)
  q=q.replace("###file4###",fnam4)
  q=q.replace("###caption###",caption)
  q=q.replace("###label###",label)

  global allsec
  allsec.append({"typ":"img4","files":[fnam,fnam2,fnam3,fnam4],"label":label,"caption":caption,"where":acfile})


  return q

def refile(fname,m):
  if len(fname)<=0:return fname
  if not ("\\" in fname):
    fname=join(m.imgfold,fname)
  fname=fname.replace("\\","/")
  if isfile(fname):
    return fname
  if isfile(fname+stdimgext):
    return fname+stdimgext
  if isfile(fname+altimgext):
    return fname+altimgext
  return fname
def addimg(**q):
  m=q["m"]
  wid="0.9"
  if "w" in q.keys():wid=q["w"].replace(",",".")
  if "wid" in q.keys():wid=q["wid"].replace(",",".")
  fname="none"
  usedq=False
  if "file" in q.keys():
    fname=q["file"]
  elif "f" in q.keys():
    fname=q["f"]
  elif len(q["q"])>0:
    fname=q["q"]
    usedq=True
  label=fname.replace("/","").replace("\\","").replace(".","")
  if "label" in q.keys():
    label=q["label"]
  fname=refile(fname,m)
  caption=""
  if "capt" in q.keys():
    caption=q["capt"]
  elif "caption" in q.keys():
    caption=q["caption"]
  elif len(q["q"])>0 and not usedq:
    caption=q["q"]
  fname2=""
  if "file2" in q.keys():
    fname2=q["file2"]
  elif "f2" in q.keys():
    fname2=q["f2"]
  fname3=""
  if "file3" in q.keys():
    fname3=q["file3"]
  elif "f3" in q.keys():
    fname3=q["f3"]
  fname4=""
  if "file4" in q.keys():
    fname4=q["file4"]
  elif "f4" in q.keys():
    fname4=q["f4"]
  didchance=True
  while didchance:
    didchance=False
    if len(fname3)==0 and len(fname4)>0:
      fname3=fname4
      fname4=""
      didchance=True
    if len(fname2)==0 and len(fname3)>0:
      fname2=fname3
      fname3=""
      didchance=True
    if len(fname)==0 and len(fname2)>0:
      fname=fname2
      fname2=""
      didchance=True
  fname2=refile(fname2,m)
  fname3=refile(fname3,m)
  fname4=refile(fname4,m)

  if fname.find("none")>-1 or fname2.find("none")>-1 or fname3.find("none")>-1 or fname4.find("none")>-1:
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("missing image",caption)    
    # print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
  if len(fname2)>0 and len(fname3)==0:
    # wid=str(float(wid)*0.49)
    return addtwoimg(fname,fname2,label,caption,wid)
  if len(fname3)>0 and len(fname4)==0:
    # wid=str(float(wid)*0.33)
    return addthreeimg(fname,fname2,fname3,label,caption,wid)
  if len(fname4)>0:
    # wid=str(float(wid)*0.25)
    return addfourimg(fname,fname2,fname3,fname4,label,caption,wid)
  

  heimode=True
  if "wmode" in q.keys():
    heimode=not bool(q["wmode"])
  
  q=""
  if heimode:
    if len(caption)>0:
      q=read("pattern/image.txt")
    else:
      q=read("pattern/imagenc.txt")
  else:
    if len(caption)>0:
      q=read("pattern/aimage.txt")
    else:
      q=read("pattern/aimagenc.txt")
  q=q.replace("###wid###",wid)
  q=q.replace("###file###",fname)
  q=q.replace("###caption###",caption)
  q=q.replace("###label###",label)

  global allsec
  allsec.append({"typ":"img","files":[fname],"label":label,"caption":caption,"where":acfile})

  
  return q
def runpy(**q):
  what=q["q"]
  return str(eval(what))
acfile=""
lastsec=""
def xsection(**q):
 
  title=""
  if "title" in q.keys():
    title=q["title"]
  elif len(q["q"])>0:
    title=q["q"]
  label=title
  if "label" in q.keys():
    label=q["label"]
  global allsec
  allsec.append({"typ":q["fil"],"title":title,"label":label,"file":acfile,"issec":True})
  global lastsec
  lastsec=label
  return read("pattern/"+q["fil"]+".txt").replace("###title###",title).replace("###label###",label)

def additem(**q):
  ac=q["q"]
  
  # if len(ac)>0:
    # ac=ac[0].upper()+ac[1:]
    # ac=ac.strip()
    # if not(ac[-1]=="." or ac[-1]=="!" or ac[-1]=="?"):
      # ac=ac+"."
  
  
  p=read("pattern/item.txt")
  p=p.replace("###q###",ac)
  return p
  

def addlist(**q):
  data=q["q"]
  data=listfilter(data,m=q["m"])
  data=calledfilter(data,"e",additem,m=q["m"])
  
  p=read("pattern/list.txt")
  p=p.replace("###q###",data)
  return p  
def listfilter(q,m):
  q=calledfilter(q,"list",addlist,m=m)
  q=calledfilter(q,"l1st",addlist,m=m)
  q=calledfilter(q,"l2st",addlist,m=m)
  q=calledfilter(q,"l3st",addlist,m=m)
  q=calledfilter(q,"l4st",addlist,m=m)
  q=calledfilter(q,"l5st",addlist,m=m)
  q=calledfilter(q,"l6st",addlist,m=m)
  q=calledfilter(q,"l7st",addlist,m=m)
  q=calledfilter(q,"l8st",addlist,m=m)
  q=calledfilter(q,"l9st",addlist,m=m)
  return q
def addque(**q):
  wid="0.48"
  if "wid" in q.keys():
    wid=q["wid"]
  elif "w" in q.keys():
    wid=q["w"]
  q=q["q"]
  
  p=read("pattern/splitque.txt")
  p=p.replace("###wid###",wid)
  p=p.replace("###q###",q)
  return p
  
def addsplit(**q):
  data=q["q"]
  
  data=calledfilter(data,"que",addque,m=q["m"])
  
  p=read("pattern/splitframe.txt")
  p=p.replace("###q###",data)
  return p
def addframe(**q):
  m=q["m"]
  #label,title
  title=""
  if "title" in q.keys():
    title=q["title"]
  elif "t" in q.keys():
    title=q["t"]
  label=title
  if "label" in q.keys():
    label=q["label"]
  elif "l" in q.keys():
    label=q["l"]
  hidden=False
  if "hidden" in q.keys():
    hidden=bool(q["hidden"])
  if hidden:
    ret=read("pattern/framehidden.txt")
  else:
    ret=read("pattern/frame.txt")
  ret=ret.replace("###title###",title)
  ret=ret.replace("###label###",label)
  ret=ret.replace("###q###",q["q"])
  return ret

loop=""
loopx=0.0
loopy=0.0
loopr=1.0
def addloop(**q):
  # print("added loop",q)
  global loop
  nam=q["q"]
  if "which" in q.keys():nam=q["which"]
  if "w" in q.keys():nam=q["w"]
  
  global loopx
  global loopy
  global loopr
  
  loopx=0
  if "x" in q.keys():loopx=float(q["x"])
  if "loopx" in q.keys():loopx=float(q["loopx"])
  loopy=0
  if "y" in q.keys():loopy=float(q["y"])
  if "loopy" in q.keys():loopy=float(q["loopy"])
  loopr=1
  if "r" in q.keys():loopr=float(q["r"])
  if "loopr" in q.keys():loopr=float(q["loopr"])
  
  
  
  loop=nam
  
  return ""
  

allnodes=[]
nodedex=0
def addnode(**q):
  global nodedex
  global allnodes
  m=q["m"]
  #label,title
  title=""
  if "title" in q.keys():
    title=q["title"]
  elif "t" in q.keys():
    title=q["t"]
  label=title
  if "label" in q.keys():
    label=q["label"]
  elif "l" in q.keys():
    label=q["l"]
  
  c=[]
  if "c" in q.keys():
    c=eval(q["c"])
    c=[{"key":cc} for cc in c]
  # hidden=False
  # if "hidden" in q.keys():
    # hidden=bool(q["hidden"])
  allnodes.append({"id":nodedex,"label":label,"title":title,"loop":loop,"c":c,"looplen":-1,"loopx":loopx,"loopy":loopy,"loopr":loopr})
  ret=read("pattern/grapage.txt")
  ret=ret.replace("###title###",title)
  ret=ret.replace("###label###",str(nodedex))
  nodedex+=1
  ret=ret.replace("###q###",q["q"])
  return ret

def xfootnote(**q):
  ac=q["q"]
  ac=ac[0].upper()+ac[1:]
  ac=ac.strip()
  if not(ac[-1]=="." or ac[-1]=="!" or ac[-1]=="?"):
    ac=ac+"."
  return "\\footnote{"+ac+"}"

def xblock(**q):
    ac=q["q"]
    if "wid" in q.keys():
        wid=str(q["wid"])
    else:
        wid="5"
    if "x" in q.keys():
        x=str(q["x"])
    else:
        x="1.0"
    if "y" in q.keys():
        y=str(q["y"])
    else:
        y="1.0"
    ret=read("pattern/block.txt")

    ret=ret.replace("###wid###",wid)
    ret=ret.replace("###x###",x)
    ret=ret.replace("###y###",y)
    ret=ret.replace("###q###",ac)

    return ret

def xcbox(**q):
  fg=q["f"]
  bg=q["b"]
  data=q["q"]
  ret= read("pattern/cbox.txt")
  
  ret=ret.replace("###fg###",fg)
  ret=ret.replace("###bg###",fg)
  ret=ret.replace("###q###",data)

  return ret


backrefs={}
def xref(**q):
  what=q["q"]
  typ="sec"
  if "t" in q.keys():
    typ=q["t"]
  if "typ" in q.keys():
    typ=q["typ"]
  if typ=="sec":
    global backrefs
    if not what in backrefs.keys():
      backrefs[what]=[]
    backrefs[what].append(lastsec)
  
  return read("pattern/ref.txt").replace("###q###",what).replace("###t###",typ)

def gentmode(collums,modus):
  modus=modus.lower()
  if modus=="f":modus="free"
  if modus=="c":modus="classic"
  if modus=="c2":modus="classic2"

  if modus=="free":
    return " ".join(["c" for i in range(collums)])
    
  if modus=="classic":
    rel=gentmode(collums,"free")
    return "c | "+rel[2:] 

  if modus=="classic2":
    rel=gentmode(collums,"free")
    return "c | c |"+rel[4:] 



  if modus=="full":
    rel=gentmode(collums,"free")
    return rel.replace(" "," | ")
    
def addtable(**q):
  # print("adding table",q)
  
  inside=q["q"]
  collums=3
  if "c" in q.keys():collums=q["c"]
  if "cols" in q.keys():collums=q["cols"]
  if "collums" in q.keys():collums=q["collums"]
  collums=int(collums)
  
  caption=""
  if "cap" in q.keys():caption=q["cap"]
  if "caption" in q.keys():caption=q["caption"]
  
  modus="classic"
  # if "m" in q.keys():modus=q["m"]
  if "mode" in q.keys():modus=q["mode"]
  if "modus" in q.keys():modus=q["modus"]
  
  global allsec
  label="table"+str(1+len([1 for q in allsec if q["typ"]=="table"]))
  if "l" in q.keys():label=q["l"]
  if "lab" in q.keys():label=q["lab"]
  if "label" in q.keys():label=q["label"]
  
  allsec.append({"typ":"table","caption":caption,"label":label,"file":acfile})
  
  if len(caption)>0:
    rel=read("pattern/table.txt")
  else:
    rel=read("pattern/tablenc.txt")
  
  rel=rel.replace("###label###",label)
  rel=rel.replace("###caption###",caption)
  rel=rel.replace("###head###",gentmode(collums=collums,modus=modus))
  rel=rel.replace("###q###",inside)

  return rel

def addtline(**q):
  prep=[ac for ac in q["q"].split("~") if len(ac)>0]
  for i in range(len(prep)):
    try:
      ac=float(prep[i])
      prep[i]="#"+prep[i]+"#"
    except:pass
      

  ret= " & ".join(prep)
  ret+=" \\\\\n"
  return ret

def addhline(**q):
  return read("pattern/hline.txt")

def returnnothing(**q):
  return ""

def addtoc(**q):
  title=""
  if "title" in q.keys():
    title=q["title"]
  elif len(q["q"])>0:
    title=q["q"]
  else:
    title="Inhaltsverzeichnis"
  return read("pattern/toc.txt").replace("###title###",title)
def addtitlepage(**q):
  title=""
  if "title" in q.keys():title=q["title"]
  subtitle=""
  if "subtitle" in q.keys():subtitle=q["subtitle"]
  name="Simon Kluettermann"
  if "name" in q.keys():name=q["name"]
  department="Insitute for theoretical Particle Physics and Cosmology"
  if "department" in q.keys():department=q["department"]
  university="RWTH Aachen"
  if "university" in q.keys():university=q["university"]
  country="Germany"
  if "country" in q.keys():country=q["country"]
  
  return read("pattern/titlepage.txt").replace("###title###",title).replace("###subtitle###",subtitle).replace("###name###",name).replace("###department###",department).replace("###university###",university).replace("###country###",country)
    
def addcite(**q):
  what=q["q"]
  if "w" in q.keys():what=q["w"]
  if "what" in q.keys():what=q["what"]
  
  return read("pattern/cite.txt").replace("###what###",what)
def addhlink(**q):
  print("hlink",q)
  

  if "w" in q.keys():what=q["w"]
  if "where" in q.keys():what=q["what"]
  

  return read("pattern/hyperlink.txt").replace("###where###",what).replace("###q###",q["q"])
def makebold(**q):
  q=q["q"]
  
  return read("pattern/bold.txt").replace("###q###",q)
  
def addmultiply(**q):
  inside=q["q"]
  
  repl=eval(q["w"])
  
  # print(inside)
  # print("inside has len ",len(inside))
  # print(repl)
  # print("repl has cou ",len(repl))
  # exit()
  
  return "\n\n".join([inside.replace("???",rep).replace("?i?",str(i)) for i,rep in enumerate(repl)])
  
  # print("!!!!")
  # print(repl)
  # print("!!!!")
  
  # exit()
  
def addphibox(**q):
  inn=q["q"]
  phi=q["phi"]
  phi=float(phi)*np.pi/180
  
  midx=220
  midy=140
  rx=150
  ry=80
  
  x=midx+rx*np.sin(phi)
  y=midy+ry*np.cos(phi)
  
  return read("pattern/phibox.txt").replace("###x###",str(x)).replace("###y###",str(y)).replace("###q###",inn)
  
  
  

def addfile(m,fil):
  print("adding file",fil)
  global acfile
  acfile=fil
  
  s=read(fil)
  s=calledfilter(s,"multiply",addmultiply)
  s=calledfilter(s,"repeat",addmultiply)
  
  s=calledfilter(s,"ignore",returnnothing)
  s=calledfilter(s,"python",runpy)
  
  
  s=calledfilter(s,"special",special,m=m)
  s=calledfilter(s,"toc",addtoc,m=m)
  s=calledfilter(s,"titlepage",addtitlepage,m=m)
 
  s=calledfilter(s,"frame",addframe,m=m)
  
  s=calledfilter(s,"loop",addloop)
  s=calledfilter(s,"node",addnode,m=m)
  
  s=calledfilter(s,"section",xsection,m=m,fil="section")
  s=calledfilter(s,"subsection",xsection,m=m,fil="subsection")
  s=calledfilter(s,"subsubsection",xsection,m=m,fil="subsubsection")
  s=calledfilter(s,"paragraph",xsection,m=m,fil="paragraph")

  s=calledfilter(s,"split",addsplit,m=m)
  s=listfilter(s,m=m)
  
  
  s=calledfilter(s,"phibox",addphibox)
  s=calledfilter(s,"block",xblock)
  
  
  s=calledfilter(s,"table",addtable,m=m)
  s=calledfilter(s,"tline",addtline,m=m)
  s=calledfilter(s,"hline",addhline,m=m)
  
  

  s=calledfilter(s,"refi",xref,m=m,t="fig")#a bit of abodge, but...
  s=calledfilter(s,"refs",xref,m=m,t="sec")
  s=calledfilter(s,"reft",xref,m=m,t="table")
  s=calledfilter(s,"ref",xref,m=m)
  s=calledfilter(s,"cite",addcite)
  s=calledfilter(s,"link",addhlink)
  
  s=calledfilter(s,"note",xfootnote,m=m)
  s=calledfilter(s,"cbox",xcbox,m=m)


  s=calledfilter(s,"i",addimg,m=m)
  s=betweencall(s,"##",addformula,mode=False)
  s=betweencall(s,"#",addformula,mode=True)
  
  s=calledfilter(s,"b",makebold,m=m)
  
 
  return s
def commentary(q):
  return nl()+"%"+q+nl()
def addfolder(m,folder):
  print("adding folder",folder)
  ret=""
  for path,isfil in advlist(folder):
    if path.find(".swp")>-1:continue
    if isfil:
      ret+=nl()+commentary("from file "+path)+addfile(m,path)
    else:
      ret+=nl()+commentary("from folder "+path)+addfolder(m,path)
  return ret
def compileplt(m,folder):
  

  begin=read("pattern/pltstart.txt")
 
  begin=begin.replace("###shorttitle###",m.stitle)
  begin=begin.replace("###title###",m.title)
  begin=begin.replace("###author###",m.author)
  begin=begin.replace("###theme###",m.theme)
  begin=begin.replace("###colo###",m.colo)
  
  addin=""
  if len(m.institute)>0:addin+="\n \institute{"+m.institute+"}"
  begin=begin.replace("###addin###",addin)

  middle=""

  middle=addfolder(m,folder+"/data") 



  back=read("pattern/pltend.txt")  
  
  

  return begin+nl()+middle+nl()+back
def compiledoc(m,folder,bib):
  

  begin=read("pattern/docstart.txt")
 
  begin=begin.replace("###name###",m.name)

  middle=""

  middle=addfolder(m,folder+"/data") 



  if bib:
    back=read("pattern/docendbib.txt")  
  else:
    back=read("pattern/docend.txt")  
  
  

  return begin+nl()+middle+nl()+back

def compilegra(m,folder):
  

  begin=read("pattern/grastart.txt")
 
  begin=begin.replace("###shorttitle###",m.stitle)
  begin=begin.replace("###title###",m.title)
  begin=begin.replace("###author###",m.author)
  # begin=begin.replace("###theme###",m.theme)
  # begin=begin.replace("###colo###",m.colo)
  
  addin=""
  if len(m.institute)>0:addin+="\n \institute{"+m.institute+"}"
  begin=begin.replace("###addin###",addin)

  middle=""

  middle=addfolder(m,folder+"/data") 



  back=read("pattern/graend.txt")  
  
  

  return begin+nl()+middle+nl()+back

  
def readsettings(q,folder,**kw):
  m=setting(**kw)
 
  m.imgfold="../imgs"#relative to the latex dir
  m.folder=folder#relativ to the actual dir
  _,m.name,q,_=sfilterq(q,"name")
  
  
  _,m.stitle,q,_=asfilterq(q,"stitle")
  _,m.title,q,_=asfilterq(q,"title")
  _,m.author,q,_=asfilterq(q,"author","Simon Kluettermann")
  _,m.theme,q,_=asfilterq(q,"theme","Berlin")
  _,m.colo,q,_=asfilterq(q,"colo","whale")
  _,m.institute,q,_=asfilterq(q,"institute")
 
 
  # print(m.title,m.stitle)
  # exit()
 
  return m
def getbat(bib):
  if bib:
    return read("pattern/batbib.txt")
  else:
    return read("pattern/bat.txt")
def getsh(bib):
  return getbat(bib)


def killdoubles(l):
  ll=[]
  for lll in l:
    if not lll in ll:
      ll.append(lll)
  return ll
def techbackref(l):
  #\ref{sec:###q###}
  
  base="[\\ref{sec:###q###}] "
  
  ll=[base.replace("###q###",ac) for ac in killdoubles(l)]
  
  
  return "{\scriptsize Referenced in: "+"".join(ll)+" \par}"

def enterbackrefs(data,b):
  for key in b.keys():
    data=data.replace("{{{for_"+key+"}}}",techbackref(b[key]))
    #allsec.append({"typ":q["fil"],"title":title,"label":label,"file":acfile,"issec":True})
  for entry in allsec:
    if "issec" in entry.keys():
      data=data.replace("{{{for_"+entry["label"]+"}}}","")
  return data

def somebib(**q):
  what=q["what"]
  del q["what"]
  name=q["q"]
  del q["q"]
  if "w" in q.keys():
    name=q["w"]
    del q["w"]
  if "n" in q.keys():
    name=q["n"]
    del q["n"]
  if "name" in q.keys():
    name=q["name"]
    del q["name"]
  
  ret="@"+what+"{"+name+",\n"
  
  for key in q.keys():
    val=q[key]
    ret+=f'{key} = "{val}",\n'
  
  ret+="}"
  
  return ret
  
def refraw(**q):
  return q["q"]


def handleonebib(file):
  q=read(file)
  
  if "<" in q:
    
    
    q=calledfilter(q,"ignore",returnnothing)
    
    q=calledfilter(q,"raw",refraw)
    q=calledfilter(q,"misc",somebib,what="misc")
    q=calledfilter(q,"article",somebib,what="article")
    q=calledfilter(q,"book",somebib,what="book")
    q=calledfilter(q,"misc",somebib,what="misc")
    q=calledfilter(q,"phdthesis",somebib,what="phdthesis")
    q=calledfilter(q,"pthesis",somebib,what="phdthesis")
    q=calledfilter(q,"mthesis",somebib,what="masterthesis")
    q=calledfilter(q,"unpublished",somebib,what="unpublished")
  
  return q
  
  

def handlebib(folder):
  if not isdir(folder):return None

  ret=""
  
  for path,isfil in advlist(folder):
    if isfil:
      ac=handleonebib(path)
    else:
      ac=handlebib(path)
    if not ac is None:ret+=ac+"\n\n"
    
  if len(ret.replace("\n",""))==0:return None
    
  return ret

def gencol(node):
  c=node["c"]
  idd=node["id"]
  ret=[]
  
  for cc in c:
    if cc["q"]-1==idd:# or (cc["q"]==0 and  idd==node["looplen"]-1:
      ret.append("red")
      continue
    
    ret.append("black")
  
  
  return ret

def generatebackimgs(folder):
  #byangles
  #  allnodes.append({"id":nodedex,"label":label,"title":title,"loop":loop})

  for node in allnodes:
    byangles([int(c["phi"]) for c in node["c"]],gencol(node),folder+"\\imgs\\back\\page"+str(node["id"]),title=node["title"])
    print("generated",node)


def orderloops(q):
  q=list(q)
  q.sort()
  if "main" in q:
    q.remove("main")
    q.insert(0,"main")
  if "" in q:
    q.remove("")
    q.insert(0,"")
  
  return q

def cononeloop(nodes):
  mp={node["label"]:node["id"]for node in allnodes}
 

  ln=len(nodes)
  for i in range(ln):
    nodes[i]["c"].append({"q":(i+1)%ln,"phi":(360*(1-i/ln)+90)%360})
    nodes[i]["c"].append({"q":(i-1)%ln,"phi":(360*(1-i/ln)+180)%360})
    nodes[i]["phi"]=(360*(1-i/ln)+135)%360
  return nodes

def conhandle(nodes):
  mp={node["label"]:node["id"]for node in allnodes}
 

  ln=len(nodes)
  for i in range(ln):
    for j in range(len(nodes[i]["c"])):
      
      if "key" in nodes[i]["c"][j].keys():
        idd=mp[nodes[i]["c"][j]["key"]]
        nodes[i]["c"][j]={"q":idd,"phi":0.0}
        nodes[idd]["c"].append({"q":i,"phi":0.0})

  for i in range(ln):
    for j in range(len(nodes[i]["c"])):
      
      alpha0=nodes[i]["phi"]
      delta=1/(nodes[i]["looplen"])
      otq=nodes[i]["c"][j]["q"]
      
      
      diff=abs(i-otq)
      diff2=abs(nodes[i]["looplen"]+i-otq)
      
      
      
      diffuse=diff
      if diff2<diffuse:diffuse=diff2
      
      # if diffuse>2:
        # print("using difference",diffuse,i,j,delta*diff)
        # exit()
      
      nodes[i]["c"][j]["phi"]=180-(alpha0+delta*diff*180)-1
      # if otq>i:
        # pass
      # else:
      if i>=otq or diff2<diff:
        nodes[i]["c"][j]["phi"]=180*(1-2*delta)+nodes[i]["c"][j]["phi"]#(360-alpha0-delta*(i-otq))
      
      while nodes[i]["c"][j]["phi"]<0:nodes[i]["c"][j]["phi"]+=360
      while nodes[i]["c"][j]["phi"]>360:nodes[i]["c"][j]["phi"]-=360

  # print(json.dumps(nodes,indent=2))
  
  # exit()
  
  return nodes

def norderset(q):
  ret=[]
  for qq in q:
    if not qq in ret:ret.append(qq)
  return ret

def createconnections():
  #allnodes.append({"id":nodedex,"label":label,"title":title,"loop":loop,"c":[]})

  global allnodes
  loops=norderset([qq["loop"] for qq in allnodes])
  
  newnodes=[]
  maxll=int(np.max([np.sum([1 for qq in allnodes if qq["loop"]==loop]) for loop in loops]))
  for loop in loops:
    acnodes=[qq for qq in allnodes if qq["loop"]==loop]
    for i in range(len(acnodes)):
      acnodes[i]["looplen"]=maxll
    for nnode in cononeloop(acnodes):
      # print("nnode",nnode)
      nnode["looplen"]=maxll
      newnodes.append(nnode)
      
    
  
  allnodes=conhandle(newnodes)
  
  
  # print(loops)
  # exit()
def enteroverlay(allnodes,folder,data):
  # print(json.dumps(allnodes,indent=2))
  
  with open("debug.txt","w") as f:
    f.write(json.dumps(allnodes,indent=2))
    
  tele=genoverlay(allnodes,folder+"\\imgs\\back\\overlay")
  
  
  data=data.replace("{{{overlay}}}",read("pattern/overlay.txt"))
  
  links=""
  
  for tel in tele:
    wid=tel[3]-tel[1]
    hei=tel[4]-tel[2]
    px=tel[1]
    py=1-tel[4]
    links+=read("pattern\\gramap2.txt").replace("###wid###",str(wid)).replace("###px###",str(px)).replace("###py###",str(py)).replace("###goto###","page"+str(tel[0]))+"\n"
  
  data=data.replace("{{{teleports}}}",links)
  
  
  
  return data
  
  exit()


def entertrafos(data):
  #allnodes
  
  # print("!!!",len(allnodes))
   
  for node in allnodes:
    c=node["c"]
    idd=node["id"]
    ret=""
    for cc in c:
      phi=cc["phi"]
      
      wid=3
      if phi<45 or phi>315 or (phi>225 and phi<225+90):wid=5
      
      wid*=2
      
      phi0=phi
      phi-=90
      while phi<0:phi+=360
      while phi>360:phi-=360
      phi2=phi*np.pi/180
      #x axis: 200-420
      #y axis: 109-220
      px,py=210+210*np.cos(phi2),110+110*np.sin(phi2)
      
      if phi<=45 or phi>=315:px=420
      if phi<=225 and phi>=135:px=0
      if phi>=45 and phi<=135:py=220
      if phi>=225 and phi<=315:py=0
      
      px-=wid*0.3
      py-=wid*0.1
      
      goto=cc["q"]
      ret+=read("pattern\\gramap.txt").replace("###wid###",str(wid)).replace("###px###",str(px)).replace("###py###",str(py)).replace("###goto###","page"+str(goto)).replace("###phi###",str(phi))+"\n"
    data=data.replace("{{{trafo"+str(idd)+"}}}",ret)
    # print("replacing","{{{trafo"+str(idd)+"}}}",ret)
  
  return data


def xfilter(q):
  q=q.replace("->","$\Rightarrow$")

  return q

def compile(folder):
  global allsec
  allsec=[]
  
  g=read(folder+"/general.txt")

  isdoc=False
  isplt=False
  isgra=False
 
  #doc
  isdoc,_,sett,_,kw=filterq(g,"doc")
  if not isdoc:isplt,_,sett,_,kw=filterq(g,"plt")
  if not (isdoc or isplt):isgra,_,sett,_,kw=filterq(g,"gra")

 
  m=readsettings(sett,folder,**kw)
  if isdoc:m.typ="doc"
  if isplt:m.typ="plt"
  data=""  

  bib=handlebib(folder+"/bib/")

  if isdoc:
    data=compiledoc(m,folder,bib=not bib is None)
    data=enterbackrefs(data,backrefs)

  if isplt:
    data=compileplt(m,folder)

  if isgra:
    data=compilegra(m,folder)

  
  
  
  

  assert assertfolder(folder+"/out")
  if isgra:
    assert assertfolder(folder+"/imgs/back")
  
  # print(len(allnodes))
  
  if isgra:
    createconnections() 
  # print("!",len(allnodes))
  
  if isgra:
    generatebackimgs(folder)
  # print("!!",len(allnodes))
    
  if isgra:
    data=entertrafos(data)
  # print("!!!!",len(allnodes))
  
  if isgra:
    data=enteroverlay(allnodes,folder,data)
  
  data=xfilter(data)
  
  write(fil=folder+"/out/main.tex",x=data)

  write(fil=folder+"/out/compile.bat",x=getbat(not bib is None))
  write(fil=folder+"/out/compile.sh",x=getsh(not bib is None))
  write(fil=folder+"/out/label.json",x=json.dumps(allsec,indent=2))
  
  if not bib is None:write(fil=folder+"/out/main.bib",x=bib)
  
  run("chmod 777 "+folder+"/out/compile.sh")  
  



