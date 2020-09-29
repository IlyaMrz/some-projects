import requests
from bs4 import BeautifulSoup
from pprint import pprint


def multiPageRes(pageNumber=1):
    res = requests.get('http://news.ycombinator.com/news?p=1').text
    if pageNumber > 1:
        for i in range(2, pageNumber):
            res = res + \
                (requests.get('http://news.ycombinator.com/news?p='+str(i)).text)

    return res


z = int(input('How Much pages to parse? '))
y = int(input('Enter a minimum score for news to parse: '))

res = multiPageRes(z)


soup = BeautifulSoup(res, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > y:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint(create_custom_hn(links, subtext))
