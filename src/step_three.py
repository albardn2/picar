import picar_4wd as pcar
import time

servo_angle = 0
turning = False

def get_distances_list(max_angle = 45, min_angle = -45,step_increment = 9):
        global servo_angle
        angle_list = []
        if servo_angle >= max_angle:
            step_increment = -abs(step_increment)
            while servo_angle >= min_angle:
                angle_list.append((pcar.us.get_distance()/5,servo_angle))
                pcar.servo.set_angle(servo_angle + step_increment)
                servo_angle = servo_angle + step_increment
                time.sleep(0.04)
            return angle_list

        elif servo_angle <= min_angle:
            step_increment = abs(step_increment)
            while servo_angle <= max_angle:
                angle_list.append((pcar.us.get_distance()/5,servo_angle))
                pcar.servo.set_angle(servo_angle + step_increment)
                servo_angle = servo_angle + step_increment
                time.sleep(0.04)
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
            if len(l) > 0 and min(l) <= 20:
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


# step_three()
# left_rear_speed = pcar.Speed(25)
# left_rear_speed.start()
# pcar.forward(0)
#
# while True:
#     print(left_rear_speed.speed)
#     time.sleep(1)
