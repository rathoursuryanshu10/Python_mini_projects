import matplotlib.pyplot as plt
import numpy as np
def quadratic(x,a,b,c):
    return a*x**2+ b*x + c
x=np.linspace(-10,10,1000)
y=quadratic(x,4,2,1)
fig,ax=plt.subplots()
ax.plot(x,y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Quadratic Graph equation')


plt.show()
