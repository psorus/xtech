import numpy as np
import os
import os.path
import json

from rechtschreib import correct

folder="../../write/data/"


def iscapital(w):
  o=ord(w)
  if o>64 and o<91:return True
  return False

def shouldbelow(w):
  if iscapital(str(w[0]).upper()) and not iscapital(w[0]):return True
  try:
    i=int(w[0])
    return True
  except:pass
  if w[0]=="#":return False
  return False

def anafile(q):
  print("analysing file",q)
  with open(q,"r") as f:
    qq=f.read()
  
  ret=[]
  
  for i in range(2,len(qq)-1):
    ac=qq[i]
    if not iscapital(ac):continue
    acm1=qq[i-1]
    if iscapital(acm1):continue#yes i know redundant
    if not (acm1==" " or acm1=="\n"):continue
    acp1=qq[i+1]
    if iscapital(acp1):continue
    ret.append(qq[i-2:i+2])
    
  
  return ret

  


def capitalfile(q,mp):
  print("capitaling file",q)
  with open(q,"r") as f:
    qq=f.read()
  
  for key in mp.keys():
    qq=qq.replace(key,mp[key])
  
    
  with open(q,"w") as f:
    f.write(qq)
  
  
l=[]

for dirpath, dirnames, filenames in os.walk(folder):
  for filename in [f for f in filenames]:
    for ll in anafile(dirpath+"/"+filename):
      l.append(ll)

s=set(l)

s=[q for q in s if shouldbelow(q)]
s=set(s)

def lowered(q):
  return q[:-2]+str(q[-2]).lower()+str(q[-1])
  
mp={ss:lowered(ss) for ss in s}

print("working with")
print(json.dumps(mp,indent=2))


for dirpath, dirnames, filenames in os.walk(folder):
  for filename in [f for f in filenames]:
    capitalfile(dirpath+"/"+filename,mp=mp)




exit()



ss=[q[0] for q in s if not iscapital(str(q[0]).upper())]

print(set(ss))

exit()

print(s)

