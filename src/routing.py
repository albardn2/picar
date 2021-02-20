
from algorithms_interface import *
from math import floor
import numpy as np



def get_navigation_instructions(path):
    directions = []
    i = 0
    while i < len(path)-1:
        value = 0
        direction = None
        while (i < len(path)-1) and (path[i+1][0]- path[i][0] != 0):
            direction = "V"
            diff = path[i+1][0]- path[i][0]
            value += diff
            i+=1
        if direction == "V":
            directions.append((direction,value))
            continue
        while (i < len(path)-1) and (path[i+1][1]- path[i][1] != 0):
            direction = "H"
            diff = path[i+1][1]- path[i][1]
            value += diff
            i+=1

        directions.append((direction,value))
    return directions

def route(numpy_map,start = None,goal=None):
    center_x = floor(numpy_map.shape[1]/2)
    goal[1] = goal[1] + center_x
    walls = np.where(numpy_map == 1)
    grid = GridWithWeights(numpy_map.shape[1], numpy_map.shape[0])
    grid.walls = [(i,j) for i,j in zip(walls[0],walls[1])]
    start, end = (0,center_x), goal
    came_from, cost_so_far = a_star_search(grid, start, goal)

    draw_grid(grid, point_to=came_from, start=start, goal=goal)
    print()
    draw_grid(grid, path=reconstruct_path(came_from, start=start, goal=goal))

    path =  reconstruct_path(came_from, start=start, goal=goal)
    navigation = get_navigation_instructions(path)

    return navigation
