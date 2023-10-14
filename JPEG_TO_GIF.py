import imageio
filenames=['download1.jpeg', 'download2.jpeg','download3.jpeg','download4.jpeg']
images=[]
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('RS.gif', images,'GIF',duration=2)
