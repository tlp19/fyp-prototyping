# import the opencv library
import cv2
import numpy as np
import pyboof as pb

# define a video capture object
cam = cv2.VideoCapture(0)
#cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
#cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

detector = pb.FactoryFiducial(np.uint8).qrcode()

while(True):
    # Capture the video frame by frame
    success, frame = cam.read()

    if not success:
        print("Camera could not be read")
        break
    
    else:
        # # Display the resulting frame
        # cv2.imshow('initialFrame', frame)


        boof_img = pb.ndarray_to_boof(frame)
        detector.detect(boof_img)

        print("Detected a total of {} QR Codes".format(len(detector.detections)))

        for qr in detector.detections:
            print("Message: " + qr.message)
            print("     at: " + str(qr.bounds))

        cv2.imshow('detectionFrame', frame)
        
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(40) & 0xFF == ord('q'): #40 for 25Hz
        break

# After the loop release the cap object
cam.release()
# Destroy all the windows
cv2.destroyAllWindows()
