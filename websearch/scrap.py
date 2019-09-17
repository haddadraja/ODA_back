from time import sleep

from bs4 import BeautifulSoup

from selenium import webdriver

from image_search import image_search
from selenium.webdriver.common.keys import Keys


def get_html(url):
    browser = webdriver.Chrome('/Users/ali/Downloads/chromedriver')
    browser.get(url) #navigate to page behind login
    innerHTML = browser.execute_script("return document.body.innerHTML") #returns the inner HTML as a string

    #x = BeautifulSoup(innerHTML, "html.parser")
    #possible_associated_search = x.find('a', {'class': 'fKDtNb'})
    #found_big_title = x.find('div', {'class': 'kno-ecr-pt kno-fb-ctx PZPZlf gsmt sKbx2c'}).text
    #x.find('a', {'class': 'q qs'})

    print('INNERHTML', innerHTML)




get_html(image_search())
