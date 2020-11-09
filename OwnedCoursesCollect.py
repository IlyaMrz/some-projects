# collect to the file all Udemy courses links which I own.
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_argument(
    "user-data-dir=C:\\Users\\pk111\\AppData\\Local\\Google\\Chrome\\")


driver = "C:\\Games\\VScodeProjects\\udemy_automat\\chromedriver.exe"
chrome_browser = webdriver.Chrome(
    driver, chrome_options=chrome_options)  # here
chrome_browser.maximize_window()


def getpage(pageNumber):
    chrome_browser.get(
        f'https://www.udemy.com/home/my-courses/learning/?p={pageNumber}')
    time.sleep(3)
    sp = chrome_browser.page_source
    soup = BeautifulSoup(sp, 'html.parser')
    return soup


def getMaxPage(soup):
    maxPage = soup.find("ul", {"class": "pagination pagination-expanded"})
    maxPage = maxPage.findChildren('li')[-2].get_text()
    return maxPage


def findAndWriteLinks(innerSoup):
    z = innerSoup.findAll('a', {'class': 'card--learning__details'})
    for i in z:
        try:
            courseLink = 'https://www.udemy.com' + \
                str(i["href"]).replace("learn/", "")
            print(courseLink)
            with open("MyCourses.txt", 'a') as file:
                file.write(courseLink+'\n')
        except:
            pass


def main():
    pageNumber = 1
    while True:
        soup = getpage(pageNumber)
        findAndWriteLinks(soup)
        if pageNumber == 1:
            maxPage = getMaxPage(soup)
        if pageNumber < int(maxPage):
            pageNumber += 1
        else:
            break


main()
print("Done!")
chrome_browser.close()
