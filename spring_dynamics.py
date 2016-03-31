

"""
This python script was the result of reading this 
excellent tutorial on dynamical systems: http://www.gribblelab.org/compneuro/2_Modelling_Dynamical_Systems.html
"""



from scipy.integrate import odeint

# This computes the acceleration of the spring
# in space
def MassSpring(state,t):
  # unpack the state vector
  x = state[0]
  xd = state[1]

  # these are our constants
  k = 2.5 # Newtons per metre
  m = 1.5 # Kilograms
  g = 9.8 # metres per second

  # compute acceleration xdd
  xdd = ((-k*x)/m) + g

  # return the two state derivatives
  return [xd, xdd]

import numpy
from matplotlib.pyplot import *
state0 = [0.0, 0.0]
t = numpy.arange(0.0, 10.0, 0.1)

state = odeint(MassSpring, state0, t)

plot(t, state)

# Here we compute xdds
plot(t[0:-1], numpy.diff(state[:,1]))

xlabel('TIME (sec)')
ylabel('STATES')
title('Mass-Spring System')
legend(('$x$ (m)', '$\dot{x}$ (m/sec)', '$\ddot{x}$ (m/sec^2)'))
savefig('spring.jpg')
