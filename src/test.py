from mapping import main_map_function
from move import move_cm_forward, car_orientation
import picar_4wd as pcar
from routing import route

# FIND SERVO MEASUREMENTS
# FIND ENGINE SLIPPAGE
# RERUN MAPPING AND ROUTING AFTER THRESHOLD
# TRACK LOCATION


Final_destination = (100,100)   # y,x, from origin

def main_route(final_destination = None):
    numpy_map = main_map_function(max(final_destination) * 3)
    nav = route(numpy_map,goal=Final_destination)
    return nav



main_route((100,100))
# def drive(navigation):
#     current_orientation = "Forward"
#     for nav in navigation:
#         direction = nav[0]
#         distance = nav[1]
#
#         if distance > 0 and direction == "H":
#             #ORIENT LEFT
#             #MOVE LEFT BY VALUE (UNLESS ULTRASONIC < threshold or > 1 METER)
#         elif distance < 0 and direction == "H":
#             #ORIENT Right
#             #MOVE LEFT BY VALUE
#         elif distance > 0 and direction == "V":
#             #ORIENT Forward
#             #MOVE Forward BY VALUE
#         elif distance < 0 and direction == "V":
#             #Orient Backwards
#             #REMAP AND ROUTE
