# Blood Cells Detection with Deployment

## Overview

This project uses deep learning for blood cell detection using a YOLOv10 (You Only Look Once) model fine-tuned on the **BCCD dataset**. The trained model is deployed as a web app using **Gradio** and hosted on **Hugging Face Spaces**. This application allows users to upload images of blood cell samples and receive instant predictions on the presence of various cell types.

## Features

- **Object Detection:** Detects different types of blood cells in images.
- **Model:** YOLOv10 fine-tuned on the BCCD dataset.
- **Web Interface:** Simple and interactive Gradio interface to upload images and view results.
- **Deployment:** Deployed on Hugging Face Spaces for easy access.

![Screenshot 2025-03-19 220617](https://github.com/user-attachments/assets/392f14d1-afd5-4e07-be62-7278682564bb)

![Screenshot 2025-03-19 220631](https://github.com/user-attachments/assets/d02ae302-7b45-4a7e-a977-e1f9c2500aae)

## Installation

### Requirements

- Python 3.8 or higher
- `pip` for installing dependencies

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/sohal944/Blood-Cells-Detection-With-Deployement.git
2. cd Blood-Cells-Detection-With-Deployement-

3. pip install -r requirements.txt

 python app.py

