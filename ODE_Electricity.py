import numpy as np
from scipy.integrate import odeint
mag = lambda r: np.sqrt(np.sum(np.power(r, 2)))
k = 8.99*10**9

def g(r, t, q1, q2, m1, m2):
 r = r.reshape((4,2))
 r1 = r[0]
 dr1dt = r[1]

 r2 = r[2]
 dr2dt= r[3]

 F = q1*q2/mag(r2-r1)**2

 dy_dt = [
     dr1dt,
     (F/m1)*(r2-r1),
     dr2dt,
     (F/m2)*(r1-r2)
  ]
 return np.array(dy_dt).reshape(8)

t = np.linspace(0, 10, num=1000)

r1i = np.array([1.,2.])
dr1dti = np.array([2,.4])

r2i = np.array([3.,4.])
dr2dti = np.array([0.3, -2.])

y0 = np.array([r1i, dr1dti, r2i, dr2dti]).reshape(8)

y = odeint(g, y0, t, args=(-1,1,1,1)).reshape(1000,4,2)

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ys1 = y[:,0,1]
xs1 = y[:,0,0]

xs2 = y[:,2,0]
ys2 = y[:,2,1]

print xs1[:1]
ax.plot(xs1[:1], ys1[:1], t[:1],'bv')
ax.plot(xs1[-1:], ys1[-1:], t[-1:], 'rv')
ax.plot(xs2[:1], ys2[:1], t[:1], 'bv') 
ax.plot(xs2[-1:], ys2[-1:], t[-1:], 'rv') 

ax.plot(xs1, ys1, t)
ax.plot(xs2, ys2, t)

plt.show()
