# import required libraries
from vidgear.gears import VideoGear
import cv2
import time
import numpy as np
from matplotlib import pyplot as plt

# define and start the stream on first source 
stream1 = VideoGear(source=1, logging=True).start() 

# define and start the stream on second source 
stream2 = VideoGear(source=2, logging=True).start() 

stereo = cv2.StereoBM_create(numDisparities = 0, blockSize = 5)

# infinite loop
while True:
    
    frameA = stream1.read()
    # read frames from stream1

    frameB = stream2.read()
    # read frames from stream2

    # check if any of two frame is None
    if frameA is None or frameB is None:
        #if True break the infinite loop
        break
    
    left_image= cv2.cvtColor(frameA, cv2.COLOR_BGR2GRAY)
    right_image= cv2.cvtColor(frameB, cv2.COLOR_BGR2GRAY)

    depth = stereo.compute(left_image, right_image)

    
    cv2.imshow("Output Frame1", left_image)
    cv2.imshow("Output Frame2", right_image)

    plt.imshow(depth)
    plt.axis('off')
    plt.pause(0.02)

    key = cv2.waitKey(1) & 0xFF
    # check for 'q' key-press
    if key == ord("q"):
        #if 'q' key-pressed break out
        break

    if key == ord("w"):
        #if 'w' key-pressed save both frameA and frameB at same time
        cv2.imwrite("Image-1.jpg", left_image)
        cv2.imwrite("Image-2.jpg", right_image)
        #break   #uncomment this line to break out after taking images
plt.show()

cv2.destroyAllWindows()
# close output window

# safely close both video streams
stream1.stop()
stream2.stop()
