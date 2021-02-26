from mapping import main_map_function,distance
from move import move_cm_forward, car_orientation
import picar_4wd as pcar
from routing import route
import settings
import matplotlib.pyplot as plt
import time
import threading
from detect_picamera import main
# FIND SERVO MEASUREMENTS
# FIND ENGINE SLIPPAGE
# RERUN MAPPING AND ROUTING AFTER THRESHOLD
# TRACK LOCATION
# GLOBAL ORIENATION,
settings.init()

tf_object_detection = threading.Thread(target=main, name="object_detection_thread")
tf_object_detection.start()

# Final_destination = (30,0) # (y,x) from origin


# main_route((100,100))
def drive(navigation,multiplyer):
    # current_orientation = "Forward"
    for nav in navigation:
        direction = nav[0]
        distance  = nav[1] * multiplyer
        print("DISTANCE {}".format(distance))
        if distance > 0 and direction == "H":
            car_orientation(settings.global_orientation,"L")
            settings.global_orientation = "L"
            move_cm_forward(distance)
        elif distance < 0 and direction == "H":
            car_orientation(settings.global_orientation,"R")
            settings.global_orientation = "R"
            move_cm_forward(distance)
        elif distance > 0 and direction == "V":
            car_orientation(settings.global_orientation,"F")
            settings.global_orientation = "F"
            move_cm_forward(distance)
        elif distance < 0 and direction == "V":
            car_orientation(settings.global_orientation,"B")
            settings.global_orientation = "B"
            move_cm_forward(distance)

def dist_less_than_1_m(nav,threshold):
    dist_v = 0
    dist_h = 0
    total_distance = 0
    i = 0
    for n in nav:
        if n[0] == "V":
            dist_v += n[1]
        elif n[0] == "H":
            dist_h += n[1]

        total_distance = distance((0,0),(dist_v,dist_h))
        if total_distance > threshold:
            return (nav[0:i+1],dist_v,dist_h)
        i+=1
    return (nav,dist_v,dist_h)

def draw_path_on_array(numpy_map,path):
    for p in path:
        numpy_map[p] = 0.5
    return numpy_map
def main_route(final_destination = None):

    while final_destination != (0,0):
        print(final_destination)
        numpy_map,center = main_map_function(max(final_destination) * 2 + 1,clearance=3,interpolate_value=6)
        nav,path = route(numpy_map,goal=final_destination)
        print("nav",nav)
        plt.imsave("path-{}.png".format(final_destination[1]),draw_path_on_array(numpy_map,path))
#         plt.show()
        final_nav,dist_v,dist_h = dist_less_than_1_m(nav,30)
        
        print("final nav",final_nav)
        drive(final_nav,3)
        final_destination = (final_destination[0]-dist_v,final_destination[1]-dist_h)
        if settings.global_orientation == "R":
            final_destination = (-final_destination[1],final_destination[0])
        elif settings.global_orientation == "L":
            final_destination  = (final_destination[1],-final_destination[0])
        elif settings.global_orientation == "B":
            final_destination  = (-final_destination[0],-final_destination[1])

 

    # 
    # nav = main_route(Final_destination)
    # print(nav)
# print(dist_less_than_1_m([('H', 4)],30))
# settings.global_orientation = "F"
# drive(nav)
# x = move_cm_forward(25) [('V', 48), ('H', 4), ('V', 1), ('H', 17), ('V', 5), ('H', 5), ('V', 2), ('H', -5), ('V', 5), ('H', -21), ('V', 139)]
time.sleep(5)
main_route((100,0))
# drive([('V', 2`0)],3)