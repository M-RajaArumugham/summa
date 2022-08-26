from bs4 import BeautifulSoup
import requests
import re
import socket
import json
pages_data = [0]
list=[]
def get_pages(params):
    pages = int(params+"0")
    for i in range(1, pages):
        if i % 10 == 0:
            pages_data.append(i)


def get_dork(params):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    for i in pages_data:
        url = "https://www.google.com/search?q=" + \
            params + "&start=" + str(i)
        dork = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
        for j in dork.find_all('div', attrs={'class': 'g'}):
            result = j.find('a', href=True)['href']
            list.append(result)

pages = input("Input Pages : ")
dork = "site: "+str(var)
get_pages(pages)
get_dork(dork)




host = list[1]
url = re.compile(r"https?://(www\.)?")
hostname = url.sub('', str(host)).strip().strip('/')


def facebook():
    if fb is None:
        return "No Facebook Link Is Found"
    return fb['href']


def instagram():
    if insta is None:
        return "No Instagram Link Is Found"
    return insta['href']


def twitter():
    if twt is None:
        return "No Twitter Link Is Found"
    return twt['href']


def youtube():
    if y is None:
        return "No Youtube Link Is Found"
    return y['href']


headers = {
    'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
url = str(host)
r = requests.get(url, headers)
soup = BeautifulSoup(r.content, 'html.parser')
title = soup.find("title").text
fb = soup.find('a', {'href': re.compile("https?://(www\\.)?facebook\\.com/[^(share)]?(\\w+\\.?)+")})
insta = soup.find('a', {'href': re.compile("https?://(www\\.)?instagram\\.com/[^(share)]?(\\w+\\.?)+")})
twt = soup.find('a', {'href': re.compile("https?://(www\\.)?twitter\\.com/[^(share)]?(\\w+\\.?)+")})
y = soup.find('a', {'href': re.compile("https?://(www\\.)?youtube\\.com/[^(share)]?(\\w+\\.?)+")})
fab = facebook()
i = instagram()
t = twitter()
y = youtube()

print("TITLE:")
print(title)
print("LINKS:")
print(fab)
print(i)
print(t)
print(y)