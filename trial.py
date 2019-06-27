import time
import picamera

with picamera.PiCamera() as camera:

 camera.resolution= (400,168)
 camera.start_preview()
 time.sleep(1)
 camera.capture('pic2.jpg')
 camera.stop_preview()
