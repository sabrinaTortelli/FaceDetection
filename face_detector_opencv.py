import cv2


def detector_face(paths0):
    #Modelo pré-treinado de detecção de face do open-cv
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    for i, path in enumerate(paths0):
        print(str(i) + '-' + str(path))
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        try:
            faces = face_cascade.detectMultiScale(gray, 1.03, 5)
            for j, (x, y, w, h) in enumerate(faces):
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.imshow("teste", img)
            k = cv2.waitKey(0)
            if k == 27 or k == ord('q'):
                cv2.destroyAllWindows()
        except:
            continue