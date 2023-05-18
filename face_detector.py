from pathlib import Path

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
        print("Interation " + i)
        # loop for image processing, takes an image array produced in main
        # and iterates through it

        string = path
        # obtains path from current iterator

        file_name = path[string.find("/") + 1:]
        # string slicer finds / on path, gets its index adds one to it
        # slices the string from the index to the end and stores it in file_name
        # file_name will be used by the saving method bellow

        input_image = face_recognition.load_image_file(path)
        # uses face_recognition to load image into input_image

        input_face_locations = face_recognition.face_locations(input_image, model=model)
        # locates faces in the loaded image according to the assigned model and saves it in input_face_locations
        # generates a tuple containing the coordinates for drawing each face's bounding box

        with open("imagesSaved/faceDetector/face_detector.txt", "a") as file:
            # opens opencv.tx with value "a" for appending

            file.write(file_name + "\n" + str(len(input_face_locations)) + "\n")
            # writes current image's name and amount of detected faces

        pillow_image = Image.fromarray(input_image)
        # generates a PIL image for drawing bounding boxes

        draw = ImageDraw.Draw(pillow_image)
        # creates draw image for drawing bounding boxes

        for bounding_box in input_face_locations:
            print("FACE DETECTED", bounding_box)
            # prints located bounding boxes

            with open("imagesSaved/faceDetector/face_detector.txt", "a") as file:
                file.write(str(bounding_box) + "\n")
                # writes bounding boxes coordinates on opencv.txt

            _display_face(draw, bounding_box, "FACE DETECTED")
            # calls _display_face passing the draw image, bounding_box, and a label for the bounding box
        with open("imagesSaved/faceDetector/face_detector.txt", "a") as file:
            file.write("\n")

        del draw
        # deletes current draw

        save_image(file_name, pillow_image)
        # saves processed images with bounding boxes using filename

        print("\n")


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
    # receives an image name and an image file

    path = str(Path("imagesSaved/faceDetector/") / image_name)
    # uses Path lib for solving multi OS / issue on directory tree
    #path = "imagesSaved/faceDetector/" + image_name
    image.save(path)
    # saves image on the informed path using pillow lib
