from picamera import PiCamera

camera = PiCamera()
camera.resolution = (1024,768)
camera.vflip = True
camera.start_preview()
    