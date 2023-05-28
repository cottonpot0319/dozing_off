# stdlib
from typing import List, Dict, Optional
import os
import platform

# third party
import cv2

# self-made


class Camera(object):
    # def __init__(self):
    #     if platform.system() == 'Windows':
    #         os.environ['OPENCV_VIDEOIO_MSMF_ENABLE_HW_TRANSFORMS'] = '0'

    #     self.capture = capture

    # def find_the_camera(self):
    #     self.capture = cv2.VideoCapture(0, cv2.CAP_V4L2)

    #     if not self.capture.isOpend():
    #         print(f'==============================')
    #         print(f'Could not find the camera.')
    #         print(f'Come back with your camera on.')
    #         print(f'==============================')
    #         exit()

    def dozing_off(self):
        capture = cv2.VideoCapture(0, cv2.CAP_V4L2)

        if not capture.isOpend():
            print(f'==============================')
            print(f'Could not find the camera.')
            print(f'Come back with your camera on.')
            print(f'==============================')
            exit()

        while True:
            ret, img = capture.read()
            if not ret:
                print(f'========================')
                print(f'Image could not be read.')
                print(f'========================')
                break

            cv2.imshow('video image', img)

            key = cv2.waitKey(1) & 0xFF
            if key == 27:
                break

        capture.release()
        cv2.destroyAllWindows()
