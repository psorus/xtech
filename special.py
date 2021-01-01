import numpy as np

from strg import *
from foldery import *







def special(**q):
  print("called special with",q)
  m=q["m"]
  typ=Trim(q["q"]).lower()
  if len(typ)<1:typ=Trim(q["q"].lower())

  if typ=="toc":
    title=""
    if "title" in q.keys():
      title=q["title"]
    elif len(q["q"])>0:
      title=q["q"]
    else:
      title="Inhaltsverzeichnis"
    return read("pattern/toc.txt").replace("###title###",title)
  if typ=="titlepage":
    title=""
    if "title" in q.keys():title=q["title"]
    subtitle=""
    if "subtitle" in q.keys():subtitle=q["subtitle"]
    name="Simon Klüttermann"
    if "name" in q.keys():name=q["name"]
    department="Insitute for theoretical Particle Physics and Cosmology"
    if "department" in q.keys():department=q["department"]
    university="RWTH Aachen"
    if "university" in q.keys():university=q["university"]
    country="Germany"
    if "country" in q.keys():country=q["country"]
    
    return read("pattern/titlepage.txt").replace("###title###",title).replace("###subtitle###",subtitle).replace("###name###",name).replace("###department###",department).replace("###university###",university).replace("###country###",country)
    
  if typ=="ptoc":
    return read("pattern/ptoc.txt")
  if typ=="ptitle":
    return read("pattern/ptitle.txt")
  if typ=="appendix":
    return read("pattern/appendix.txt")
  if typ=="colordef":
    color=q["c"]
    colornam=q["n"]
    return read("pattern/colordef.txt").replace("###color###",color).replace("###name###",colornam)

  return read(f"pattern/{typ}.txt")

  return ""
