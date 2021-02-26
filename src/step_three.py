import picar_4wd as pcar
import time
from move import car_orientation, move_cm_forward
servo_angle = 0
turning = False

def get_distances_list(max_angle = 45, min_angle = -45,step_increment = 9):
        global servo_angle
        angle_list = []
        if servo_angle >= max_angle:
            step_increment = -abs(step_increment)
            while servo_angle >= min_angle:
                angle_list.append((pcar.us.get_distance()/3,servo_angle))
                pcar.servo.set_angle(servo_angle + step_increment)
                servo_angle = servo_angle + step_increment
                time.sleep(0.04)
            return angle_list

        elif servo_angle <= min_angle:
            step_increment = abs(step_increment)
            while servo_angle <= max_angle:
                angle_list.append((pcar.us.get_distance()/3,servo_angle))
                pcar.servo.set_angle(servo_angle + step_increment)
                servo_angle = servo_angle + step_increment
                time.sleep(0.06)
            return list(reversed(angle_list))
        else:
            pcar.servo.set_angle(min_angle)
            servo_angle = min_angle
        return angle_list


def step_three():
    global turning
    turning = False
    try:
        while True:
            l = [d[0] for d in get_distances_list(max_angle=45, min_angle=-45, step_increment=20)]
            print(l)
            l = list(filter(lambda f: f != -2, l))
            print(l)
            if len(l) > 0 and min(l) <= 30:
                if turning == True:
                    continue
                pcar.backward(50)
                time.sleep(0.5)

                pcar.turn_left(50)
                turning = True
            else:
                turning = False
                pcar.forward(50)
    except:
        pcar.stop()
def navigate_around_obstacle():
    pcar.forward(50)
    try:
        while True:
            l = [d[0] for d in get_distances_list(max_angle=45, min_angle=-45, step_increment=20)]
#             print(l)
            l = list(filter(lambda f: f != -2, l))
#             print(l)
            if len(l) > 0 and min(l) <= 30:
                pcar.stop()
                car_orientation(current="F",final="L")
                move_cm_forward(30)
                car_orientation(current="L",final="F")
            pcar.forward(50)
    except:
        pcar.stop()
# time.sleep(10)
# step_three()
# pcar.stop()
# navigate_around_obstacle()
# move_cm_forward(1)
# car_orientation(current="F", final="R")
# car_orientation(current="R", final="F")

# car_orientation(current="F",final="L")
# car_orientation(current="L",final="F")
# car_orientation(current="F",final="R")
# car_orientation(current="R",final="F")
