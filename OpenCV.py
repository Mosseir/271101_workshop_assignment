#This code demonstrate how to show location of hand landmark
import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)

#Call hand pipe line module
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


axis = np.zeros((21, 2))
#print(axis)
while True:
    finger = []
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for handRms in results.multi_hand_landmarks:
            for id, lm in enumerate(handRms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                axis[id] = [cx, cy] # [ 0, 1 ]
                #print(id , axis[id])
            if axis[4, 0] > axis[3, 0]:
                finger.append("Thumbs")
            if axis[8, 1] < axis[7, 1]:
                finger.append("Index")
            if axis[12, 1] < axis[11, 1]:
                finger.append("Middle")
            if axis[16, 1] < axis[15, 1]:
                finger.append("Ring")
            if axis[20, 1] < axis[19, 1]:
                finger.append("Pinky")

            mpDraw.draw_landmarks(img, handRms, mpHands.HAND_CONNECTIONS)
    Nfing = len(finger)
    cv2.putText(img, str(Nfing), (10, 150), cv2.FONT_HERSHEY_PLAIN, 1.5,
                (0, 0, 252), 2)
    cv2.putText(img, str(finger), (10, 70), cv2.FONT_HERSHEY_PLAIN, 1.5,
                (0, 0, 252), 2)
    cv2.imshow("Index finger of right-hand system", img)
    cv2.waitKey(1)
#Closeing all open windows
#cv2.destroyAllWindows()