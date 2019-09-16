import os

import cv2
import numpy as np
from detector import run_detection

if __name__ == '__main__':
    detected_objects = run_detection('./test-images/choco.jpeg')
    print(len(detected_objects))
    for image in detected_objects:
        cv2.imshow("Image", image)
        cv2.waitKey(0)
