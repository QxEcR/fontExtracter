import requests
from bs4 import BeautifulSoup
import re


def extractFontlinksFromPage(url):
    list = []
    try:
        req = requests.get(url)
    except:
        print(f"somthing went wrong with requesting {url}")
        return None

    try:
        soup = BeautifulSoup(req.content, "html.parser")
        links = soup.find_all('link')

        for link in links:
            if "font" in str(link):
                font_link = re.findall(r'href="(.*?)"', str(link))

                if "http" not in str(font_link):
                    list.append(font_link[0])
                if "?" in str(font_link):
                    list.append(font_link[0])

        return list
    except:
        print(f"could not parse content from {url}")
        return None


def extractFontFamilyFromPage(url):
    try:
        req = requests.get(url)
    except:
        print(f"somthing went wrong with requesting {url}")
        return None

    try:
        soup = BeautifulSoup(req.content, "html.parser")
        fontFamilies = re.findall(r'font-family:(.*?);', str(soup))
        return fontFamilies
    except:
        print(f"could not parse content from {url}")
        return None


def extractFontFamilyFromCSS(url):
    list = []

    try:
        req = requests.get(url)
    except:
        print(f"somthing went wrong with requesting {url}")
        return None

    try:
        soup = BeautifulSoup(req.content, "html.parser")
        links = soup.find_all('link')

        for link in links:
            if "stylesheet" in str(link):
                font_link = re.findall(r'href="(.*?)"', str(link))
                if "http" not in font_link[0] and "bootstrap" not in font_link[0]:
                    for i in parseCSSForFontFamily(url+font_link[0]):
                        list.append(str(i))

        return list
    except:
        print(f"could not parse content from {url}")
        return None

def parseCSSForFontFamily(url):
    try:
        req = requests.get(url)
    except:
        print(f"somthing went wrong with requesting {url}")
        return None
    
    try:
        soup = BeautifulSoup(req.content, "html.parser")
        fontFamilies = re.findall(r'font-family:(.*?);', str(soup))
        return fontFamilies
    except:
        print(f"could not parse content from {url}")
        return None