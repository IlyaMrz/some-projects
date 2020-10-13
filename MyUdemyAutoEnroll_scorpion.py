# Script is broken
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
# z = int(input('How Much pages to parse? there is max 17 pages '))


def getScorpLinks(pagenumber):
    url = f'https://couponscorpion.com/category/100-off-coupons/page/' + \
        str(pagenumber)
    rawUrl = requests.get(url).text
    soup = BeautifulSoup(rawUrl, 'html.parser')

    links = []
    for div in soup.find_all(
            'div', {"class": 'newsdetail newstitleblock rh_gr_right_sec'}):
        for a in div.select('a'):
            links.append(a['href'])
    pprint(f'{links}================ raw links above ============')
    return links


# pprint(f'{links}================ raw links above ============')
# Get scorpion links and afet get LIST of links directly to courses


def udemy_login(email_text, password_text):
    chrome_browser.get("https://www.udemy.com/join/login-popup/")

    email = chrome_browser.find_element_by_name("email")
    password = chrome_browser.find_element_by_name("password")

    email.send_keys(email_text)
    password.send_keys(password_text)

    chrome_browser.find_element_by_name("submit").click()


def reedemCourse(url):

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


def getUdemyPhpLinks(links):
    for link in links:
        print(f'link is >>>>>>>>>> {link}')
        time.sleep(2)
        chrome_browser.get(link)
        time.sleep(10)
        chrome_browser.find_element_by_xpath(
            '//button[@class="align-right primary slidedown-button"]').click()
        content = chrome_browser.page_source
        soup = BeautifulSoup(content, 'html.parser')
        course_link = soup.find_all('span', {'class': "rh_button_wrapper"})
        for i in course_link:
            phplink = i.find('a', href=True)
            phplink = phplink['href']
            print(f'php link >>>>>>>>> {phplink}')
            if phplink is None:
                print('No Links Found')
        try:
            reedemCourse(phplink)
        except:
            print('something goes wrong')


def main():
    loop = 0
    pagenumber = 1
    while pagenumber < 5:
        links = getScorpLinks(pagenumber)
        if loop == 0:
            udemy_login(email, password)

        getUdemyPhpLinks(links)
        pagenumber += 1
        loop += 1


main()


print('done')
chrome_browser.close()
