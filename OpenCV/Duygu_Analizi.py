import cv2
from deepface import DeepFace
import pygame

cap=cv2.VideoCapture(0)
pygame.mixer.init()

emotion_translate={
    "angry": "Kizgin",
    "disgust": "Tiksinti",
    "fear": "Korku",
    "happy":"Mutlu",
    "sad": "Uzgun",
    "surprise": "Saskin",
    "neutral": "Notr"
}

emotion_voice={
    "happy": "happy.mp3",
    "sad": "sad.mp3"
}

last_emotion=None

while True:
    ret,frame=cap.read()

    if not ret:
        break

    try:
        analysis=DeepFace.analyze(frame,actions=['emotion'],enforce_detection=False)

        for face in analysis:
            x,y,w,h=face['region']['x'],face['region']['y'],face['region']['w'],face['region']['h']

            emotion=face['dominant_emotion']

            turkce_duygular=emotion_translate.get(emotion)


            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
            cv2.putText(frame,turkce_duygular,(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,255),2)

            if emotion in emotion_voice and emotion_voice !=last_emotion:
                pygame.mixer.music.load(emotion_voice[emotion])
                pygame.mixer.music.play()
                last_emotion=emotion

    except Exception as e:
        print('Hata: ',e)

    cv2.imshow('Gerçek Zamanlı Duygu Analizi',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()