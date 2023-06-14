import cv2
import mediapipe as mp
import pyautogui

# Initialize video capture
cap = cv2.VideoCapture(0)

# Initialize hand detector
hand_detector = mp.solutions.hands.Hands()

# Initialize drawing utilities
drawing_utils = mp.solutions.drawing_utils

# Get screen dimensions
screen_width, screen_height = pyautogui.size()

# Initialize index finger position
index_x = 0
index_y = 0

while True:
    # Read frame from video capture
    _, frame = cap.read()
    
    # Flip frame horizontally
    frame = cv2.flip(frame, 1)
    
    # Get frame dimensions
    frame_height, frame_width, _ = frame.shape
    
    # Convert frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with the hand detector
    output = hand_detector.process(rgb_frame)
    
    # Get detected hands
    hands = output.multi_hand_landmarks
    
    if hands:
        for hand in hands:
            # Draw landmarks on the frame
            drawing_utils.draw_landmarks(frame, hand)
            
            # Get landmarks
            landmarks = hand.landmark
            
            for id, landmark in enumerate(landmarks):
                # Calculate coordinates of landmark in pixel space
                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)
                
                if id == 8:  # Index finger tip
                    # Draw a circle on the index finger tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    
                    # Calculate index finger position in screen space
                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y

                if id == 4:  # Thumb tip
                    # Draw a circle on the thumb tip
                    cv2.circle(img=frame, center=(x, y), radius=10, color=(0, 255, 255))
                    
                    # Calculate thumb position in screen space
                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y
                    
                    # Calculate the vertical distance between index finger and thumb
                    distance = abs(index_y - thumb_y)
                    print('distance:', distance)
                    
                    if distance < 20:
                        # If the distance is small, perform a click action
                        pyautogui.click()
                        pyautogui.sleep(1)
                    elif distance < 100:
                        # If the distance is moderate, move the mouse to the index finger position
                        pyautogui.moveTo(index_x, index_y)
    
    # Show the frame with virtual mouse
    cv2.imshow('Virtual Mouse', frame)
    
    # Wait for key press and exit loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release video capture and destroy windows
cap.release()
cv2.destroyAllWindows()

