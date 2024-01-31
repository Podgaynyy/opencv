import cv2
#funktion der face-anerkennung
face_cascades =cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


#img = cv2.imread("Lica.jpeg")
#faces = face_cascades.detectMultiScale(img) #anerkennung in img starten

#print(faces)
#for (x, y, w, h) in faces:
 #   cv2.rectangle(img, (x,y),(x+w, y+h), (0,0,255), 1) #viereck mit x,y, breite, hoehe, farbe und dicke
#cv2.imshow("Result", img)
#cv2.waitKey()
cap = cv2.VideoCapture(0) #aktiviert webcam

while True: #bleibt laufen
    _, frame = cap.read() #name und funktion

    faces = face_cascades.detectMultiScale(frame) #anerkennung in videoq starten
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x,y),(x+w, y+h), (0,0,255), 1)

    cv2.imshow("Result", frame)

    if cv2.waitKey(1) & 0xff == ord("q"):
        break