import picar_4wd as pcar
import time
import math
import settings
pcar.start_speed_thread()

def move_cm_forward(distance):
    time.sleep(0.3)
    distance = abs(distance)
    t = time.time()
    total_dist = 0
    pcar.forward(50)
    previous_time = t
    while total_dist < distance:
        if settings.stop_sign_detected==False and settings.stop_sign == True:
            pcar.stop()
            time.sleep(3)
            pcar.forward(50)
            settings.stop_sign = False
            settings.stop_sign_detected = True
            
        if settings.person == True:
            pcar.stop()
            print("PERSON STOP")
            while settings.person == True:
                time.sleep(3)
                continue
            pcar.forward(50)
        # print(total_dist)
        current_time = time.time()
        total_dist += pcar.speed_val() * (current_time - previous_time)
        previous_time = current_time
    pcar.stop()
    time.sleep(0.3)
    return total_dist

def car_orientation(current,final):
    time.sleep(0.4)
    if final  == current:
        return

    distance = 2*13*math.pi/4
    t = time.time()
    total_dist = 0
    if (current == "F" and final == "R") or (current == "R" and final == "B") or (current == "L" and final == "F"):
        pcar.turn_right(50)
    elif (current == "F" and final == "L") or (current == "R" and final == "F") or (current == "L" and final == "B"):
        pcar.turn_left(50)
    elif (current == "F" and final == "B") or (current == "R" and final == "L") or (current == "L" and final =="R"):
        pcar.turn_left(50)
        distance *=2
    previous_time = t
    while total_dist < distance:
        if settings.stop_sign_detected==False and settings.stop_sign == True:
            pcar.stop()
            time.sleep(3)
            pcar.forward(50)
            settings.stop_sign = False
            settings.stop_sign_detected = True
            
        if settings.person == True:
            pcar.stop()
            print("PERSON STOP")
            while settings.person == True:
                time.sleep(3)
                continue
            pcar.forward(50)
#         print(total_dist)
        current_time = time.time()
        total_dist += pcar.speed_val() * (current_time - previous_time)
        previous_time = current_time
#     time.sleep(0.8)
    pcar.stop()
    time.sleep(0.3)
    return total_dist

# time.sleep(5)
# move_cm_forward(25)
# car_orientation("left")
# move_cm_forward(30)
# time.sleep(5)
# pcar.forward(50)
# time.sleep(3)
# pcar.stop()