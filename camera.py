import picamera
import time

camera =picamera.PiCamera()
camera.start_preview()
time.sleep(5)
camera.capture('picture.jpg')
camera.stop_preview

