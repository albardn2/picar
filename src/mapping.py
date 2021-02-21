import picar_4wd as pcar
from step_three import get_distances_list,servo_angle
import math
import numpy as np
import itertools

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

def distance(first_point, second_point):
    x_squared = math.pow(first_point[0] - second_point[0],2)
    y_squared = math.pow(first_point[1]-second_point[1],2)
    d = math.sqrt(x_squared + y_squared)
    return d

def interpolate(numpy_map,max_distance):
    cooridinates = np.where(numpy_map == 1)
    r = [(cooridinates[0][x],cooridinates[1][x]) for x in range(len(cooridinates[0]))]
    points = list(itertools.combinations(r,2))
    for point in points:
        point_one = point[0]
        point_two = point[1]
        d = distance(point_one, point_two)
        if d < max_distance:
            if point_two[1] == point_one[1]:
                for y in range(min(point_one[0],point_two[0]) + 1,max(point_one[0],point_two[0])):
                    numpy_map[y][point_two[1]] = 1
                continue
            m = (point_two[0] - point_one[0])/(point_two[1] - point_one[1])
            b =  point_one[0] - (m*point_one[1])
            diff = abs(point_one[1] - point_two[1])
            for x in range(min(point_one[1],point_two[1]) + 1,max(point_one[1],point_two[1])):
                y = (m*x) + b
                y_floor = math.floor(y)
                y_ceil = math.ceil(y)
                numpy_map[y_floor][x] = 1
                numpy_map[y_ceil][x] = 1

    return numpy_map


def add_clearance(numpy_map,threshold):
    cooridinates = np.where(numpy_map == 1)
    r = [(cooridinates[0][x],cooridinates[1][x]) for x in range(len(cooridinates[0]))]
    shape_x,shape_y = numpy_map.shape[1],numpy_map.shape[0]
    for point in r:
        y = point[0]
        x = point[1]
        numpy_map[max(y-threshold,0):min(y + threshold+1,shape_y),max(x-threshold,0):min(x+threshold+1,shape_x)] = 1
    return numpy_map

def main_map_function(map_size,clearance = 1,interpolate_value = 1):
    dist_list = get_distances_list(90, -90, 5)
    if dist_list == []:
        dist_list = get_distances_list(90,-90,5)
    c = get_x_y_coordinates(dist_list)
    numpy_map = get_numpy_map(c,map_size)
    numpy_map_interpolated   = interpolate(numpy_map,interpolate_value)
    numpy_map_clearance = add_clearance(numpy_map_interpolated,clearance)

    return (numpy_map_clearance, math.floor(map_size/2))

# main_map_function(201)
# c = get_x_y_coordinates(dist_list)
# np.set_printoptions(threshold=np.inf)
# r = get_numpy_map(c,201)
# print(r)
# print(dist_list)
#

# x  = get_x_y_coordinates(dist_list)
#
# x_array = []
# y_array = []
# for i in x:
#     if i[2] == 0:
#         continue
#     x_array.append(i[0])
#     y_array.append(i[1])
#
# import matplotlib.pyplot as plt
# X = np.array(x_array)
# Y = np.array(y_array)
# # Plotting point using sactter method
# plt.scatter(X,Y)
# plt.show()
