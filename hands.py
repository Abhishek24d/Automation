import mediapipe as mp
import cv2
import time
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
# print(mp.__file__)
#capturing image and Detecting Hands-----------------------------
cap = cv2.VideoCapture(0)
while 1:

    status, img = cap.read()

    init = time.time()

    img.flags.writeable = False
    image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hands = mp_hands.Hands()
    results = hands.process(image)


    img.flags.writeable = True
    image = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)


    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            )

    final_time = time.time()
    flipped_image = cv2.flip(image, 1)

    fps = 1//(final_time-init)
    cv2.putText(flipped_image, str(fps) , (10,50),cv2.FONT_HERSHEY_SIMPLEX,fontScale=1, color=(255,156,255), thickness=5,)
    cv2.imshow('image', flipped_image)

    if cv2.waitKey(1) == 27:
        break
    print(status)# True or False
cap.release()
cv2.destroyAllWindows()
#--------------------------------------------
