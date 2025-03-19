import gradio as gr
import onnxruntime as ort
import numpy as np
import cv2

# Load ONNX model
session = ort.InferenceSession("best.onnx")  # Ensure correct path to your ONNX model

# Get input and output names
input_name = session.get_inputs()[0].name
output_name = session.get_outputs()[0].name

# Function to preprocess image
def preprocess(image):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)  # Convert RGB to BGR (if needed)
    image = cv2.resize(image, (640, 640))  # Resize to model input size
    image = image.astype(np.float32) / 255.0  # Normalize
    image = np.transpose(image, (2, 0, 1))  # Change to (C, H, W)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

# Function to make predictions
def detect_objects(image):
    processed_image = preprocess(image)
    preds = session.run([output_name], {input_name: processed_image})[0]  # Run inference
    
    # Process output (depends on YOLO format)
    detections = []
    for pred in preds[0]:
        x1, y1, x2, y2, conf, cls = pred
        if conf > 0.5:  # Confidence threshold
            detections.append((int(x1), int(y1), int(x2), int(y2), conf, int(cls)))
    
    # Draw bounding boxes
    for (x1, y1, x2, y2, conf, cls) in detections:
        label = f"Class {cls}: {conf:.2f}"
        cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(image, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    return image

# Add a small class mapping table
class_mapping = """
Class 0: RBC (Red Blood Cells)
Class 1: WBC (White Blood Cells)
Class 2: Platelets
"""

# Gradio Interface
iface = gr.Interface(
    fn=detect_objects,
    inputs=gr.Image(type="numpy"),
    outputs=gr.Image(type="numpy"),
    title="YOLOv10 BCCD Object Detection",
    description=f"Upload an image to detect RBCs, WBCs, and Platelets.\n\n"
                f"### Class Mapping:\n{class_mapping}",
    allow_flagging="never"
)

# Launch the app
if __name__ == "__main__":
    iface.launch()
