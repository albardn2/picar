from mapping import main_map_function,distance
from move import move_cm_forward, car_orientation
import picar_4wd as pcar
from routing import route
import settings
import matplotlib.pyplot as plt
# FIND SERVO MEASUREMENTS
# FIND ENGINE SLIPPAGE
# RERUN MAPPING AND ROUTING AFTER THRESHOLD
# TRACK LOCATION
# GLOBAL ORIENATION,
settings.init()

Final_destination = (30,0) # (y,x) from origin


# main_route((100,100))
def drive(navigation):
    # current_orientation = "Forward"
    for nav in navigation:
        direction = nav[0]
        distance  = nav[1] * 5
        if distance > 0 and direction == "H":
            car_orientation(settings.global_orientation,"L")
            settings.global_orientation = "L"
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


def main_route(final_destination = None):

    while final_destination != (0,0):
        numpy_map = main_map_function(max(final_destination) * 2 + 1,clearance=3,interpolate_value=2)
        # plt.imshow(numpy_map[0])
        # plt.show()
        nav = route(numpy_map[0],goal=Final_destination)
        final_nav,dist_v,dist_h = dist_less_than_1_m(nav,21)
        drive(final_nav)
        final_destination = (final_destination[0]-dist_v,final_destination[1]-dist_h)
        if settings.global_orientation == "R":
            final_destination = (-final_destination[1],final_destination[0])
        elif settings.global_orientation == "L":
            final_destination  = (final_destination[1],-final_destination[0])
        elif settings.global_orientation == "B":
            final_destination  = (-final_destination[0],-final_destination[1])

        # return nav




nav = main_route(Final_destination)
print(nav)
print(dist_less_than_1_m(nav,21))
settings.global_orientation = "F"
# drive(nav)
# x = move_cm_forward(25) [('V', 48), ('H', 4), ('V', 1), ('H', 17), ('V', 5), ('H', 5), ('V', 2), ('H', -5), ('V', 5), ('H', -21), ('V', 139)]
