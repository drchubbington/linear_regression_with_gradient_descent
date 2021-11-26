import matplotlib.pyplot as plt
import numpy as np
import random

#prepare data
#modeled line: y=2.5x+20
random.seed(11)
data=[]
for i in range(100):
    data.append([i, 2.5*i+20+random.gauss(0, 30)])

x_coords = []
y_coords = []
for coord in data:
    x_coords.append(coord[0])
    y_coords.append(coord[1])
    
plt.scatter(x_coords, y_coords)

#train model
#only 100 epoochs since data is 100 pts
m=0
b=0
lr=.01/(data[-1][1])
for i in range(100):
    error=0
    for point in data:
        guess = m*point[0]+b
        error = point[1]-guess
        m += error*point[0]*lr
        b += error*lr
        print("x:", point[0], "y:", point[1], "error:", error, "m:", m, "b:", b)

#display results
x = np.linspace(min(x_coords),max(x_coords),100)
y = m*x+b
plt.plot(x, y, '-r')
plt.scatter(x_coords, y_coords)
print ("y = ", m, "x +", b)
mean = 0
error = 0
variance = 0
for point in data:
    guess = m*point[0]+b
    mean += point[0]/len(data)
    error += (point[1]-guess)**2
for point in data:
    variance += (point[1]-mean)**2
    
print("R^2:", 1-(error/variance))
