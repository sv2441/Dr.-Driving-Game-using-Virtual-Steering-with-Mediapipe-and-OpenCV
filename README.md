# Dr. Driving Game using Virtual Steering with Mediapipe and OpenCV

![](https://github.com/sv2441/OpenCV-with-MediaPipeline/blob/master/allresultgif.gif)

Introduction

"Dr. Driving" is a popular mobile game that requires the player to drive a car through a city while obeying traffic rules and completing various challenges. In this report, we will explore how to play "Dr. Driving" game using virtual steering built with Mediapipe and OpenCV.

Methodology

We will be using a webcam to capture the player's hand movements and use that to control the car in the game. The virtual steering wheel will be drawn on the hand using OpenCV, and the player's hand movements will be tracked using Mediapipe.

The game itself will be running on a mobile device and connected to the computer running the Python code via Wi-Fi. We will use the ADB (Android Debug Bridge) tool to send touch events to the mobile device to control the car.

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

**[Youtube](https://sv2441.github.io/sandeepp/)**

## Acknowledgements

- [Hand Detection | mediapipe](https://google.github.io/mediapipe/solutions/pose.html)

## Links

[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://sv2441.github.io/sandeepp/)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/sandeep-vishwakarma-3b592b174/)
