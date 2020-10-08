import time
from selenium import webdriver
from bs4 import BeautifulSoup
path = r"C:\\Games\\VScodeProjects\\udemy_automat\\chromedriver.exe"
driver = webdriver.Chrome(path)
driver.maximize_window()
driver.get(
    'https://couponscorpion.com/marketing/the-ultimate-seo-social-media-digital-marketing-mastery/')
time.sleep(5)
driver.find_element_by_xpath(
    '//button[@class="align-right primary slidedown-button"]').click()
content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
course_link = soup.find_all('span', {'class': "rh_button_wrapper"})
for i in course_link:
    link = i.find('a', href=True)
    if link is None:
        print('No Links Found')
    b = link['href']
    print(link['href'])
driver.get(b)
