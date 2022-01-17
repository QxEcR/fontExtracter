from funcs import extractFontFromPage, extractFontFromCSS
from Excel import Excel

fileName = "Font_Example.xlsx"  # Put the excel file name Here
excel = Excel(fileName)


def main():
    # getting the inputs from the excel object
    input_urls = excel.getInputs()

    #for every url in the list: extract the font info then write it to the excel sheet
    for url in input_urls:
        font_within_page = extractFontFromPage(url)
        excel.writeToExcel(False, font_within_page)

        font_within_css = extractFontFromCSS(url)
        excel.writeToExcel(True, font_within_css)


if __name__ == '__main__':
    main()

# for i in inputs:
#     req = requests.get(i)
#     soup = BeautifulSoup(req.content, "html.parser")
#     css = re.search(r'rel="stylesheet"', soup.prettify())
#     print(css.group())
#     print()
