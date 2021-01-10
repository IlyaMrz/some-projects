# blog parser to txt. alexmutnyi.com
import requests
from bs4 import BeautifulSoup
import codecs
import re


fileObj = codecs.open( "D:\\Downloads\\AlexMutnyi_0-107\\html.txt", "r", "utf_8_sig" )
text = fileObj.read()
fileObj.close()

soup = BeautifulSoup(text, 'html.parser')
elem = soup.findAll('a',{"class":"blog-link-hover-color"})
listOflinks = []
for i in elem:
    link = i['href']
    listOflinks.insert(0,link)

unacceptables = ['/','\\',':','*','>','\"','<','|','?','\\n','n']
count = 0
for ilink in listOflinks:
    res = requests.get(ilink).text
    soup = BeautifulSoup(res,'html.parser')
    title = soup.title.text
    text = soup.find('div',{
        'class':'post-content__body'
    })
    text2 = [''.join(s.findAll(text=True))for s in text.findAll('p')]
    print(text2)
    print(title)
    for z in title:
        if z in unacceptables:
            title = title.replace(z,'')
            print(title)    
    title = title.replace('\\n','')
    title = title.replace('\n','')
    filename = str(count) + '. ' + title.strip(" \n")
    writeFile = open(
        f'D:\\Downloads\\AlexMutnyi_0-107\\{filename}.txt', 'w')
    for i in text2:
        try:
            writeFile.write(i)
        except:
            pass
    writeFile.close()
    count+=1
    