from face_detector import recognize_faces
from face_detector_opencv import detector_face
import os


if __name__ == '__main__':
    paths0 = []
    path_dir = 'images/0--Parade'
    for dirname, _, filenames in os.walk(path_dir):
        for filename in filenames:
            paths0 += [(os.path.join(dirname, filename))]
    print(len(paths0))

    #detector_face(paths0)
    recognize_faces(paths0)


