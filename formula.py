from sympy.parsing.sympy_parser import parse_expr as parse
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application
from sympy import latex

from strg import hasq

from sympy import sympify

def gotec(q,mode="equation"):
#def hasq(q,key):#returns if q has (<key> or <key></key>),q without it

  shallhide,q=hasq(q,"h")
  shallhide2,q=hasq(q,"hide")
  modus,q=hasq(q,"empty")
  if modus:mode="plain"
  if shallhide or shallhide2:
    mode="equation*"
  trafo=(standard_transformations+(implicit_multiplication_application,))
  #p=parse(q,evaluate=0)
  #p=parse(q,transformations=trafo,evaluate=False)

  #print("parsing",q)
  #exit()

  p=sympify(q,evaluate=False)
  #print("parsed",p)
  return latex(p,mul_symbol="dot",mode=mode)

def gostec(q):
  return gotec(q,mode="inline")

