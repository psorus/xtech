import numpy as np
import os
import os.path

from rechtschreib import correct

folder="../../write/data/"

def fixstring(qq,bef=None):

  # print("fixing",qq)
  
  intags=False
  inhash=False
  ac=""
  ret=""
  stopat=[".","(",")",">","\n"]
  
  lq=len(qq)
  
  for ii,zw in enumerate(qq):
    basei=[intags,inhash]
    if zw=="<":intags=True
    if zw=="#" and inhash==False:inhash=True
    

    ac+=zw
    
    if zw==">":intags=False
    if zw=="#" and inhash==True:inhash=False

    if len(ret)>5:
      if ret[-6:]=="<note ":
        intags=False


    if zw in stopat or zw==">" or (zw=="#" and inhash==False) or (ii==lq-1):
      if len(ac)==0:continue
      if len(ac)<5 or intags or inhash or zw==">" or (zw=="#" and not inhash):
        ret+=ac
        ac=""
        continue
      # print(intags,inhash,zw)
      ac=correct(ac,bef)
      # print(ac)
      # exit()
      ret+=ac
      ac=""
  return ret


def noignorefix2(q,befstr=None):
  fix1="#"
  fix2="#"
  ret=""
  while fix1 in q:
    i1=q.find(fix1)
    if i1<0:continue
    bef=q[:i1]
    q=q[i1:]
    i2=q.find(fix2)
    if i2<0:continue
    mid=q[:i2+len(fix2)]
    post=q[i2+len(fix2):]
    
    
    # print("bef",bef)
    # print("mid",mid)
    # print("post",post)
    
    
    
    bef=fixstring(bef,befstr)
    
    # print("bef2",bef)
    # exit()
    
    ret+=bef
    ret+=mid

    
    q=post
  if len(q)>0:ret+=fixstring(q,befstr)
  
  # exit()
  
  return ret

def noignorefix(q,befstr=None):
  fix1="<ignore>"
  fix2="</ignore>"
  ret=""
  while fix1 in q:
    i1=q.find(fix1)
    if i1<0:continue
    bef=q[:i1]
    q=q[i1:]
    i2=q.find(fix2)
    if i2<0:continue
    mid=q[:i2+len(fix2)]
    post=q[i2+len(fix2):]
    
    
    # print("bef",bef)
    # print("mid",mid)
    # print("post",post)
    
    
    
    bef=noignorefix2(bef,befstr)
    
    # print("bef2",bef)
    # exit()
    
    ret+=bef
    ret+=mid

    
    q=post
  if len(q)>0:ret+=noignorefix2(q,befstr)
  
  # exit()
  
  return ret
    

def correctfile(q):
  print("correcting file",q)
  with open(q,"r") as f:
    qq=f.read()
  
  ret=noignorefix(qq,"working on "+q)
    
  with open(q,"w") as f:
    f.write(ret)
  
  


for dirpath, dirnames, filenames in os.walk(folder):
  for filename in [f for f in filenames]:
    correctfile(dirpath+"/"+filename)
