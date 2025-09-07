import cv2 #open cv accessing the camera -pip install opencv-python
import mediapipe as mp #hand tracking -pip install mediapipe
#hand detection and drawing utilities
mp_hands=mp.solutions.hands
mp_drawing=mp.solutions.drawing_utils
hands=mp_hands.Hands(min_detection_confidence=0.5,min_tracking_confidence=0.5)

#open webcam
cap=cv2.VideoCapture(0)
while cap.isOpened():
    ret,frame=cap.read()#capture a frame
    if not ret:
        break
    #convert bgr to rgb
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    #process the frame
    results=hands.process(rgb_frame)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(frame,hand_landmarks,mp_hands.HAND_CONNECTIONS)
    #Display
    cv2.imshow('Hand Tracking',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()