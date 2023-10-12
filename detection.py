import cv2
yuzCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

kamera= cv2.VideoCapture(0)

def kamera_read():
    ret, kare = kamera.read()
    if not ret:
        return None, None
    return kare, ret

while True:
    kare, ret = kamera_read()
    if kare is None:
        break

    # Giriş görüntüsünü yeniden boyutlandır
    kare = cv2.resize(kare, (480, 360))

    # Giriş görüntüsünü griye çevir
    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)

    yuzler = yuzCascade.detectMultiScale(
        gri,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20,20)
    )

    for (x,y,w,h) in yuzler:
        cv2.rectangle(kare,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('kare',kare)
        k = cv2.waitKey(1) & 0xff
        if k == 27 or k==ord('q'):
            break
kamera.release()
cv2.destroyAllWindows()
