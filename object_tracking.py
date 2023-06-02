# import the opencv library
import cv2
import sys
import numpy as np

# define a video capture object
cam = cv2.VideoCapture(0)
cam.set(cv2.CAP_PROP_AUTOFOCUS, 0)

# Choose a tracker type
tracker_types = ['MIL','KCF', 'GOTURN', 'MOSSE']
tracker_type = tracker_types[0]

if tracker_type == 'MIL':
    tracker = cv2.TrackerMIL_create()               #Not good
elif tracker_type == 'KCF':
    tracker = cv2.legacy.TrackerKCF_create()        #Okay-ish (good sometimes)
elif tracker_type == 'GOTURN':
    tracker = cv2.TrackerGOTURN_create()            #? Need additional file
elif tracker_type == 'MOSSE':
    tracker = cv2.legacy.TrackerMOSSE_create()      #Okay
else:
    tracker = None
    print('Incorrect tracker selected')
    sys.exit()

# Read first frame.
success, frame = cam.read()
if not success:
    print("Camera could not be read")
    sys.exit()

# Select a bounding box
bbox = cv2.selectROI(frame, False)
# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)
p1, p2 = 0, 0

while(True):
    # Capture the video frame by frame
    success, frame = cam.read()

    if not success:
        print("Camera could not be read")
        break

    # Start timer
    timer = cv2.getTickCount()

    # Update tracker
    ok, bbox = tracker.update(frame)

    # Draw bounding box
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
    else :
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
        cv2.rectangle(frame, p1, p2, (0,0,255), 2, 1)
    
    # Display tracker type on frame
    cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

    # Display result
    cv2.imshow("Tracking", frame)


    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cam.release()
# Destroy all the windows
cv2.destroyAllWindows()