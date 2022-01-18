from funcs import extractFontlinksFromPage, extractFontFamilyFromPage, extractFontFamilyFromCSS
from Excel import Excel


def main():
    fileName = "Font_Example.xlsx"  # Put the excel file name Here
    excel = Excel(fileName)

    # getting the inputs from the excel object
    input_urls = excel.getInputs()

    # for every url in the list: extract the font info then write it to the excel sheet
    for url in input_urls:
        url = url[:len(url)-1] if url[-1] == '/' else url

        font_links_within_page = extractFontlinksFromPage(url)
        if font_links_within_page:
            excel.writeToExcel(url, False, font_links_within_page)

        font_family_within_page = extractFontFamilyFromPage(url)
        if font_family_within_page:
            excel.writeToExcel(url, True, font_family_within_page)

        font_family_within_css = extractFontFamilyFromCSS(url)
        if font_family_within_css:
            excel.writeToExcel(url, True, font_family_within_css)


if __name__ == '__main__':
    main()
