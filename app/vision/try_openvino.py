# -*- coding: utf-8 -*-
# FileName: try_openvino.py
# Time : 2024/8/15 23:01
# Author: zzy
import cv2
import numpy as np
from openvino import IECore

# COCO dataset labels
class_names = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat", "traffic light",
               "fire hydrant",
               "stop sign", "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear",
               "zebra", "giraffe", "backpack", "umbrella",
               "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
               "baseball glove", "skateboard", "surfboard",
               "tennis racket", "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple",
               "sandwich", "orange", "broccoli", "carrot",
               "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed", "diningtable", "toilet",
               "tvmonitor", "laptop", "mouse", "remote",
               "keyboard", "cell phone", "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock",
               "vase", "scissors", "teddy bear", "hair drier", "toothbrush"]

# OpenVINO IR model files
ir_filename = "D:/chenhan/opencv_tutorial_data-master/models/yolov5/yolov5s.xml"


# Function to fill tensor data with image
def fill_tensor_data_image(input_tensor, input_image):
    tensor_shape = input_tensor.shape
    width, height, channels = tensor_shape[3], tensor_shape[2], tensor_shape[1]
    input_tensor_data = input_tensor.data
    for c in range(channels):
        for h in range(height):
            for w in range(width):
                input_tensor_data[c * width * height + h * width + w] = input_image[h, w, c]


# Create OpenVINO Core
ie = IECore()
net = ie.read_network(model=ir_filename, weights=ir_filename.replace(".xml", ".bin"))
exec_net = ie.load_network(network=net, device_name="CPU", num_requests=1)

# Preprocess input data
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Exit! Webcam fails to open!")
    exit()

input_image_tensor = next(iter(net.input_info))
input_h, input_w = net.input_info[input_image_tensor].input_data.shape[2], \
net.input_info[input_image_tensor].input_data.shape[3]
print(f"input_h: {input_h}; input_w: {input_w}")
print(f"input_image_tensor's element type: {net.input_info[input_image_tensor].precision}")
print(f"input_image_tensor's shape: {net.input_info[input_image_tensor].input_data.shape}")

output_image_tensor = next(iter(net.outputs))
out_rows, out_cols = net.outputs[output_image_tensor].shape[2], net.outputs[output_image_tensor].shape[3]
print(f"out_cols: {out_cols}; out_rows: {out_rows}")

while True:
    ret, frame = cap.read()

    if not ret:
        print("Failed to grab frame")
        break

    start = cv2.getTickCount()
    h, w = frame.shape[:2]
    _max = max(h, w)
    image = np.zeros((_max, _max, 3), dtype=np.uint8)
    image[:h, :w] = frame

    x_factor, y_factor = image.shape[1] / input_w, image.shape[0] / input_h

    blob_image = cv2.resize(image, (input_w, input_h)).astype(np.float32) / 255.0

    # Fill image data into the input tensor
    fill_tensor_data_image(exec_net.requests[0].input_blobs[input_image_tensor], blob_image)

    # Perform inference
    exec_net.requests[0].infer()

    # Get inference results
    output_tensor = exec_net.requests[0].output_blobs[output_image_tensor]
    det_output = output_tensor.buffer

    boxes, classIds, confidences = [], [], []

    for i in range(det_output.shape[0]):
        confidence = det_output[i, 4]
        if confidence < 0.4:
            continue
        classes_scores = det_output[i, 5:85]
        classIdPoint = np.argmax(classes_scores)
        score = classes_scores[classIdPoint]

        if score > 0.5:
            cx, cy, ow, oh = det_output[i, :4]
            x = int((cx - 0.5 * ow) * x_factor)
            y = int((cy - 0.5 * oh) * y_factor)
            width = int(ow * x_factor)
            height = int(oh * y_factor)
            box = (x, y, width, height)
            boxes.append(box)
            classIds.append(classIdPoint)
            confidences.append(score)

    # Non-maximum suppression
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.25, 0.45)

    for i in indexes:
        i = i[0]
        idx = classIds[i]
        x, y, width, height = boxes[i]
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 0, 255), 2)
        cv2.rectangle(frame, (x, y - 20), (x + width, y), (0, 255, 255), -1)
        cv2.putText(frame, class_names[idx], (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0))

    t = (cv2.getTickCount() - start) / cv2.getTickFrequency()
    print(f"Infer time(ms): {t * 1000:.2f}ms; Detections: {len(indexes)}")
    cv2.putText(frame, f"FPS: {1.0 / t:.2f}", (20, 40), cv2.FONT_HERSHEY_PLAIN, 2.0, (255, 0, 0), 2)
    cv2.imshow("YOLOv5-6.1 + OpenVINO 2022.1 Python Demo", frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC
        break

cv2.destroyAllWindows()
