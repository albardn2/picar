import picar_4wd as pcar






pcar.servo.set_angle(0)
import time
while True:
    print(pcar.us.get_distance())
    time.sleep(1)