import picar_4wd as pcar
from step_three import get_distances_list,servo_angle
import math
import numpy as np

 
dist_list = get_distances_list(90, -90, 5)
if dist_list == []:
    dist_list = get_distances_list(90,-90,5)



def get_x_y_coordinates(distance_list):
    coordinates_list = []
    for d,a in distance_list:
        a_rad = a*math.pi/180
        x_coordinate = d*math.sin(a_rad)
        y_coordinate = d*math.cos(a_rad)
        coordinates_list.append((x_coordinate,y_coordinate,d,a))    
    return coordinates_list
                                                                                                                 




def get_numpy_map(coordinates_list,length):
    n = np.zeros((length,length))
    for c in coordinates_list:
        if c[2] < 0:
            continue
        x_dist = math.floor(length/2) + c[0]
        x = math.floor(x_dist) if c[0] > 0  else math.ceil(x_dist)
        y = math.floor(c[1])
        if x_dist >= length or y >= length or x_dist < 0:
            continue
        n[y,x] = 1
    return n



# c = get_x_y_coordinates(dist_list)
# np.set_printoptions(threshold=np.inf)
# r = get_numpy_map(c,201)
# print(r)
# print(dist_list) 
#

x  = get_x_y_coordinates(dist_list)

x_array = []
y_array = []
for i in x:
    if i[2] == 0:
        continue
    x_array.append(i[0])
    y_array.append(i[1])

import matplotlib.pyplot as plt
X = np.array(x_array)
Y = np.array(y_array)
# Plotting point using sactter method
plt.scatter(X,Y)
plt.show()