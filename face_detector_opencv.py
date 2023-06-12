import argparse

import cv2
from pathlib import Path


def recognize_faces_open_cv(paths0):
    # open-cv pre-trained face detection model
    # receives an array of images to be processed

    # parser = argparse.ArgumentParser(description='Code for Cascade Classifier tutorial.')
    # parser.add_argument('--face_cascade', help='Path to face cascade.',
    #                     default='haarcascade_frontalface_default.xml')
    # parser.add_argument('--eyes_cascade', help='Path to eyes cascade.',
    #                     default='haarcascade_eye.xml')
    # args = parser.parse_args()
    # face_cascade_name = args.face_cascade
    # eyes_cascade_name = args.eyes_cascade

    face_cascade = cv2.CascadeClassifier()
    # eyes_cascade = cv2.CascadeClassifier()
    # loads rules for frontal face detection from xml file into face_cascade object

    # if not face_cascade.load(cv2.samples.findFile(face_cascade_name)):
    #     print('--(!)Error loading face cascade')
    #     exit(0)
    # if not eyes_cascade.load(cv2.samples.findFile(eyes_cascade_name)):
    #     print('--(!)Error loading eyes cascade')
    #     exit(0)

    # face_cascade.load('haarcascade_frontalface_default.xml')
    # face_cascade.load('haarcascade_profileface.xml')

    face_cascade.load('haarcascade_frontalface_alt2.xml')

    for i, path in enumerate(paths0):
        print("Interation ", i)
        # loop for image processing, takes an image array produced in main
        # and iterates through it

        string = path
        # obtains path from current iterator

        file_name = path[string.find("/") + 1:]
        # string slicer finds / on path, gets its index adds one to it
        # slices the string from the index to the end and stores it in file_name
        # file_name will be used by the saving method bellow

        img = cv2.imread(path)
        # creates a cv2 image from current iterator image and saves it on img

        frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # converts img to shades of gray and saves in gray
        frame_gray = cv2.equalizeHist(frame_gray)

        try:
            #faces = face_cascade.detectMultiScale(frame_gray, 1.1, 3)
            faces = face_cascade.detectMultiScale(frame_gray, 1.04, 5)
            # faces object receives face_cascade and executes detectMultiScale taking
            # a gray image, a scale factor specifying how much the image size is reduced
            # and minNeighbors specifying how many neighbors each candidate rectangle should have to retain it

            with open("imagesM3/openCV/opencv.txt", "a") as file:
                # opens opencv.tx with value "a" for appending

                file.write(file_name + "\n" + str(len(faces)) + "\n")
                # writes current image's name and amount of detected faces

            for j, (x, y, w, h) in enumerate(faces):
                # loops through faces object setting bounding boxes for detected faces

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # draws bounding boxes on image

                with open("imagesM3/openCV/opencv.txt", "a") as file:
                    file.write("(" + str(x) + ", " + str(y) + ", " + str(w) + ", " + str(h) + ")\n")
                    # writes bounding boxes coordinates on opencv.txt
                print(str(x) + " - " + str(y))

                # faceROI = frame_gray[y:y + h, x:x + w]
                # # -- In each face, detect eyes
                # eyes = eyes_cascade.detectMultiScale(faceROI)
                # for (x2, y2, w2, h2) in eyes:
                #     eye_center = (x + x2 + w2 // 2, y + y2 + h2 // 2)
                #     radius = int(round((w2 + h2) * 0.25))
                #     img = cv2.circle(img, eye_center, radius, (255, 0, 0), 4)

            with open("imagesM3/openCV/opencv.txt", "a") as file:
                file.write("\n")

            save_image(file_name, img)
            # saves processed images with bounding boxes using filename

            print("\n")
        except:
            continue


def save_image(image_name, image):
    # receives an image name and an image file

    path = str(Path("imagesM3/openCV/") / image_name)
    # uses Path lib for solving multi OS / issue on directory tree

    cv2.imwrite(path, image)
    # saves image on the informed path using cv2 lib
