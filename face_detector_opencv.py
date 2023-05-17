import cv2
from pathlib import Path


def detector_face(paths0):
    # Modelo pré-treinado de detecção de face do open-cv
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    for i, path in enumerate(paths0):
        # Substring para capturar o nome do arquivo
        string = path
        file_name = path[string.find("/") + 1:]
        #lê a imagem
        img = cv2.imread(path)
        #Transforma a imagem em tons de cinza
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        try:
            #algoritmo para a detecção das faces
            #param1 = imagem em tons de cinza
            #param2 = fator de escala
            #param3 = quantidade de vizinhos que cada retângulo candidato deve ter para retê-lo
            faces = face_cascade.detectMultiScale(gray, 1.04, 5)
            # Escreve no arquivo txt o nome da imagem que está sendo processada e o total de faces detectadas
            with open("imagesSaved/openCV/opencv.txt", "a") as file:
                file.write(file_name + "\n" + str(len(faces)) + "\n")

            for j, (x, y, w, h) in enumerate(faces):
                #Desenha os bounding box na imagem
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # Escreve os bounding box encontrados na imagem
                with open("imagesSaved/openCV/opencv.txt", "a") as file:
                    file.write("(" + str(x) + ", " + str(y) + ", " + str(w) + ", " + str(h) + ")\n")
                print(str(x) + " - " + str(y))
            # Salva as imagens com os bounding box desenhados
            save_image(file_name, img)

        except:
            continue


def save_image(image_name, image):
    # recebe um nome para a imagem, concatena a terminação e salva a imagem no path indicado
    # o Path especifica o path no formato / forward slash e resolve o caminho no SO que está rodando
    path = str(Path("imagesSaved/openCV/") / image_name)
    cv2.imwrite(path, image)
