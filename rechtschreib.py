from loadsite import *

import os


#disabledRules=WHITESPACE_RULE,FRENCH_WHITESPACE&allowIncompleteResults=true&enableHiddenRules=true&text=Halo&language=de-DE

def gendic(q):
  return {"disabledRules":"WHITESPACE_RULE,FRENCH_WHITESPACE","allowIncompleteResults":"true","enableHiddenRules":"true","text":q,"language":"en-US"}

def check(q):
  site="https://api.languagetool.org/v2/check"
  return json.loads(loadsite(site,gendic(q)))

def intp(q):
  # print("intp:::",[ord(qq) for qq in q])
  if len(q)==0:return 0
  if q=="\n":return q
  return int(q)

def isint(q):
  try:
    qq=int(q)
    return True
  except:
    return False

def correct(q,pref=None):
  matches=check(q)["matches"]
  for match in matches:
    if len(match["replacements"])==0:continue
    os.system("clear")
    if not pref is None:print(pref)
    ac=q
    oo=match["offset"]
    le=match["length"]
    ac=ac[:oo]+ac[oo:oo+le].upper()+ac[oo+le:]
    print(ac)
    
    for i,rep in enumerate(match["replacements"]):
      print(i,rep["value"])
    
    try:
    # for i in range(1):
      ii=input("Choose a replacement: ")
      if ii=="#":ii=int("#")
      if len(ii)==0:ii=0
      
      if isint(ii):
        q=q[:oo]+match["replacements"][ii]["value"]+q[oo+le:]
      else:
        q=q[:oo]+ii+q[oo+le:]
      return correct(q,pref=None)
    except:
      print("skipping this")
      continue
    
  return q

if __name__=="__main__":

  print(correct("Helo World"))