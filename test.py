import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe hand tracking
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.5,
                       min_tracking_confidence=0.5)

# Define the steering wheel parameters
wheel_center = (150, 150)
wheel_radius = 100

# Initialize the current steering value and previous hand position
current_steering = 0
prev_hand_pos = np.zeros(2)

# Start the video capture loop
cap = cv2.VideoCapture(0)
while True:
    # Capture a frame from the webcam
    ret, frame = cap.read()

    # Convert the image to RGB and pass it to the hand tracking module
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the virtual steering wheel on the frame
    cv2.circle(frame, wheel_center, wheel_radius, (0, 0, 255), 2)
    cv2.line(frame, wheel_center, (int(wheel_center[0] + wheel_radius * np.cos(np.radians(current_steering))),
                                   int(wheel_center[1] - wheel_radius * np.sin(np.radians(current_steering)))),
             (255, 0, 0), 2)

    # Draw the detected hand landmarks on the frame
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
                frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Calculate the hand's position and movement
            hand_points = np.zeros((21, 2))
            for i, landmark in enumerate(hand_landmarks.landmark):
                hand_points[i] = [landmark.x, landmark.y]
            hand_pos = np.mean(hand_points, axis=0)
            hand_vel = hand_pos - prev_hand_pos
            hand_dir = hand_vel / np.linalg.norm(hand_vel)

            # Map hand movements to steering input
            steering_input = hand_dir[0] * 90
            current_steering = int(steering_input)

            # Print the steering direction
            cv2.putText(frame, 'Steering: {}'.format(current_steering), (20, 50),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Update previous hand position
            prev_hand_pos = hand_pos

    # Display the frame
    cv2.imshow('Virtual Steering Wheel', frame)
    if cv2.waitKey(1) == 27:
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
