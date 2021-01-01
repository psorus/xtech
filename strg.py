import numpy as np



def Trim(q):
  return q.strip()
def kwargread(**kwargs):
  ret={}
  for zw in kwargs:
    ret[zw]=kwargs[zw]
  return ret
def del34(q):
  if len(q)<2:return q
  if (q[0]==q[-1] and (q[0]=='"' or q[0]=="'")):return q[1:-1]
  return q
def readic(q):
  if "=" in q:
    # print(q)
    return eval("kwargread("+Trim(q).replace('" ','",')+")")
  elif len(q)==0:
    return {}
  else:
    return {"q":del34(q)}
def filterq(q,key):
  #if contains any a<key kwargs>b</key>c   returns True,a,b,c,{kwargs}
  #                          else   returns False,a,a,a,{}
  
  oq=q

  s1="<"+key
  s1p=">"
  s1p2="/>"
  s2="</"+key+">"
  
  i1=q.find(s1)
  if i1<0:return False,oq,oq,oq,{}
  a=q[:i1]

  q=q[i1+len(s1):]
  ip=q.find(s1p)
  ip2=q.find(s1p2)

  modus=True#modus <></> enabled
  iq=ip
  if ip<0:
    if ip2<0:
      return False,oq,oq,oq,{}#mode that just does not work
    else:#<??/> modus
      iq=ip2
      modus=False
  else:
    if ip2<0:#<></> modus
      #iq=ip#standart values, so useles
      #modus=True
      pass
    else:
      if ip<ip2:
        #<></> modus
        pass
      else:
       iq=ip2
       modus=False
  p=q[:iq]
  p=Trim(p)
  dic=readic(p)


  if modus:
    q=q[iq+len(s1p):]
  else:
    q=q[iq+len(s1p2):]
  
  i2=q.find(s2)
  if i2<0 or (not modus):
    #if no closing: then assume no midth
    return True,a,"",q,dic
  b=q[:i2]
  c=q[i2+len(s2):]
  return True,a,b,c,dic
def sfilterq(q,key,std=""):
  #filterq, but the position does not matter

  b,x,y,z,dic=filterq(q,key)
  if b:
    return True,y,x+z,dic
  else:
    return False,std,x,dic
def asfilterq(q,key,std=""):#filterq, but if no result, then take q
  a,b,c,d=sfilterq(q,key,std=std)
  if not a:return a,b,c,d
  if len(Trim(b))<1:b=d["q"]
  return a,b,c,d
def calledfilter(q,key,func,**kwargs):
  # print("filtering",q,key)
  has,bef,xq,bej,dic=filterq(q,key)
  if has:
    if not "q" in dic.keys():dic["q"]=Trim(xq)
    q=bef+func(**dic,**kwargs)+bej
    return calledfilter(q,key,func,**kwargs)
  else:
    return q

def hasq(q,key):#returns if q has (<key> or <key></key>),q without it
  s1="<"+key+">"
  i1=q.find(s1)
  if i1>-1:
    pref=q[:i1]
    post=q[i1+len(s1):]
    return True,pref+post

  s2="<"+key+"></"+key+">"
  i2=q.find(s2)
  if i2>-1:
    pref=q[:i2]
    post=q[i2+len(s2):]
    return True,pref+post

  return False,q

def betweens(q,key):
  oq=q
  i1=q.find(key)
  if i1<0:return oq,[]
  bef=q[:i1]
  q=q[i1+len(key):]
  i2=q.find(key)
  if i2<0:return oq,[]
  mid=q[:i2]
  bej=q[i2+len(key):]
  q=bef+bej
  ac,li=betweens(q,key)
  li.append(mid)
  return ac,li
  
def betweencall(q,key,func,**kwargs):
  oq=q
  i1=q.find(key)
  if i1<0:return oq
  bef=q[:i1]
  q=q[i1+len(key):]
  i2=q.find(key)
  if i2<0:return oq
  mid=q[:i2]
  bej=q[i2+len(key):]
  mid=func(mid,**kwargs)
  q=bef+mid+bej
  ac=betweencall(q,key,func,**kwargs)
  return ac
  






