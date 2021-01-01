import numpy as np
import os
import os.path


folder="../../write/data/"

def coukom(q):
  return len([qq for qq in q if qq==","])

def remignore(q):
  t1="<ignore>"
  t2="</ignore>"
  if t1 in q:
    i1=q.find(t1)
    i2=q.find(t2)
    if i2==-1:return q
    q=q[:i1+len(t1)]+q[i2+len(t2):]
    return remignore(q)
  return q


def correctfile(q):
  print("correcting file",q)
  with open(q,"r") as f:
    qq=f.read()
  
  qq=remignore(qq)
  
  intags=False
  inhash=False
  ac=""
  ret=0
  stopat=[".",">","\n",":"]
  
  for zw in qq:
    basei=[intags,inhash]
    if zw=="<":intags=True
    if zw=="#" and inhash==False:inhash=True
    

    ac+=zw
    
    if zw==">":intags=False
    if zw=="#" and inhash==True:inhash=False

    # if len(ret)>5:
      # if ret[-6:]=="<note ":
        # intags=False


    if zw in stopat or zw==">" or (zw=="#" and inhash==False):
      if len(ac)==0:continue
      if len(ac)<5 or intags or inhash or zw==">" or (zw=="#" and not inhash):
        ac=""
        continue
      # print(intags,inhash,zw)
      if len(ac)>400 or coukom(ac)>4:
        print("!!!")
        print("found horror sentence in",q)
        print(ac)
        print("!!!")
        # os.system("pause")
        ret+=1
      # print("!",ac,"!")
      # print(ac)
      # exit()
      # ret+=ac
      ac=""
  return ret

  

totalc=0
for dirpath, dirnames, filenames in os.walk(folder):
  for filename in [f for f in filenames]:
    totalc+=correctfile(dirpath+"/"+filename)

print("in total:",totalc)

