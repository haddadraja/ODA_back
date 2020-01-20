# ODA_back

### 1 : YOLOV3 WEIGHTS
Download yolov3 weights for the pretrained neural network and save it in the folder 'objectDetector/yolo-coco'
- https://pjreddie.com/media/files/yolov3.weights

### 2 : Set the good chrome navigator driver : Download the same driver version that chrome driver on your laptop from https://chromedriver.chromium.org/downloads
#### Default : mac os chrome driver
- Set it in websearch/scrap.py (LINE 9 : WHERE : browser = webdriver.Chrome('websearch/chromedriver', chrome_options=options))

### 3 : Run application :
##### By default product file image to search is set at LINE 46 in main.py, change the path to a new image to test others.
- pipenv shell
- python main.py

### 4 : Open URL http://localhost:5000/search and wait for response.
