import requests
from bs4 import BeautifulSoup
import re
inputs = ["https://yoser.org/static/css/footerStyle.css", "https://www.youtube.com/", "https://www.youtube.com/s/desktop/d3411c39/cssbin/www-main-desktop-player-skeleton-rtl.css"]

for i in inputs:
    req = requests.get(i)
    soup = BeautifulSoup(req.content, "html.parser")
    fonts = re.findall(r'font-family: (.*?);', soup.prettify())
    weights = re.findall(r'font-weight: (.*?);', soup.prettify())
    sizes = re.findall(r'font-size: (.*?);', soup.prettify())
    print(f"{i} fonts are : ", end=" ")
    for font in fonts:
        print(font, end=", ")
    print()

    print(f"{i} weights are : ", end=" ")
    for weight in weights:
        print(weight, end=", ")
    print()

    print(f"{i} sizes are : ", end=" ")
    for size in sizes:
        print(size, end=", ")

    print()
    print()
    

# for i in inputs:
#     req = requests.get(i)
#     soup = BeautifulSoup(req.content, "html.parser")
#     css = re.search(r'rel="stylesheet"', soup.prettify())
#     print(css.group())
#     print()