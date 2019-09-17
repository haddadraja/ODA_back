import glob
import uuid
from pprint import pprint
from flask import Flask
from PIL import Image
from objectDetector.detector import run_detection
from websearch.image_search import image_search
from websearch.scrap import scrap_similar, find_shopping_url
import os

WORK_DIR = 'workDir'
app = Flask(__name__)


def save_detected_images(detected_images: list):
    try:
        if not os.path.exists(WORK_DIR):
            os.mkdir(WORK_DIR)
        for image_array in detected_images:
            im = Image.fromarray(image_array)
            im.save('/'.join([WORK_DIR, uuid.uuid1().__str__()]) + '.jpg')
        return True
    except:
        return False


def search_on_google_shopping():
    similar_products = {}
    images = glob.glob(WORK_DIR + '/*')
    for image in images:
        similar_products[image] = scrap_similar(find_shopping_url(image_search(image)))
        os.remove(image)
    return similar_products


@app.route("/search")
def search_request():
    try:
        detected_objects = run_detection('objectDetector/test-images/sejour.jpg')
        if detected_objects is not None or detected_objects.__len__().__gt__(0):
            if save_detected_images(detected_objects):
                return search_on_google_shopping()
        else:
            return Exception('NO OBJECTS DETECTED IN THE IMAGE')
    except Exception as e:
        return Exception('ERROR ', e)


if __name__ == '__main__':
    app.run()