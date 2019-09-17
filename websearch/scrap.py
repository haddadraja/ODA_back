from bs4 import BeautifulSoup
from selenium import webdriver
from .image_search import image_search

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
browser = webdriver.Chrome('websearch/chromedriver', chrome_options=options)


def find_shopping_url(url):
    browser.get(url)
    url_shopping = browser.find_element_by_xpath('//*[@id="hdtb-msb-vis"]/div[4]/a').get_attribute('href')
    return url_shopping


def scrap_similar(url):
    browser.get(url)
    inner_html = browser.execute_script("return document.body.innerHTML")
    soup = BeautifulSoup(inner_html, "html.parser")
    elements = soup.find_all('div', {'class': 'sh-dgr__content'})
    objects = []

    for elem in elements:
        obj = {
            'title': elem.find('a', {'class': 'EI11Pd'}).text,
            'price': elem.find('span', {'class': 'Nr22bf'}).text,
            'image': elem.find('img')['src']
        }
        objects.append(obj)
    return objects
