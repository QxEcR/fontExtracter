import requests
from bs4 import BeautifulSoup
import re



def extractFontFromPage(url):
    list = []

    req = requests.get(url)
    soup = BeautifulSoup(req.content, "html.parser")

    links = soup.find_all('link')
    for link in links:
        if "font" in str(link):
            font_link = re.findall(r'href="(.*?)"', str(link))
            list.append(font_link[0])
    return list


def extractFontFromCSS(url):
    list = []

    return list

