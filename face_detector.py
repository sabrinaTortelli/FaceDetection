import face_recognition
from PIL import Image, ImageDraw

BOUNDING_BOX_COLOR = "red"
TEXT_COLOR = "white"


def recognize_faces(paths0, model: str = "hog") -> None:
    # receives an image location and a model it uses to locate faces (hog/cnn)
    # hog stands for histogram of oriented gradients - works best in CPU
    # cnn stands for convolutional neural network - works best in GPU
    # returns None
    for i, path in enumerate(paths0):
        #Substring para capturar o nome do arquivo
        string = path
        file_name = path[string.find("/")+1:]

        input_image = face_recognition.load_image_file(path)
        # uses face_recognition to load image into input_image

        input_face_locations = face_recognition.face_locations(input_image, model=model)
        # locates faces in the loaded image according to the assigned model and saves it in input_face_locations
        # generates a tuple containing the coordinates for drawing each face's bounding box

        # Escreve no arquivo txt o nome da imagem que está sendo processada e o total de faces detectadas
        with open("imagesSaved/faceDetector/face_detector.txt", "a") as file:
            file.write(file_name + "\n" + str(len(input_face_locations)) + "\n")

        pillow_image = Image.fromarray(input_image)
        # generates a PIL image for drawing bounding boxes

        draw = ImageDraw.Draw(pillow_image)
        # creates draw image for drawing bounding boxes

        for bounding_box in input_face_locations:
            print("FACE DETECTED", bounding_box)
            # prints located bounding boxes

            #Escreve os bounding box encontrados na imagem
            with open("imagesSaved/faceDetector/face_detector.txt", "a") as file:
                file.write(str(bounding_box) + "\n")

            _display_face(draw, bounding_box, "FACE DETECTED")
            # calls _display_face passing the draw image, bounding_box, and a label for the bounding box

        del draw
        # deletes current draw
        #Salva as imagens com os bounding box desenhados
        save_image(file_name, pillow_image)


def _display_face(draw, bounding_box, name):
    # receives draw image, bounding_box, and a label for the bounding box
    # draws bounding boxes

    top, right, bottom, left = bounding_box
    # box limits

    draw.rectangle(((left, top), (right, bottom)), outline=BOUNDING_BOX_COLOR)
    # draws bounding box rectangle

    text_left, text_top, text_right, text_bottom = draw.textbbox((left, bottom), name)
    # text box limits

    draw.rectangle(((text_left, text_top), (text_right, text_bottom)), fill="red", outline="red")
    # draws text box

    draw.text((text_left, text_top), name, fill="white")
    # draws text


def save_image(image_name, image):
    # recebe um nome para a imagem, concatena a terminação e salva a imagem no path indicado
    # o Path especifica o path no formato / forward slash e resolve o caminho no SO que está rodando
    path = "imagesSaved/faceDetector/" + image_name
    image.save(path)