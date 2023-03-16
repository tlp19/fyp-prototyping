# import packages
import cv2
import numpy as np

# define a video capture object
cam = cv2.VideoCapture(0)

network = cv2.dnn.readNet(
        'tensorflow/yolo-model/yolov3.weights',
        'tensorflow/yolo-model/yolov3.cfg')

# read class names from text file
classes_path = 'tensorflow/yolo-model/coco.names'
with open(classes_path, 'r') as f:
    classes = [line.strip() for line in f.readlines()]

# generate different colors for different classes 
COLORS = np.random.uniform(0, 255, size=(len(classes), 3))



# function to get the output layer names 
# in the architecture
def get_output_layers(net):
    layer_names = net.getLayerNames()
    output_layers_idx = net.getUnconnectedOutLayers()
    output_layers = [layer_names[i - 1] for i in output_layers_idx]
    return output_layers

# function to draw bounding box on the detected object with class name
def draw_bounding_box(img, class_id, confidence, x, y, x_plus_w, y_plus_h):
    label = str(classes[class_id])
    color = COLORS[class_id]
    cv2.rectangle(img, (x,y), (x_plus_w,y_plus_h), color, 2)
    cv2.putText(img, label, (x-10,y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)



while(True):
    # Capture the video frame by frame
    success, frame = cam.read()
    if not success:
        print("Camera could not be read")
        break
    else:

        rows, cols, channels = frame.shape
        
        # create input blob 
        blob = cv2.dnn.blobFromImage(frame, 1, (416,416), (0,0,0), True, crop=False)
        # set input blob for the network
        network.setInput(blob)

        # run inference through the network
        # and gather predictions from output layers
        outs = network.forward(get_output_layers(network))

        # initialization
        class_ids = []
        confidences = []
        boxes = []
        conf_threshold = 0.5
        nms_threshold = 0.4

        # for each detetion from each output layer 
        # get the confidence, class id, bounding box params
        # and ignore weak detections (confidence < 0.5)
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * cols)
                    center_y = int(detection[1] * rows)
                    w = int(detection[2] * cols)
                    h = int(detection[3] * rows)
                    x = center_x - w / 2
                    y = center_y - h / 2
                    class_ids.append(class_id)
                    confidences.append(float(confidence))
                    boxes.append([x, y, w, h])

        # apply non-max suppression
        indices = cv2.dnn.NMSBoxes(boxes, confidences, conf_threshold, nms_threshold)

        # go through the detections remaining
        # after nms and draw bounding box
        for i in indices:
            box = boxes[i]
            x = box[0]
            y = box[1]
            w = box[2]
            h = box[3]
            
            draw_bounding_box(frame, class_ids[i], confidences[i], round(x), round(y), round(x+w), round(y+h))

        # display output image    
        cv2.imshow("object detection", frame)

        

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cam.release()
# Destroy all the windows
cv2.destroyAllWindows()