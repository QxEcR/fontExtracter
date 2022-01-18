from funcs import extractFontlinksFromPage, extractFontFamilyFromPage, extractFontFamilyFromCSS
from Excel import Excel


def main():
    fileName = "Font_Example.xlsx"  # Put the excel file name Here
    excel = Excel(fileName)

    input_urls = excel.getInputs()

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
