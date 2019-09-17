import webbrowser

import requests

def image_search(filePath='/Users/ali/Desktop/CHAISE.jpg'): #chaise_grise
    search_url = 'http://www.google.hr/searchbyimage/upload'
    multipart = {'encoded_image': (filePath, open(filePath, 'rb')), 'image_content': ''}
    response = requests.post(search_url, files=multipart, allow_redirects=False)
    fetch_url = response.headers['Location']
    #webbrowser.open(fetch_url)
    return fetch_url
