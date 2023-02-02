# import the opencv library
import cv2
import numpy as np

# define a video capture object
cam = cv2.VideoCapture(0)

while(True):
    # Capture the video frame by frame
    success, frame = cam.read()

    if not success:
        print("Camera could not be read")
        break
    
    else:
        # Display the resulting frame
        cv2.imshow('initialFrame', frame)

        # Choose a crop ratio
        crop_ratio = 1/2

        # Find the position of each border
        height, width, _ = frame.shape
        side_length = height * crop_ratio
        top_border = int((height/2) - (side_length/2))
        bottom_border = int((height/2) + (side_length/2))
        left_border = int((width/2) - (side_length/2))
        right_border = int((width/2) + (side_length/2))

        # Slice the initial image
        center_frame = frame[top_border:bottom_border, left_border:right_border]
        cv2.imshow('centerFrame', center_frame)
        

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cam.release()
# Destroy all the windows
cv2.destroyAllWindows()