# Dr. Driving Game using Virtual Steering with Mediapipe and OpenCV

![](https://github.com/sv2441/Dr.-Driving-Game-using-Virtual-Steering-with-Mediapipe-and-OpenCV/blob/master/output.gif)

Introduction

"Dr. Driving" is a popular mobile game that requires the player to drive a car through a city while obeying traffic rules and completing various challenges. In this report, we will explore how to play "Dr. Driving" game using virtual steering built with Mediapipe and OpenCV.

Methodology

1) Load the hand tracking model: Load the hand tracking model from Mediapipe. The hand tracking model will detect the hand and its landmarks.

2) Load the drawing module: Load the drawing module from OpenCV. The drawing module will be used to draw the virtual steering wheel on the detected hand.

3) Define the region of interest: Define the region of interest (ROI) around the detected hand. This ROI will be used to draw the virtual steering wheel on the detected hand.

4) Define the steering angles: Define the steering angles for the left and right turns. These angles will be used to calculate the steering direction based on the hand landmarks.

5) Calculate the steering direction: Calculate the steering direction based on the hand landmarks. You can use the position of the thumb and the index finger to calculate the direction.


Here are the steps to play "Dr. Driving" game using virtual steering:

## Installation

Clone the Repository
and Install the library

```bash
  pip install opencv-python
  pip install mediapipe
```

## Run This

```bash
   python run Steering.py
```

## Results

Using virtual steering with Mediapipe and OpenCV, we were able to successfully control the car in "Dr. Driving" game using hand movements. The steering was responsive and accurate, allowing us to easily navigate through the city and complete the challenges.

## Conclusion

Virtual steering with Mediapipe and OpenCV is a powerful tool that can be used to control games and applications using hand movements. With this technique, we were able to play "Dr. Driving" game without using a physical steering wheel or a controller, which is a fun and immersive experience.

## Tech Stack

OpenCV , Mediapipe

## Demo

**[Youtube](https://github.com/sv2441/Dr.-Driving-Game-using-Virtual-Steering-with-Mediapipe-and-OpenCV/blob/master/Result.mkv)**

## Acknowledgements

- [Hand Detection | mediapipe](https://google.github.io/mediapipe/solutions/pose.html)

## Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://sv2441.github.io/sandeepp/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sandeep-vishwakarma-3b592b174/)
