from mapping import main_map_function
from move import move_cm_forward, car_orientation
import picar_4wd as pcar

# FIND SERVO MEASUREMENTS
# FIND ENGINE SLIPPAGE
# RERUN MAPPING AND ROUTING AFTER THRESHOLD
# TRACK LOCATION

def main_route(goal = None):
    numpy_map = main_map_function(max(goal))
    nav = route(numpy_map,goal=goal)
    return nav




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
