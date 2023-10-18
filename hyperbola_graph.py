import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-20,20,500)
y1=np.sqrt(x**2 -1)
y2=-np.sqrt(x**2 - 1)

fig,ax=plt.subplots()
ax.plot(x,y1,color='blue' ,label='y= +sqrt(x^2-1)')
ax.plot(x,y2,color='red' ,label='y= +sqrt(x^2-1)')

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Hyperbola Graph')
ax.legend()
plt.show()
