# import the opencv library
import cv2
import numpy as np
import tensorflow as tf

# define a video capture object
cam = cv2.VideoCapture(0)

net_path = "./tensorflow/ssd-model/lite-model_ssd_mobilenet_v2_100_int8_default_1.tflite"


while(True):
    # Capture the video frame by frame
    success, frame = cam.read()

    if not success:
        print("Camera could not be read")
        break

    else:
        rows, cols, channels = frame.shape
 
        ## Load TFLite model and allocate tensors.
        interpreter = tf.lite.Interpreter(model_path="converted_model.tflite")
        interpreter.allocate_tensors()
        # Get input and output tensors.
        input_details = interpreter.get_input_details()
        output_details = interpreter.get_output_details()

        # Prepare input data.
        input_shape = input_details[0]['shape']
        input_data = cv2.resize(frame, input_shape, interpolation = cv2.INTER_AREA)

        # Run model on the input data.
        interpreter.set_tensor(input_details[0]['index'], input_data)
        interpreter.invoke()
        # The function `get_tensor()` returns a copy of the tensor data.
        # Use `tensor()` in order to get a pointer to the tensor.
        output_data = interpreter.get_tensor(output_details[0]['index'])
        print(output_data)

        # # Loop on the outputs
        # for detection in output_data[0,0]:
            
        #     score = float(detection[2])
        #     if score > 0.2:
        #         left = detection[3] * cols
        #         top = detection[4] * rows
        #         right = detection[5] * cols
        #         bottom = detection[6] * rows
        
        #         #draw a red rectangle around detected objects
        #         cv2.rectangle(frame, (int(left), int(top)), (int(right), int(bottom)), (0, 0, 255), thickness=2)

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