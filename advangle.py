import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

# plt.style.use("dark_background")

f1,f2=16,9
zom=2
f1/=zom
f2/=zom

f=f1/f2



mulf=1.7

r1=mulf*f
r2=mulf

# toa=patches.Ellipse((0,0),r1,r2,fill=False)
alpha=1.5
alpha2=alpha
alpha2=(alpha2-1)*0.4+1


def pointfromphi(phi,rmul=1.0):
  if type(phi) is int:
    phi/=180
    phi*=np.pi
  return np.sin(phi)*rmul*r1/2,np.cos(phi)*rmul*r2/2
def connect(p1,p2,lw=2,color="black",zorder=0):
  # print("connecting",p1,p2)
  plt.plot([p1[0],p2[0]],[p1[1],p2[1]],color=color,lw=lw,zorder=zorder)
def frontconnect(p1,p2,lw=2,color="black"):
  connect(p1,p2,lw=lw,color=color,zorder=100)
def diff(p1,p2):
  return [pp2-pp1 for pp1,pp2 in zip(p1,p2)]
def addcon(phi,phi2=None,color="black"):
  if phi2 is None:phi2=phi
  p1=pointfromphi(phi)
  p2=pointfromphi(phi2,10)
  connect(p1,p2,lw=None,color=color)
def treecon(phi,delta=3,color="black"):
  addcon(phi-delta,phi,color=color)
  addcon(phi,color=color)
  addcon(phi+delta,phi,color=color)
def basepatch(color="black",fill=True):
  lw=None
  if not fill:lw=2
  toa=patches.FancyBboxPatch((-r1/2/alpha2,-r2/2/alpha),r1/alpha2,r2/alpha,fill=fill,color=color,boxstyle="round",zorder=1,lw=lw)
  ax.add_patch(toa)
def byangles(angles,colors,saveas=None,title=""):

  print("using angles",angles)


  plt.close()
  


  
  
  
  fig=plt.figure(figsize=(2*f1,2*f2))
  global ax
  ax=plt.Axes(fig,[0.,0.,1.,1.],xlim=(-f,f),ylim=(-1,1))
  ax.clear()
  ax.set_xlim([-f,f])
  plt.axis("off")
  ax.set_ylim([-1,1])
  ax.set_axis_off()
  fig.add_axes(ax)
  
  

  x=[treecon(q,color=c) for q,c in zip(angles,colors)]
  # treecon(45)
  # treecon(90)




  # basepatch()
  basepatch("white")
  basepatch("black",False)

  alpha3=1*0.95#.03185
  titley=0.6
  titley2=5/6.0
  frontconnect([-alpha3*r1/2,titley],[alpha3*r1/2,titley])

  # plt.text(#,va="center",ha="center"
  plt.text(-np.sqrt(alpha3)*r1/2+0.1,titley+(titley2-titley)*0.2,title,rotation=0,fontsize=120/zom)


  if not saveas is None:plt.savefig(saveas+".png",format="png")
  if not saveas is None:plt.savefig(saveas+".pdf",format="pdf")


if __name__=="__main__":
  byangles([0,90,180,270],["black" for i in range(4)],None)
  plt.show()
# byangles([90,180,270],"page1")
# byangles([180,270],"page2")
# byangles([270,0],"page3")
# byangles([0,90],"page4")


