# ---------------------------------------------------------
# Prediction:
#     - Face Mask Detection 
#       -------------------
#     - Headshots invocation and execution
#       - - - - - - - - - -
#       December /021
#       - - - - - - - - - -
# ---------------------------------------------------------

import cv2
from picamera import PiCamera
from picamera.array import PiRGBArray
        #import project support libraries

name = 'Student-X'  
        #replace with your name
cam = PiCamera()    
        #camera object
cam.resolution = (512, 304)
        #camera resolution dfn
cam.framerate = 10
        #camera frame dfn
rawCapture = PiRGBArray(cam, size=(512, 304))
    
img_counter = 0
        # control var handler
while True:
    for frame in cam.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        image = frame.array
        cv2.imshow("Press Space to take a photo", image)
        rawCapture.truncate(0)
    
        k = cv2.waitKey(1)
        rawCapture.truncate(0)
        if k%256 == 27: # ESC pressed
            break
        elif k%256 == 32:
            # SPACE pressed
            img_name = "dataset/"+ name +"/image_{}.jpg".format(img_counter)
            cv2.imwrite(img_name, image)
            print("{} written!".format(img_name))
            img_counter += 1
            
    if k%256 == 27:
        print("Escape hit, closing...")
        break

        #closes camera capture window
cv2.destroyAllWindows()