# collect to the file all Udemy courses links which I own.
import requests
from bs4 import BeautifulSoup
from pprint import pprint

with open("test.txt", 'r') as f:
    sp = f.read()

# Search for max page with courses
soup = BeautifulSoup(sp, 'html.parser')
z = soup.find("ul", {"class": "pagination pagination-expanded"})
z = z.findChildren('li')[-2].get_text()
print(f'Max page is {z}')

# Collect all courses on current page and go to next + count pages
z = soup.findAll('a', {'class': 'card--learning__details'})
for i in z:
    try:
        courseLink = 'https://www.udemy.com' + \
            str(i["href"]).replace("learn/", "")
        print(courseLink)
        with open("MyCourses.txt", 'a') as file:
            file.write(courseLink+'\n')
    except:
        pass
