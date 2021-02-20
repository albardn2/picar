import settings
import picar_4wd as pcar
import threading
from detect_picamera import main
import time

settings.init()
#start tf thread
################
tf_object_detection = threading.Thread(target=main, name="object_detection_thread")
tf_object_detection.start()

while True:
    if settings.stop_sign == True:
       time.sleep(3)
       pcar.forward(1)
    pcar.forward(1)
