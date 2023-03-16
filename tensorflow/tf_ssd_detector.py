# import the opencv library
import cv2
import numpy as np

# define a video capture object
cam = cv2.VideoCapture(0)
network = cv2.dnn.readNetFromTensorflow(
        'tensorflow/ssd-model/saved_model.pb',
        'tensorflow/ssd-model/label_map.pbtxt')


while(True):
    # Capture the video frame by frame
    success, frame = cam.read()

    if not success:
        print("Camera could not be read")
        break

    else:
        rows, cols, channels = frame.shape
 
        # Use the given image as input, which needs to be blob(s).
        network.setInput(cv2.dnn.blobFromImage(frame, size=(640, 640), swapRB=True, crop=True))
        
        # Runs a forward pass to compute the net output
        output = network.forward()

        # Loop on the outputs
        for detection in output[0,0]:
            
            score = float(detection[2])
            if score > 0.2:
                left = detection[3] * cols
                top = detection[4] * rows
                right = detection[5] * cols
                bottom = detection[6] * rows
        
                #draw a red rectangle around detected objects
                cv2.rectangle(frame, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), thickness=2)

        # Show the image with a rectagle surrounding the detected objects 
        cv2.imshow('detections', frame)

        

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cam.release()
# Destroy all the windows
cv2.destroyAllWindows()