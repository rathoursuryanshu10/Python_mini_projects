from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


Image.open('Vinod.jpg')
image=mpimg.imread('vinod.jpg')
w,h,d=tuple(image.shape)
pixels=np.reshape(image,(w*h,d))
from sklearn.cluster import KMeans
n_colors=10
model=KMeans(n_clusters=n_colors,random_state=42).fit(pixels)
palette=np.unit8(model.cluster_centers_)
plt.imshow([palette])
plt.show()
