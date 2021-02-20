from mapping import main_map_function
from move import move_cm_forward, car_orientation
import picar_4wd as pcar
from routing import route
import settings
# FIND SERVO MEASUREMENTS
# FIND ENGINE SLIPPAGE
# RERUN MAPPING AND ROUTING AFTER THRESHOLD
# TRACK LOCATION
# GLOBAL ORIENATION,
settings.init()

Final_destination = (100,100) # (y,x) from origin
def main_route(final_destination = None):
    numpy_map = main_map_function(max(final_destination) * 2 + 1)
    nav = route(numpy_map[0],goal=Final_destination)
    return nav

# main_route((100,100))
def drive(navigation):
    # current_orientation = "Forward"
    for nav in navigation:
        direction = nav[0]
        distance  = nav[1]
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

nav = main_route(Final_destination)
drive(nav)
