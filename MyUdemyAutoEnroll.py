from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from pprint import pprint


headers = {
    "User-agent": "Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5"}
driver = "C:\\Games\\VScodeProjects\\udemy_automat\\chromedriver.exe"
chrome_browser = webdriver.Chrome(driver)
chrome_browser.maximize_window()
# z = int(input('How Much pages to parse? there is max 17 pages '))

url = 'https://couponscorpion.com/category/100-off-coupons/'

rawUrl = requests.get(url, headers=headers).text
soup = BeautifulSoup(rawUrl, 'html.parser')
# link1 = soup.find_all(
#     'div', {"class": 'newsdetail newstitleblock rh_gr_right_sec'})
# for link in link1:
#     print(link['href'])
# pprint(link1)


links = []
for div in soup.find_all(
        'div', {"class": 'newsdetail newstitleblock rh_gr_right_sec'}):
    for a in div.select('a'):
        links.append(a['href'])


pprint(f'{links} \n ================ raw links above ============')
# Get scorpion links and afet get LIST of links directly to courses


def getUdemyLinks(links):
    udemy_links = []
    for link in links:
        link_req = requests.get(link, headers=headers).text
        soup2 = BeautifulSoup(link_req, 'html.parser')
        udemy_links.append(soup2.find(
            'span', class_="rh_button_wrapper").find('a').get('href'))
        print(udemy_links)

        # for span in soup.find_all('div', {'class': 'priced_block clearfix  inline_compact_btnblock mobile_block_btnclock mb0'}):
        #     for a in span.select('a'):
        #         print(f'======spann{a}')
        #         udemy_links.append(a['href'])
    return udemy_links


print(getUdemyLinks(links))

# go to udemy courses from list of links and click add button if FREE

# after a page click card and enroll if card cost == 0

# repeat so many times as pages entered
