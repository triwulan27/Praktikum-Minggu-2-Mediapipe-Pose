import cv2
import mediapipe as mp
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw =mp.solutions.drawing_utils
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        break
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    hasil = pose.process(imgRGB)
    if hasil.pose_landmarks:
        mp_draw.draw_landmarks(img,hasil.pose_landmarks,mp_pose.POSE_CONNECTIONS)

        lm = hasil.pose_landmarks.landmark

        left_shoulder = lm[11]
        right_shoulder = lm[12]
        left_wrist = lm[15]
        right_wrist = lm[16] #Deteksi tangan terangkat

        if left_wrist.y < left_shoulder.y:
            cv2.putText(img,"Tangan Kiri Terangkat", (30,50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

        if right_wrist.y < right_shoulder.y:
            cv2.putText(img,"Tangan Kanan Terangkat", (30,100),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0),2)

    cv2.imshow("webcam",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
