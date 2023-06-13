from face_detector_opencv import recognize_faces_open_cv_frontal
from face_detector_opencv import recognize_faces_open_cv_default
from face_detector_opencv import recognize_faces_open_cv_profile

import os

if __name__ == '__main__':
    paths0 = []
    #path_dir = 'images/0--Parade'
    #path_dir = 'images/1--Handshaking'
    #path_dir = 'images/4--Dancing'
    #path_dir = 'images/20--Family_Group'
    path_dir = 'images/imagesTest'

    for dirname, _, filenames in os.walk(path_dir):
        # receives a folder path as input, iterates through that folder coping the images
        # to paths0 array and assigns folder name + file name as image's name

        for filename in filenames:
            paths0 += [(os.path.join(dirname, filename))]

    recognize_faces_open_cv_default(paths0)
    recognize_faces_open_cv_profile(paths0)
    recognize_faces_open_cv_frontal(paths0)

