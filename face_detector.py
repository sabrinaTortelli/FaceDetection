
import face_recognition
from PIL import Image, ImageDraw

BOUNDING_BOX_COLOR = "red"
TEXT_COLOR = "white"


def recognize_faces(image_location: str, model: str = "hog") -> None:
    # receives an image location and a model it uses to locate faces (hog/cnn)
    # hog stands for histogram of oriented gradients - works best in CPU
    # cnn stands for convolutional neural network - works best in GPU
    # returns None

    input_image = face_recognition.load_image_file(image_location)
    # uses face_recognition to load image into input_image

    input_face_locations = face_recognition.face_locations(input_image, model=model)
    # locates faces in the loaded image according to the assigned model and saves it in input_face_locations
    # generates a tuple containing the coordinates for drawing each face's bounding box

    pillow_image = Image.fromarray(input_image)
    # generates a PIL image for drawing bounding boxes

    draw = ImageDraw.Draw(pillow_image)
    # creates draw image for drawing bounding boxes

    for bounding_box in input_face_locations:
        print("FACE DETECTED", bounding_box)
        # prints located bounding boxes

        _display_face(draw, bounding_box, "FACE DETECTED")
        # calls _display_face passing the draw image, bounding_box, and a label for the bounding box

    del draw
    # deletes current draw

    pillow_image.show()
    # displays image with bounding boxes


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

