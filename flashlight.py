import cv2
import numpy as np

pts = []
while (1):

    # Take each frame
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_flashlight = np.array([0, 0, 255])
    upper_flashlight = np.array([0, 0, 255])
    mask = cv2.inRange(hsv, lower_flashlight, upper_flashlight)
    (minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(mask)

    cv2.circle(frame, maxLoc, 50, (0, 0, 255), 2, cv2.LINE_AA)
    cv2.imshow('flash', frame)

    

cv2.destroyAllWindows()
