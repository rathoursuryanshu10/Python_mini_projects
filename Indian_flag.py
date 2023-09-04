import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch
 
a=patch.Rectangle((0,1), width=9, height=2,facecolor='#138808', edgecolor='grey')
b=patch.Rectangle((0,3), width=9, height=2,facecolor='#ffffff', edgecolor='grey')
c=patch.Rectangle((0,5), width=9, height=2,facecolor='#FF6103', edgecolor='grey')
m,n=py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)

radius=0.8
py.plot(4.5,4,marker='o',markerfacecolor='#000080',markersize=9.5)
chakra=py.Circle((4.5,4),radius,color='#000080',fill=False,linewidth=7)
n.add_artist(chakra)
for i in range(0,24):
    p=4.5 + radius/2 * np.cos(np.pi*i/9 + np.pi/48)
    q=4.5 + radius/2 * np.cos(np.pi*i/9 - np.pi/48)
    r=4 + radius/2 * np.sin(np.pi*i/9 + np.pi/48)
    s=4 + radius/2 * np.sin(np.pi*i/9 - np.pi/48)
    t=4.5  + radius * np.cos(np.pi*i/9)
    u=4 + radius * np.sin(np.pi*i/9)
    n.add_patch(patch.Polygon([[4.5,4],[p,r],[t,u],[q,s]],fill=True,closed=True,color='#000080'))
py.axis('equal')
py.show()
