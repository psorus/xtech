from os.path import isfile,join,isdir
from os import listdir,makedirs,system



def germanise(q):
  q=q.replace("Ã¼","ü")
  q=q.replace("Ã¤","ä")
  q=q.replace("Ã¶","ö")
  q=q.replace("ÃŸ","ß")
  q=q.replace("Ãœ","Ü")
  q=q.replace("ä",'{\\"a}')
  q=q.replace("ö",'{\\"o}')
  q=q.replace("ü",'{\\"u}')
  q=q.replace("Ä",'{\\"A}')
  q=q.replace("Ö",'{\\"O}')
  q=q.replace("Ü",'{\\"U}')
  q=q.replace("ß",'{\\ss}')

  return q


def listfile(q):#list every file in q
  return {join(q,f) for f in listdir(q) if isfile(join(q, f))}
def listfold(q):#list every folder in q
  return {join(q,f) for f in listdir(q) if isdir(join(q, f))}
def listboth(q):
  return listfile(q)|listfold(q)
def advlist(q):
  return [[join(q,f),isfile(join(q,f))] for f in sorted(listdir(q))]
def read(fil):
  if isfile(fil):
    with open(fil,"r") as f:
      return germanise(f.read() )
  return fil
def write(fil,x):
  with open(fil,"w") as f:
    f.write(x)

def assertfolder(q):
  if isdir(q):
    return True
  try:
    makedirs(q)
    return True
  except:
    return False

def run(q):
  system(q)

