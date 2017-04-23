import numpy as np
import matplotlib.pyplot as plt

angles = np.linspace(0,359,360)
size = 18
acc = np.zeros(shape=(180,180))
x = np.linspace(0,size,size)
y = np.zeros(size)
rho = np.zeros(shape=(len(x),len(angles)))
x[15] = 23
x[16] = 35
x[17] = 21
for i in xrange(size):
    y[i] = 2*x[i]


def hough(x,y,angles):
    for i in xrange(180):
        r = x*np.cos(angles[i]*np.pi/180) + y*np.sin(angles[i]*np.pi/180)
        acc[angles[i]][round(r)] +=1
    return x*np.cos(angles*np.pi/180) + y*np.sin(angles*np.pi/180)

for i in xrange(len(x)):
    rho[i] = hough(x[i], y[i], angles)
   

fig = plt.figure()
ax = fig.add_subplot(111)
for i in xrange(len(x)):
    ax.plot(angles,rho[i],color='red')
    
ax.patch.set_facecolor('black')
plt.figure()
plt.scatter(x,y)
plt.grid()
plt.matshow(acc)
plt.show()