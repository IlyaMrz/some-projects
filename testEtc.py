import time
from selenium import webdriver
from bs4 import BeautifulSoup
driver = webdriver.Chrome(
    r'C:\\Games\\VScodeProjects\\udemy_automat\\chromedriver.exe')
driver.maximize_window()
driver.get('https://couponscorpion.com/marketing/build-a-spare-room-studio-for-rapid-video-and-audio-creation/')
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
    phplink = link['href']
driver.get(phplink)
