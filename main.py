import glob
import uuid
import cv2
from flask import Flask
from objectDetector.detector import run_detection
from websearch.scrap import run
import os

WORK_DIR = 'workDir'
app = Flask(__name__)


def save_detected_images(detected_images: list):
    if detected_images.__len__().__eq__(0):
        return False
    if not os.path.exists(WORK_DIR):
        os.mkdir(WORK_DIR)
    if not os.path.exists('workDirPersist'):
        os.mkdir('workDirPersist')
    for image_array in detected_images:
        #im = Image.fromarray(image_array)
        #im.save('/'.join([WORK_DIR, uuid.uuid1().__str__()]) + '.jpg')
        #im.save('/'.join(['workDirPersist', uuid.uuid1().__str__()]) + '.jpg')
        cv2.imwrite('/'.join(['workDirPersist', uuid.uuid1().__str__()]) + '.jpg', image_array)
        cv2.imwrite('/'.join([WORK_DIR, uuid.uuid1().__str__()]) + '.jpg', image_array)
    return True


def search_on_google_shopping():
    similar_products = {}
    images = glob.glob(WORK_DIR + '/*')
    print(">>> images saved", images)
    for image in images:
        similar_products[image] = run(image)
        os.remove(image)
    return similar_products


@app.route("/search")
def search_request():
    detected_objects = run_detection('test-images/ordi.jpg')
    if detected_objects is not None or detected_objects.__len__().__gt__(0):
        if save_detected_images(detected_objects):
            x = search_on_google_shopping()
            print('\n\n\n\n X', x)
            return x
    else:
        return []


if __name__ == '__main__':
    app.run()
