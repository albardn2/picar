


def init():
    global stop_sign
    global traffic_light
    global person
    global stop_sign_detected
    stop_sign,traffic_light, person, stop_sign_detected = False, False , False, False

    global global_orientation
    global_orientation = "F"
    global global_location
    global_location = (0,0)
