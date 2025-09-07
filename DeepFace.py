#pip install deepface tf-keras opencv-python

from deepface import DeepFace
import cv2
# Specify your img path
image_path="..."
image=cv2.imread(image_path)
if image is None:
    print("Error,image has not been loaded")
    exit()
try:
    result=DeepFace.analyze(image,actions=['emotion'])
    print("\n Full result:")
    print(result)

    highest_emotion=(None,0)
    for face in result:
        emotions=face['emotion']
        dominant=max(emotions.items(),key=lambda x:x[1])
        if dominant[1]>highest_emotion[1]:
            highest_emotion=dominant
    print("\nDominant emotion Analysis:")
    if highest_emotion[1]>50:
        print(f"Dominant emotion is:{highest_emotion[0]} ({highest_emotion[1]:.2f}%)")
    else:
        print("No dominant emotion detected.")
except Exception as e:
    print(f'Error:{e}')