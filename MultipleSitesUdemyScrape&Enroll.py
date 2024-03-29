# scrapes Udemy coupon links from 3 sites
# discudemy.com tutorialbar.com yofreesamples.com
# then it removes duplicates and enrolls them on Udemy. Python 3.6+
import re
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.chrome.options import Options
from pprint import pprint
from sys import exit

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# ============================= settings here =================================
# =============================================================================
# if want login with pass and email
# Change path to file with 2 lines email and password
# (Also uncomment in "main()" function udemy_login )
# and delete 'chrome options' in "here" mark. BUT BETTER USE COOKIES!!!
#
# with open('C:\\Games\\VScodeProjects\\udemy_automat\\pas.txt') as f:
#     lines = f.readlines()
#     email, password = lines

# change path to your user chrome data (to use cookies)
# Probably u need just change "pk111" to your PC user name
# First time u need log in manually
chrome_options = Options()
chrome_options.add_argument(
    "user-data-dir=D:\\MyTemp\\webDriver_auto\\temp")

chrome_options.add_argument("window-size=1920,1080")
chrome_options.add_argument(
    "user-agent=Chrome/88.0.4324.150 (Windows NT 10.0; Win64; x64)")
# Removing the Flag (Navigator.Webdriver) before it is even set (only google chrome)
chrome_options.add_argument('--disable-blink-features=AutomationControlled')
# Change path to webdriver path
driver = "C:\\Games\\VScodeProjects\\udemy_automat\\chromedriver.exe"
chrome_browser = webdriver.Chrome(
    driver, options=chrome_options)  # here
chrome_browser.maximize_window()

chrome_browser.get('https://www.udemy.com/home/my-courses/learning/')
start_page = 1  # to scrape coupons
number_of_pages = 5  # scrape until this page number
quantity_yofree = 50  # how much coupons scrape from yofreesamples.com max ~130
# use OwnedCoursesCollect.py to collect owned courses to txt
checkLink = True  # True to check and not enroll if course already owned
# file with all your courses which u own
myCoursesFile = "C:\\Games\\VScodeProjects\\some-projects\\MyCourses_1.txt"
with open(myCoursesFile, 'r') as f:
    readFileWithCourses = f.read().splitlines()
# =============================================================================


def udemy_login(email_text, password_text):
    print('udemy login')
    chrome_browser.get("https://www.udemy.com/join/login-popup/")

    email = chrome_browser.find_element_by_name("email")
    password = chrome_browser.find_element_by_name("password")

    email.send_keys(email_text)
    password.send_keys(password_text)

    chrome_browser.find_element_by_name("submit").click()


def redeemUdemyCourse(url):
    print('--------------------------------------------------')
    print("foo redeemudemyCourse")
    chrome_browser.get(url)
    print("Trying to Enroll for: " + chrome_browser.title)
    print(url)
    element_price_present = None  # and sleep to prevent scrape old page source
    time.sleep(2)
    element_price_present = EC.presence_of_element_located(
        (By.XPATH, "//div[@data-purpose='price-text-container']"))
    try:
        WebDriverWait(chrome_browser, 10).until(element_price_present)
    except:
        print("passing line 76 in main loop")
        pass

    priceHtml = chrome_browser.find_element_by_xpath(
        "//div[@data-purpose='purchase-section']").text
    if "100% off" in priceHtml:
        print("Course is truly free and new. So we are getting it!")
        # Enroll Now 1
        element_present = EC.presence_of_element_located(
            (By.XPATH, "//button[@data-purpose='buy-this-course-button']"))
        WebDriverWait(chrome_browser, 10).until(element_present)

        udemyEnroll = chrome_browser.find_element_by_xpath(
            "//button[@data-purpose='buy-this-course-button']")  # Udemy
        # check if course FREE 100% and if yes click and add to DB
        linkOFCourse = chrome_browser.current_url
        udemyEnroll.click()

        global trueNewValidCourses
        trueNewValidCourses += 1

        # Enroll Now 2
        element_present = EC.presence_of_element_located(
            (By.XPATH, "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[4]/button[1]"))
        WebDriverWait(chrome_browser, 10).until(element_present)
        # Assume sometimes zip is not required because script was originally pushed without this
        # try:
        #     zipcode_element = chrome_browser.find_element_by_id(
        #         "billingAddressSecondaryInput")
        #     zipcode_element.send_keys(zipcode)

        #     # After you put the zip code in, the page refreshes itself and disables the enroll button for a split second.
        #     time.sleep(1)
        # except NoSuchElementException:
        #     pass

        time.sleep(4)
        udemyEnroll = chrome_browser.find_element_by_xpath(
            "/html[1]/body[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/form[1]/div[2]/div[1]/div[4]/button[1]")  # Udemy
        udemyEnroll.click()
        WebDriverWait(chrome_browser, 15).until(
            EC.url_contains('success'))

        if (checkLink == True) and (("success" in chrome_browser.current_url)):
            addCourseLinkToBD(linkOFCourse)
        else:
            print('course didn\'t added to DB')
            print(linkOFCourse)
            print('_____!!!!!_____')
        time.sleep(2)


def getDiskUdemyLinks(page):
    print('PLEASE WAIT WE ARE GETTING Disk UDEMY LINKS ><><><><><><><><')
    res = requests.get(
        f'https://www.discudemy.com/all/{str(page)}', headers=headers).text
    soup = BeautifulSoup(res, 'html.parser')
    elems = soup.findAll('section', {"class": 'card'})
    truelinks = []
    for i in elems:
        try:
            price = i.select('div.meta > span:nth-child(2)')[0].text.strip()
            if len(price) > 3:
                link = i.select('a')
                link = link[0]['href']
                try:
                    findUdemylink(link, truelinks)
                except:
                    print('Broken DISCUDEMY link PASSED')
        except IndexError:
            pass
    return(truelinks)


def getOnePageLinks():
    links2 = []
    res = requests.get(
        'https://yofreesamples.com/courses/free-discounted-udemy-courses-list/', headers=headers).text
    soup = BeautifulSoup(res, 'html.parser')
    for i in soup.findAll('a', {'class': 'btn btn-md btn-success'}):
        link = i['href']
        links2.append(link)
    print('received one page links')
    return links2


def trueUdemylink(link, truelinks):
    res3 = requests.get(link, headers=headers).text
    soup3 = BeautifulSoup(res3, 'html.parser')
    for item in soup3.find('div', {'class': 'ui segment'}):
        try:
            a = item['href']
            truelinks.append(a)
            print(f'DiscUdemyLINK {a}')
        except:
            pass


def findUdemylink(link, truelinks):
    res2 = requests.get(link, headers=headers).text
    soup2 = BeautifulSoup(res2, 'html.parser')
    link2 = soup2.find('a', {'class': 'ui big inverted green button discBtn'})
    link2 = link2['href']
    trueUdemylink(link2, truelinks)


def getUdemyLink(url):
    response = requests.get(
        url=url, headers=headers
    )

    soup = BeautifulSoup(response.content, 'html.parser')

    linkForUdemy = soup.find(
        'span', class_="rh_button_wrapper").find('a').get('href')

    return linkForUdemy


def getTutorLinks(page):
    url = "https://www.tutorialbar.com/all-courses/"+"page/"+str(page)+"/"
    response = requests.get(url=url, headers=headers)

    soup = BeautifulSoup(response.content, 'html.parser')

    links = soup.find('div', class_="rh-post-wrapper").find_all('a')
    courses = []

    x = 0
    for i in range(12):
        courses.append(links[x].get('href'))
        x = x+3

    udemyLinks = []
    linkCounter = 0

    for course in courses:
        try:
            udemyLinks.append(getUdemyLink(course))
            print("Received TUTOR Link " + str(linkCounter+1) +
                  ": "+udemyLinks[linkCounter])
            linkCounter += 1
        except:
            print(
                f'____ getUdemyLink TUTOR failed for one course link {course} .. passing')
    return udemyLinks


def alllinks():
    page = start_page
    list2 = getOnePageLinks()
    alllinks = []
    while page <= number_of_pages:
        print(f'_____ sraping from PAGE #{page}')
        list1 = getDiskUdemyLinks(page)
        list3 = getTutorLinks(page)
        page += 1
        alllinks += list1
        alllinks += list3
    alllinks += list2[:quantity_yofree]
    return alllinks


def checkIfCourseOwned(link):
    try:
        print('check')
        tlink = link.split('?')[0]
        if tlink in readFileWithCourses:
            state = True
            print("course already owned")
        else:
            state = False
    except:
        state = False
    return state


def addCourseLinkToBD(link):
    try:
        link, coupon = link.split('?')[0], link.split('?')[1]
        with open(myCoursesFile, 'r') as f:
            file = f.read().splitlines()
        if link not in file:
            with open(myCoursesFile, 'a') as f:
                f.write(link+'\n')
                print(f'New link added to DataBase. Link -> {link}')
                print(f'Coupon -> ?{coupon}')
        else:
            print('seems like this course already in DB so we passing "addin to DB"')
    except:
        print("failed to add link to DB")
        pass


def checkCourseCountDB():
    print('\nchecking coincidence amount of courses Local DB and Site...')
    try:
        chrome_browser.get('https://www.udemy.com/home/my-courses/learning/')
        element_present = EC.presence_of_element_located(
            (By.XPATH, "//div[@class='pager-label']"))
        WebDriverWait(chrome_browser, 10).until(element_present)
        count = chrome_browser.find_element_by_xpath(
            "//div[@class='pager-label']").text
        countUdemy = int(re.search(r"\s\d*\s", count).group())
        localDB = sum(1 for line in open(myCoursesFile) if line.rstrip())
        if countUdemy == localDB:
            print(
                '\nGood. Local DB of courses contains exact number of courses as udemy.com')
            print(localDB)
        else:
            print(
                f'\nWARNING: Something wrong with DB. local:{localDB}. site:{countUdemy}')
            return False
    except:
        print('\nWhile checking amount of courses something goes wrong..')
        exit("Cannot check amount of courses on udemy. Maybe you logged off. Mission aborted!")


def main():
    # udemy_login(email, password)  # uncomment to use login with pass and email
    if checkLink:
        checkCourseCountDB()
    x = alllinks()
    uniqueCoupons = list(dict.fromkeys(x))  # ordered unique list
    print(f'all links: {len(x)}')
    print(f'unique links: {len(uniqueCoupons)}')
    for link in uniqueCoupons:
        try:
            if (checkLink == True):
                if (checkIfCourseOwned(link) == False):
                    redeemUdemyCourse(link)
            else:
                redeemUdemyCourse(link)
        except KeyboardInterrupt:
            print('===== user interruption =====')
            break
        except FileNotFoundError:
            print(
                f'There is no file ({myCoursesFile}). Check running directory and file, or disable checkLink')
        except BaseException:
            print("Unable to enroll for this course either because you have already claimed it or the browser window has been closed!")
            print(link)
    return len(x), len(uniqueCoupons)


trueNewValidCourses = 0
a, b = main()
print('===============================================================')
print(
    f' Done! Scraped {a} links, and {b} unique links.')
print(f'{trueNewValidCourses} truly new and valid courses were enrolled')
if checkLink:
    checkCourseCountDB()
print('===============================================================')

chrome_browser.close()
