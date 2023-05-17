import cv2
from pathlib import Path


def detector_face(paths0):
    # open-cv pre-trained face detection model
    # receives an array of images to be processed

    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # loads rules for frontal face detection from xml file into face_cascade object

    for i, path in enumerate(paths0):
        # string slicer, takes an image array produced in main
        # and iterates through it for obtaining folder name substring from path

        string = path
        # obtains path from current iterator

        file_name = path[string.find("/") + 1:]
        # finds / on path, gets its index adds one to it
        # slices the string from the index to the end and stores it in file_name
        # file_name will be used by the saving method bellow

        img = cv2.imread(path)
        # creates a cv2 image from current iterator image and saves it on img

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # converts img to shades of gray and saves in gray

        try:
            faces = face_cascade.detectMultiScale(gray, 1.04, 5)
            # faces object receives face_cascade and executes detectMultiScale taking
            # a gray image, a scale factor specifying how much the image size is reduced
            # and minNeighbors specifying how many neighbors each candidate rectangle should have to retain it

            with open("imagesSaved/openCV/opencv.txt", "a") as file:
                # opens opencv.tx with value "a" for appending

                file.write(file_name + "\n" + str(len(faces)) + "\n")
                # writes current image's name and amount of detected faces

            for j, (x, y, w, h) in enumerate(faces):
                # loops through faces object setting bounding boxes for detected faces

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # draws bounding boxes on image

                with open("imagesSaved/openCV/opencv.txt", "a") as file:
                    file.write("(" + str(x) + ", " + str(y) + ", " + str(w) + ", " + str(h) + ")\n")
                    # writes bounding boxes coordinates on opencv.txt
                print(str(x) + " - " + str(y))

            save_image(file_name, img)
            # saves processed images with bounding boxes using filename
        except:
            continue


def save_image(image_name, image):
    # receives an image name and an image file

    path = str(Path("imagesSaved/openCV/") / image_name)
    # uses Path lib for solving multi OS / issue on directory tree

    cv2.imwrite(path, image)
    # saves image on the informed path using cv2 lib
