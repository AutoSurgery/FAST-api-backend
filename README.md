# Surgical Tool Detection API

This is an API for detecting surgical tools from an input image. The API is developed using the FastAPI framework and is based on a deep learning model that can recognize surgical tools from various viewpoints and angles.

## Usage

To use the API, you need to send a POST request to the `/predict` endpoint with an image file in the request body. The API will return a JSON object with the detected surgical tools and their confidence scores.

## API Endpoints

The API provides the following endpoints:
- `POST /object-to-json`: This endpoint takes an image file as input and returns a JSON response with the detected objects in the image. The response will contain a list of objects with their class name, confidence score, and bounding box coordinates.

- `POST /object-to-img`: This endpoint takes an image file as input and returns a JSON response with the detected objects in the image, along with an image file with bounding boxes drawn around the detected objects.

- `POST /image-segmentation`: This endpoint takes an image file as input and performs image segmentation. The response will contain a base64-encoded image file with the segmented image.


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
