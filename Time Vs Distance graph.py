
# coding: utf-8

# In[ ]:

from numpy import *
from matplotlib import pyplot as plt
g = 9.8
vO = eval(input("Input initial velocity, m/s \n"))
t1 = eval(input("Input time range, seconds \n"))
a = eval(input("Input accelaration, m/s**2 \n"))
t = np.linspace(0, t1, 50)
distance = vO*t + 0.5*a*t**2
velocity = vO + a*t
plt.plot(2)
plot2, = plt.plot(t, distance, label = 'Distance')
plot3, = plt.plot(t, velocity, label = 'Velocity')
plt.xlabel('Time s')
plt.ylabel('Distance m')
plt.title('Time Vs Distance/Velocity graph')
plt.show()


# In[ ]:



