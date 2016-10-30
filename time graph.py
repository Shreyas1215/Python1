
# coding: utf-8

# In[ ]:

from numpy import *
from matplotlib.pyplot import *

def f(t):
    return t**2*exp(-t**2)

t = linspace(0, 3, 51)
y = zeros(len(t))
for i in range(len(t)):
    y[i] = f(t[i])
    
plot(t, y)
show()
    


# In[ ]:



