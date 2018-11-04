import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = Axes3D(fig)
df = pd.read_csv('temp_and_hum.csv')
col = (df['temp']-df['temp'].min())/(df['temp'].max()-df['temp'].min())
x= [5]*int((len(df)/2)+1) + [10]*int((len(df))/2)
y = [28,26,24,22,20,18,16,14,12,10,8,6,4,2,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]
X,Y = np.meshgrid(x,y)
#ax.plot(xs=df['id'], ys=df['temp'], zs = df['humid'], zdir='z', label='ys=temperature, zdir=humidity')
#for pos in range(len(df)):
#ax.scatter(x,y,df['humid'],s=100,cmap=plt.cm.coolwarm)
ax.plot_trisurf(x,y,np.array(df['humid']),cmap=cm.coolwarm,antialiased=True)

ax.set_xbound(0,15)
ax.set_xlabel('x_pos')
ax.set_ylabel('y_pos')
ax.set_zlabel('humidity')
plt.show()
