# This program scrapes News from news.ycombinator.com and return sorted by votes
import requests
from bs4 import BeautifulSoup
from pprint import pprint
import time


# fetch all page sourses form all pages which requested
def multiPageRes(pageNumber=1):
    res = requests.get('http://news.ycombinator.com/news?p=1').text
    if pageNumber > 1:
        for i in range(2, pageNumber):
            time.sleep(1)
            res = res + \
                (requests.get('http://news.ycombinator.com/news?p='+str(i)).text)
    return res


z = int(input('How Much pages to parse? there is max 17 pages '))
y = int(input('Enter a minimum score for news to parse: '))

res = multiPageRes(z)

soup = BeautifulSoup(res, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['4___Votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        com_link = [a['href'] for a in subtext[idx].select('a:nth-child(6)')]
        com_link = 'https://news.ycombinator.com/' + \
            str(''.join(map(str, com_link)))
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > y:
                hn.append({'0': '-', '1___Title': title, '2___Link': href,
                           '3___Comments': com_link, '4___Votes': points})
    return sort_stories_by_votes(hn)


final_list = create_custom_hn(links, subtext)
pprint(final_list)

# writing scraped news to file:
with open("db.txt", 'w') as f:
    for i in final_list:
        for k, v in i.items():
            f.write(str(k)+'---' + str(v) + '\n')
