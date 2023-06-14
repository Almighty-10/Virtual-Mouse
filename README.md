# Virtual-Mouse


1. The code imports the necessary libraries: `cv2` for capturing and processing video, `mediapipe` for hand detection, and `pyautogui` for controlling the mouse cursor.
2. It sets up the video capture using the default camera (`0`).
3. The hand detector and drawing utilities are initialized from the `mediapipe` library.
4. The screen width and height are obtained using `pyautogui.size()`, which returns the dimensions of the screen.
5. The code enters an infinite loop to continuously process video frames.
6. Inside the loop, it reads a frame from the video capture and flips it horizontally to create a mirror effect.
7. The frame's height, width, and number of channels (color depth) are extracted.
8. The frame is converted from the BGR color space to RGB color space, as required by the hand detector.
9. The hand detector processes the RGB frame to detect hands, and the results are stored in the `output` variable.
10. The `output` object contains information about the detected hands, such as hand landmarks.
11. If hands are detected (`hands` is not None), the code iterates over each detected hand.
12. For each hand, the code uses the drawing utilities to draw landmarks (keypoints) on the frame.
13. The landmarks for the current hand are extracted.
14. The code loops over each landmark and retrieves its coordinates in pixel space.
15. If the landmark corresponds to the index finger tip (id 8), a circle is drawn on the frame at that position.
16. The index finger position is calculated in screen space using the screen dimensions and the ratio between the frame and screen.
17. If the landmark corresponds to the thumb tip (id 4), a circle is drawn on the frame at that position.
18. The thumb position is calculated in screen space using the same approach as the index finger.
19. The vertical distance between the index finger and thumb is calculated.
20. If the distance is small (< 20 pixels), a click action is performed using `pyautogui.click()`.
21. If the distance is moderate (< 100 pixels), the mouse cursor is moved to the index finger position using `pyautogui.moveTo()`.
22. The frame with the drawn landmarks is displayed in a window titled "Virtual Mouse".
23. The code waits for a key press, and if the 'q' key is pressed, it breaks the loop.
24. Finally, the video capture is released, and all windows are destroyed.

This code combines computer vision techniques with the Mediapipe library to track the user's hand and perform actions based on the position of the index finger and thumb. It provides a basic virtual mouse control using hand gestures.

#note
Make sure to have the required libraries (cv2, mediapipe, pyautogui) installed before running the code.
