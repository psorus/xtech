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
  connect(p1,p2,lw=None,color=color,zorder=-1000)
def treecon(phi,delta=3,color="black"):
  addcon(phi-delta,phi,color=color)
  addcon(phi,color=color)
  addcon(phi+delta,phi,color=color)
def addpatch(x,y,r,tex,node,color="black",fill=True):
  
  # print("radius",r)
  
  # exit()

  lw=None
  if not fill:lw=2
  # plt.plot([x],[y],"o",color=color)
  
  # return
  # toa=patches.FancyBboxPatch((-r1/2/alpha2,-r2/2/alpha),r1/alpha2,r2/alpha,fill=fill,color=color,boxstyle="round",zorder=1,lw=lw)
  toa=patches.FancyBboxPatch((x-r*0.5,y-r*0.5),r,r,fill=fill,color=color,boxstyle="round",zorder=1,lw=lw)
  ax.add_patch(toa)
  
  
  if not tex is None:
    # toa2=patches.Rectangle((x-r,y-r),2*r,2*r,color="grey")
    
# xy : float, float The lower left corner of the box.  width : float The width of the box.  height : float The 
    
    q=plt.text(x,y, tex[:10],
           ha="center", va="center",fontsize=200/node["looplen"]
           # bbox={"xy":(x-r,y-r),"width":2*r,"height":2*r}
  #         bbox=dict(boxstyle="square",
  #                   ec=(1., 0.5, 0.5),
  #                   fc=(1., 0.8, 0.8),
  #                   )
           )
           
    # print(dir(q))
    
    # qq=q.get_size()
    # qq=q.properties()
    
    # print(dir(qq))
    # print(qq)
    
    # exit()
    
    # ax.add_patch(toa2)
  
  
def genoverlay(nodes,saveas=None):

  print("using nodes",nodes)
  
  
  ret=[]
  
  
  # phis=[node["phi"] for node in nodes]
  
  # print(phis)
  
  # exit()
  


  plt.close()
  
  nodesize=1


  minx=0.0
  maxx=0.0
  miny=0.0
  maxy=0.0
  
  
  for node in nodes:
    nodesize=100/node["looplen"]
    phi=node["phi"]*np.pi/180
    x=node["loopx"]+np.cos(phi)*node["loopr"]*node["looplen"]
    y=node["loopy"]+np.sin(phi)*node["loopr"]*node["looplen"]
    if x<minx:minx=x#-nodesize
    if x>maxx:maxx=x#+nodesize
    if y<miny:miny=y#-nodesize
    if y>maxy:maxy=y#+nodesize
    
    node["x"]=x
    node["y"]=y
    

  minx-=nodesize
  miny-=nodesize
  maxx+=nodesize#*1.5
  maxy+=nodesize#*1.5

  nodesize/=2

  
  fig=plt.figure(figsize=(2*f1,2*f2))
  global ax
  ax=plt.Axes(fig,[0.,0.,1.,1.],xlim=(minx,maxx),ylim=(miny,maxy))
  ax.clear()
  ax.set_xlim([minx,maxx])
  plt.axis("off")
  ax.set_ylim([miny,maxy])
  ax.set_axis_off()
  fig.add_axes(ax)
  
  
  
  # fig=plt.figure(figsize=(2*f1,2*f2))
  # global ax
  # ax=plt.Axes(fig,[0.,0.,30.,30.],xlim=(minx,maxx),ylim=(miny,maxy))
  # ax=plt.axes()#,xlim=(-f,f),ylim=(-1,1))
  # # ax.clear()
  # ax.set_xlim([minx,maxx])
  # plt.axis("off")
  # ax.set_ylim([miny,maxy])
  # ax.set_axis_off()
  # fig.add_axes(ax)
  
  

  # x=[treecon(q,color=c) for q,c in zip(angles,colors)]
  # treecon(45)
  # treecon(90)



  # basepatch()
  # basepatch("white")
  # basepatch("black",False)
  

  
  for node in nodes:
    x=node["x"]
    y=node["y"]
    addpatch(x,y,nodesize,None,node,"white",True)
    addpatch(x,y,nodesize,node["title"],node,"black",False)
    ret.append([node["id"],((x-nodesize-minx)/(0.001+maxx-minx)),((y-nodesize-miny)/(0.001+maxy-miny)),((x+nodesize-minx)/(0.001+maxx-minx)),((y+nodesize-miny)/(0.001+maxy-miny))])
    
  # addpatch(4,4,nodesize,None,nodes[-1],"white",True)
  # addpatch(4,4,nodesize,"test",node,"black",False)
    
    
  for node in nodes:
    i1=node["id"]
    for c in node["c"]:
      i2=c["q"]
      
      # connect([nodes[i1]["x"],nodes[i2]["x"]],[nodes[i1]["y"],nodes[i2]["y"]])
      connect([nodes[i1]["x"],nodes[i1]["y"]],[nodes[i2]["x"],nodes[i2]["y"]])
      
      # print([nodes[i1]["x"],nodes[i2]["x"]],[nodes[i1]["y"],nodes[i2]["y"]])
      
      # break
    # break
      
  # frontconnect([-10,10],[10,10],color="red")
  # frontconnect([4,4],[nodes],color="red")


  alpha3=1*0.95#.03185
  titley=0.6
  titley2=5/6.0
  # frontconnect([-alpha3*r1/2,titley],[alpha3*r1/2,titley])

  # plt.text(#,va="center",ha="center"
  # plt.text(-np.sqrt(alpha3)*r1/2+0.1,titley+(titley2-titley)*0.2,title,rotation=0,fontsize=120/zom)


  if not saveas is None:plt.savefig(saveas+".png",format="png")
  if not saveas is None:plt.savefig(saveas+".pdf",format="pdf")


# byangles([0,90,180,270],"page0")
# byangles([90,180,270],"page1")
# byangles([180,270],"page2")
# byangles([270,0],"page3")
# byangles([0,90],"page4")

  # plt.show()

  return ret


if __name__=="__main__":
  import json
  with open("debug.txt","r") as fil:
    q=json.loads(fil.read())
  
  poses=genoverlay(q)
  
  print(poses)
  
  plt.show()
  




