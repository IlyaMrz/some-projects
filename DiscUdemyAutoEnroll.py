# grabs link from discudemy and autoenroll them
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
# from webdriver_manager.chrome import ChromeDriverManager
import time

with open('C:\\Games\\VScodeProjects\\udemy_automat\\pas.txt') as f:
    lines = f.readlines()
    email, password = lines

driver = "C:\\Games\\VScodeProjects\\udemy_automat\\chromedriver.exe"
chrome_browser = webdriver.Chrome(driver)
chrome_browser.maximize_window()


def udemy_login(email_text, password_text):
    print('udemy login')
    chrome_browser.get("https://www.udemy.com/join/login-popup/")

    email = chrome_browser.find_element_by_name("email")
    password = chrome_browser.find_element_by_name("password")

    email.send_keys(email_text)
    password.send_keys(password_text)

    chrome_browser.find_element_by_name("submit").click()


def trueUdemylink(link, truelinks):
    res3 = requests.get(link).text
    soup3 = BeautifulSoup(res3, 'html.parser')
    for item in soup3.find('div', {'class': 'ui segment'}):
        try:
            a = item['href']
            truelinks.append(a)
            pprint(a)
        except:
            pass


def findUdemylink(link, truelinks):
    res2 = requests.get(link).text
    soup2 = BeautifulSoup(res2, 'html.parser')
    link2 = soup2.find('a', {'class': 'ui big inverted green button discBtn'})
    link2 = link2['href']
    trueUdemylink(link2, truelinks)


def getLinks(page):
    print('PLEASE WAIT WE ARE GETTING UDEMY LINKS ><><><><><><><><')
    res = requests.get(f'https://www.discudemy.com/all/{str(page)}').text
    soup = BeautifulSoup(res, 'html.parser')
    elems = soup.findAll('section', {"class": 'card'})
    truelinks = []
    for i in elems:
        try:
            price = i.select('div.meta > span:nth-child(2)')[0].text.strip()
            if len(price) > 3:
                link = i.select('a')
                link = link[0]['href']
                findUdemylink(link, truelinks)
        except IndexError:
            pass
    return(truelinks)
# discounted link send to funct which find TRUE link to udemy


def redeemUdemyCourse(url):

    chrome_browser.get(url)
    print("Trying to Enroll for: " + chrome_browser.title)

    # Enroll Now 1
    element_present = EC.presence_of_element_located(
        (By.XPATH, "//button[@data-purpose='buy-this-course-button']"))
    WebDriverWait(chrome_browser, 10).until(element_present)

    udemyEnroll = chrome_browser.find_element_by_xpath(
        "//button[@data-purpose='buy-this-course-button']")  # Udemy
    udemyEnroll.click()

    # Enroll Now 2
    element_present = EC.presence_of_element_located(
        (By.XPATH, "//*[@id=\"udemy\"]/div[1]/div[2]/div/div/div/div[2]/form/div[2]/div/div[4]/button"))
    WebDriverWait(chrome_browser, 10).until(element_present)

    # Assume sometimes zip is not required because script was originally pushed without this
    try:
        zipcode_element = chrome_browser.find_element_by_id(
            "billingAddressSecondaryInput")
        zipcode_element.send_keys(zipcode)

        # After you put the zip code in, the page refreshes itself and disables the enroll button for a split second.
        time.sleep(1)
    except NoSuchElementException:
        pass

    udemyEnroll = chrome_browser.find_element_by_xpath(
        "//*[@id=\"udemy\"]/div[1]/div[2]/div/div/div/div[2]/form/div[2]/div/div[4]/button")  # Udemy
    udemyEnroll.click()


def main():
    page = 1
    loop = 0
    while page < 10:
        print("Please Wait: Getting the course list from tutorialbar.com...")
        print("Page: "+str(page)+", Loop run count: "+str(loop))
        if loop == 0:
            udemy_login(email, password)
        for link in getLinks(page):
            try:
                redeemUdemyCourse(link)
            except KeyboardInterrupt:
                print('===== user interruption =====')
                break
            except BaseException as e:
                print("Unable to enroll for this course either because you have already claimed it or the browser window has been closed!")
        page += 1
        loop += 1


main()
print('done')
chrome_browser.close()
