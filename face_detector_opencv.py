import cv2
from pathlib import Path


def recognize_faces_open_cv_frontal(paths0):
    # open-cv pre-trained face detection model
    # receives an array of images to be processed

    face_cascade = cv2.CascadeClassifier()
    # creates CascadeClassifier object and saves it on face_cascade

    face_cascade.load('haarcascade_frontalface_alt2.xml')
    # loads rules xml haarcascade_frontalface_alt2.xml into face_cascade

    for i, path in enumerate(paths0):
        print("Interation ", i)
        # image processing loop, takes an image address formed in the
        # main method and iterates through it

        string = path
        # obtains path from current iterator

        file_name = path[string.find("/") + 1:]
        # string slicer: finds / on path, gets its index adds one to it
        # slices the string from the index to the end and stores it in file_name
        # file_name will be used by the saving method bellow

        img = cv2.imread(path)
        # creates a cv2 image from current image and saves it on img object

        frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # converts img to shades of gray and saves in frame_gray

        frame_gray = cv2.equalizeHist(frame_gray)
        # applies threshold for black/white to frame_gray

        try:
            faces = face_cascade.detectMultiScale(frame_gray, 1.04, 3)
            # faces object receives face_cascade and executes detectMultiScale taking
            # frame_gray, a scale factor specifying how much the image size is reduced
            # and minNeighbors specifying how many neighbors each candidate rectangle should have to retain it

            with open("imagesM3Frontal/openCV/opencv.txt", "a") as file:
                # opens opencv.tx with value "a" for appending

                file.write(file_name + "\n" + str(len(faces)) + "\n")
                # writes current image's name and amount of detected faces

            for j, (x, y, w, h) in enumerate(faces):
                # loops through faces object setting bounding boxes for detected faces

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # draws bounding boxes on image

                with open("imagesM3Frontal/openCV/opencv.txt", "a") as file:
                    file.write("(" + str(x) + ", " + str(y) + ", " + str(w) + ", " + str(h) + ")\n")
                    # writes bounding boxes coordinates on opencv.txt
                print(str(x) + " - " + str(y))

            with open("imagesM3Frontal/openCV/opencv.txt", "a") as file:
                file.write("\n")
                # writes a new image to opencv.txt for separating
                # the analysed images' bounding boxes

            save_image(file_name, img, 'frontal')
            # saves processed images with bounding boxes using filename

            print("\n")
        except:
            continue


def recognize_faces_open_cv_profile(paths0):
    # open-cv pre-trained face detection model
    # receives an array of images to be processed

    face_cascade = cv2.CascadeClassifier()
    # creates CascadeClassifier object and saves it on face_cascade

    face_cascade.load('haarcascade_profileface.xml')
    # loads rules xml haarcascade_profileface.xml into face_cascade


    for i, path in enumerate(paths0):
        print("Interation ", i)
        # image processing loop, takes an image address formed in the
        # main method and iterates through it

        string = path
        # obtains path from current iterator

        file_name = path[string.find("/") + 1:]
        # string slicer finds / on path, gets its index adds one to it
        # slices the string from the index to the end and stores it in file_name
        # file_name will be used by the saving method bellow

        img = cv2.imread(path)
        # creates a cv2 image from current iterator image and saves it on img

        frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # converts img to shades of gray and saves in frame_gray

        frame_gray = cv2.equalizeHist(frame_gray)
        # applies threshold for black/white to frame_gray

        try:
            faces = face_cascade.detectMultiScale(frame_gray, 1.04, 3)
            # faces object receives face_cascade and executes detectMultiScale taking
            # frame_gray, a scale factor specifying how much the image size is reduced
            # and minNeighbors specifying how many neighbors each candidate rectangle should have to retain it

            with open("imagesM3Profile/openCV/opencv.txt", "a") as file:
                # opens opencv.tx with value "a" for appending

                file.write(file_name + "\n" + str(len(faces)) + "\n")
                # writes current image's name and amount of detected faces

            for j, (x, y, w, h) in enumerate(faces):
                # loops through faces object setting bounding boxes for detected faces

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # draws bounding boxes on image

                with open("imagesM3Profile/openCV/opencv.txt", "a") as file:
                    file.write("(" + str(x) + ", " + str(y) + ", " + str(w) + ", " + str(h) + ")\n")
                    # writes bounding boxes coordinates on opencv.txt
                print(str(x) + " - " + str(y))

            with open("imagesM3Profile/openCV/opencv.txt", "a") as file:
                file.write("\n")
                # writes a new image to opencv.txt for separating
                # the analysed images' bounding boxes

            save_image(file_name, img, 'profile')
            # saves processed images with bounding boxes using filename

            print("\n")
        except:
            continue


def recognize_faces_open_cv_default(paths0):
    # open-cv pre-trained face detection model
    # receives an array of images to be processed

    face_cascade = cv2.CascadeClassifier()
    # creates CascadeClassifier object and saves it on face_cascade

    face_cascade.load('haarcascade_frontalface_default.xml')
    # loads rules xml haarcascade_frontalface_default.xml into face_cascade


    for i, path in enumerate(paths0):
        print("Interation ", i)
        # image processing loop, takes an image address formed in the
        # main method and iterates through it

        string = path
        # obtains path from current iterator

        file_name = path[string.find("/") + 1:]
        # string slicer finds / on path, gets its index adds one to it
        # slices the string from the index to the end and stores it in file_name
        # file_name will be used by the saving method bellow

        img = cv2.imread(path)
        # creates a cv2 image from current iterator image and saves it on img

        frame_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # converts img to shades of gray and saves in frame_gray

        frame_gray = cv2.equalizeHist(frame_gray)
        # applies threshold for black/white to frame_gray


        try:
            faces = face_cascade.detectMultiScale(frame_gray, 1.04, 3)
            # faces object receives face_cascade and executes detectMultiScale taking
            # frame_gray, a scale factor specifying how much the image size is reduced
            # and minNeighbors specifying how many neighbors each candidate rectangle should have to retain it

            with open("imagesM3Default/openCV/opencv.txt", "a") as file:
                # opens opencv.tx with value "a" for appending

                file.write(file_name + "\n" + str(len(faces)) + "\n")
                # writes current image's name and amount of detected faces

            for j, (x, y, w, h) in enumerate(faces):
                # loops through faces object setting bounding boxes for detected faces

                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
                # draws bounding boxes on image

                with open("imagesM3Default/openCV/opencv.txt", "a") as file:
                    file.write("(" + str(x) + ", " + str(y) + ", " + str(w) + ", " + str(h) + ")\n")
                    # writes bounding boxes coordinates on opencv.txt
                print(str(x) + " - " + str(y))

            with open("imagesM3Default/openCV/opencv.txt", "a") as file:
                file.write("\n")
                # writes a new image to opencv.txt for separating
                # the analysed images' bounding boxes

            save_image(file_name, img, 'default')
            # saves processed images with bounding boxes using filename

            print("\n")
        except:
            continue


def save_image(image_name, image, type):
    # receives an image name and an image file and a type
    # saves the processed image on its appropriated path
    # according to the informed type
    # uses Path lib for solving multi OS / issue on directory tree

    if type == 'default':
        path = str(Path("imagesM3Default/openCV/") / image_name)
    elif type == 'frontal':
        path = str(Path("imagesM3Frontal/openCV/") / image_name)
    else:
        path = str(Path("imagesM3Profile/openCV/") / image_name)


    cv2.imwrite(path, image)
    # saves image on the informed path using cv2 lib
