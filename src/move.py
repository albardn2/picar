import picar_4wd as pcar
import time
import math

pcar.start_speed_thread()

def move_cm_forward(distance):
    t = time.time()
    total_dist = 0
    pcar.forward(50)
    previous_time = t
    while total_dist < distance:
        print(total_dist)
        current_time = time.time()
        total_dist += pcar.speed_val() * (current_time - previous_time)
        previous_time = current_time
    pcar.stop()
    return total_dist

def car_orientation(orientation):
    distance = 2*13*math.pi/4
    t = time.time()
    total_dist = 0
    if orientation == "left":
        pcar.turn_left(50)
    elif orientation == "right":
        pcar.turn_right(50)
    elif orientation == "back":
        pcar.turn_left(50)
        distance *=2
    previous_time = t
    while total_dist < distance:
        print(total_dist)
        current_time = time.time()
        total_dist += pcar.speed_val() * (current_time - previous_time)
        previous_time = current_time
    pcar.stop()
    return total_dist

# time.sleep(5)
# move_cm_forward(300)
# car_orientation("left")
# move_cm_forward(30)
