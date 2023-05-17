from face_detector import recognize_faces
from face_detector_opencv import detector_face

import os

if __name__ == '__main__':
    paths0 = []
    # path_dir = 'images/0--Parade'
    # path_dir = 'images/1--Handshaking'
    # path_dir = 'images/4--Dancing'
    # path_dir = 'images/20--Family_Group'
    path_dir = 'images/imagesTest'
    # Junta todas as imagens de uma pasta em um array com o nome da pasta + nome do arquivo
    # Envia o array para os 2 métodos de reconhecimento de face
    for dirname, _, filenames in os.walk(path_dir):
        # receives a folder path as input, iterates through that folder coping the images
        # to paths0 array and assigns folder name + file name as image's name

        for filename in filenames:
            paths0 += [(os.path.join(dirname, filename))]

    detector_face(paths0)
    recognize_faces(paths0)
