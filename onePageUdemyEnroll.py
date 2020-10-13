# grabs link from yofreesamples.com/courses/free-discounted-udemy-courses-list/
#  and autoenroll them
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from pprint import pprint
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time


# Change path to file with 2 lines email and password
with open('C:\\Games\\VScodeProjects\\udemy_automat\\pas.txt') as f:
    lines = f.readlines()
    email, password = lines

# Change path to webdriver path
driver = "C:\\Games\\VScodeProjects\\udemy_automat\\chromedriver.exe"
chrome_browser = webdriver.Chrome(driver)
chrome_browser.maximize_window()


def getLinks():
    links = []
    res = requests.get(
        'https://yofreesamples.com/courses/free-discounted-udemy-courses-list/').text
    soup = BeautifulSoup(res, 'html.parser')
    for i in soup.findAll('a', {'class': 'btn btn-md btn-success'}):
        link = i['href']
        links.append(link)
        print(link)
    return links


def udemy_login(email_text, password_text):
    print('udemy login')
    chrome_browser.get("https://www.udemy.com/join/login-popup/")

    email = chrome_browser.find_element_by_name("email")
    password = chrome_browser.find_element_by_name("password")

    email.send_keys(email_text)
    password.send_keys(password_text)

    chrome_browser.find_element_by_name("submit").click()


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
    udemy_login(email, password)
    for link in getLinks():
        try:
            redeemUdemyCourse(link)
        except KeyboardInterrupt:
            print('===== user interruption =====')
            break
        except BaseException as e:
            print("Unable to enroll for this course either because you have already claimed it or the browser window has been closed!")


main()
print('done')
chrome_browser.close()
