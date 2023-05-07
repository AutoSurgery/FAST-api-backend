# Surgical Tool Detection API

This is an API for detecting surgical tools from an input image. The API is developed using the FastAPI framework and is based on a deep learning model that can recognize surgical tools from various viewpoints and angles.

## Usage

To use the API, you need to send a POST request to the /predict endpoint with an image file in the request body. The API will return a JSON object with the detected surgical tools and their confidence scores.

## Installation

To install the API, you need to clone this repository and install the dependencies using `pip`


```
git clone https://github.com/AutoSurgery/FAST-api-backend.git
cd FastApi_yolov5_semanticSegmentation-main
pip install -r requirements.txt
```

## Running the API

To run the API, you need to start the FastAPI server using `uvicorn`:

```
uvicorn main:app --reload
```
This will start the server on `localhost:8000` and enable automatic reloading of the code whenever a change is made.

## Models

The deep learning models used in this API are YOLOv5 for tool detection and U-Net for segmentation. YOLOv5 is a state-of-the-art object detection model that can detect different surgical tools, including scissors, forceps, scalpels, and retractors, with high accuracy. On the other hand, U-Net is a popular segmentation model that can accurately segment surgical tools from the background in the input image. The combination of these two models allows for precise detection and segmentation of surgical tools in real-time.
