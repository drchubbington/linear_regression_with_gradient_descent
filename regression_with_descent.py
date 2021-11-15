#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy as np

data = [
    [1, 2.5],
    [4, 7],
    [8, 14],
    [-3, -2],
    [6, 9],
    [7, 17],
    [34, 65],
    [20, 40],
    [-10, -15],
    [-30, -58]
]
x_coords = []
y_coords = []
for coord in data:
    x_coords.append(coord[0])
    y_coords.append(coord[1])
    
plt.scatter(x_coords, y_coords)


# In[21]:


m=1
b=0
lr=.01
for i in range(1000):
    for point in data:
        guess = m*point[0]+b
        error = point[1]-guess
        print(i, error)
        m += error*point[0]*lr
        b += error*lr

x = np.linspace(-30,35,100)
y = 2*x+1
plt.plot(x, y, '-r')
plt.scatter(x_coords, y_coords)
print ("y = ", m, "x +", b)


# In[ ]:




