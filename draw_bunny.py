#Draw a bunny and a house for the bunny
import matplotlib.pyplot as plt 
import math

#Plot bunny using yellow dots and create another list forming the house for bunny
import GetBunny
z = GetBunny.GetBunnyCloudData()

z_real = [i.real for i in z]
z_image = [i.imag for i in z]

plt.scatter(z_real,z_image,color='yellow')

w = [(0+0j), (0+1.3j), (0.5+1.85j), (1+1.3j), (1+0j),(0+0j), (2+0j), (2+1.3j), (0+1.3j), (1+1.3j), (0.5+1.85j), (2+1.85j), (2+1.3j)]

w_real = [i.real for i in w]
w_image = [i.imag for i in w]

plt.plot(w_real,w_image,color='yellow')

#Plot more lists and do transformations

#scale z and w by 3, plot in red
x_bunny1 = [3*i for i in z_real]
y_bunny1 = [3*i for i in z_image]

x_house1 = [3*i for i in w_real]
y_house1 = [3*i for i in w_image]

plt.scatter(x_bunny1,y_bunny1,color='red')
plt.plot(x_house1,y_house1,color='red')

#translate z and w by 1-2i, plot in blue
x_bunny2 = [i+1 for i in z_real]
y_bunny2 = [i-2 for i in z_image]

x_house2 = [i+1 for i in w_real]
y_house2 = [i-2 for i in w_image]

plt.scatter(x_bunny2,y_bunny2,color='blue')
plt.plot(x_house2,y_house2,color='blue')

#conjugate z and w, plot in green
x_bunny3 = z_real 
y_bunny3 = [-i for i in z_image]

x_house3 = w_real
y_house3 = [-i for i in w_image]

plt.scatter(x_bunny3,y_bunny3,color='green')
plt.plot(x_house3,y_house3,color='green')

#rotate z and w by 135 degrees, plot in black
x_bunny4 = [i*math.cos(3*math.pi/4) - j*math.sin(3*math.pi/4) for i,j in zip( z_real,z_image)]
y_bunny4 = [i*math.sin(3*math.pi/4) + j*math.cos(3*math.pi/4) for i,j in zip(z_real,z_image)]

x_house4 = [i*math.cos(3*math.pi/4) - j*math.sin(3*math.pi/4) for i,j in zip(w_real,w_image)]
y_house4 = [i*math.sin(3*math.pi/4) + j*math.cos(3*math.pi/4) for i,j in zip(w_real,w_image)]
 
plt.scatter(x_bunny4,y_bunny4,color='black')
plt.plot(x_house4,y_house4,color='black')

plt.show()
