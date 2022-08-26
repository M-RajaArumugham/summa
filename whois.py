from bs4 import BeautifulSoup
import requests
import re
import socket
import json
pages_data = [0]
list=[]
faceurl=[]
instaurl=[]
youtubeurl=[]
twitterurl=[]
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
def get_dork_face(params):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    for i in pages_data:
        url = "https://www.google.com/search?q=" + \
            params + "&start=" + str(i)
        dork = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
        for j in dork.find_all('div', attrs={'class': 'g'}):
            result = j.find('a', href=True)['href']
            faceurl.append(result)
        return faceurl[0]
def get_dork_insta(params):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    for i in pages_data:
        url = "https://www.google.com/search?q=" + \
            params + "&start=" + str(i)
        dork = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
        for j in dork.find_all('div', attrs={'class': 'g'}):
            result = j.find('a', href=True)['href']
            instaurl.append(result)
        return instaurl[0]
def get_dork_twitter(params):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    for i in pages_data:
        url = "https://www.google.com/search?q=" + \
            params + "&start=" + str(i)
        dork = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
        for j in dork.find_all('div', attrs={'class': 'g'}):
            result = j.find('a', href=True)['href']
            twitterurl.append(result)
        return twitterurl[0]
def get_dork_youtube(params):
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
    for i in pages_data:
        url = "https://www.google.com/search?q=" + \
            params + "&start=" + str(i)
        dork = BeautifulSoup(requests.get(url, headers=headers).text, "html.parser")
        for j in dork.find_all('div', attrs={'class': 'g'}):
            result = j.find('a', href=True)['href']
            youtubeurl.append(result)
        return youtubeurl[0]
pages = '1'
dork = input("Input Data : ")
dork="site: " + dork
get_pages(pages)
get_dork(dork)



def facebook():
    if fb is None:
        return get_dork_face(dork+"facebook")
    return fb['href']


def instagram():
    if insta is None:
        return get_dork_insta(dork+"instagram")
    return insta['href']


def twitter():
    if twt is None:
        return get_dork_twitter(dork + "twitter")
    return twt['href']


def youtube():
    if y is None:
        return get_dork_youtube(dork+"youtube")
    return y['href']


headers = {
    'User Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'}
url = list[0]
r = requests.get(url, headers)
soup = BeautifulSoup(r.content,'html.parser')
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
print("WEBSITE:",list[0])
print("FACEBOOK:",fab)
print("INSTAGRAM:",i)
print("TWITTER:",t)
print("YOUTUBE:",y)
import csv  # for reading/writing in CSV file
import re  # for regular expressions
import requests  # for opening web page

# Create phone number regular expression
phone_regex = re.compile(r'''(
                        (\d{3}|\(\d{3}\))?
                        (\s|-|\.)?
                        (\d{3})
                        (\s|-|\.)
                        (\d{4})
                        (\s*(ext|x|ext.)\s*(\d{2,5}))?)
                        (\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$
                        (?:(?:\+|0{0,2})91(\s*[\ -]\s*)?|[0]?)?[456789]\d{9}|(\d[ -]?){10}\d$
                        ^=\+91 0120 3305555$''', re.VERBOSE)

# Create email id regular expression
email_regex = re.compile(r'''(
                        [a-zA-Z0-9._%+-]+
                        @
                        [a-zA-Z0-9.-]+
                        (\.[a-zA-Z]{2,4}))''', re.VERBOSE)

# Open URLs from CSV file and
# with open("web_urls.csv") as csv_file:
# csv_reader = csv.reader(csv_file)

# for row in csv_reader:
page_url = str(url)+"contacts"

page_data = requests.get(page_url)

# Convert byte data to a string
page_html = str(page_data.content)
matches = []
matc = []
for groups in phone_regex.findall(page_html):
    phone_numbers = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phone_numbers += ' x' + groups[8]
        matches.append(phone_numbers)
for groups in email_regex.findall(page_html):
    matc.append(groups[0])

if (len(matc) > 0):
    print("Email:")
    print(matc[0])
else:
    print("Not found")