import cv
import numpy as np
import cv2

# defining a video capture object
cap = cv2.VideoCapture(0)

fgbg = cv2.createBackgroundSubtractorMOG2()

while(True):
    # Capturing the video frame
    # by frame
    ret, frame = cap.read()

    # Display the resulting frame
    fgmask = fgbg.apply(frame)
    cv2.imshow('frame',fgmask)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()