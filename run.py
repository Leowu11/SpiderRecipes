import re
import lxml
import urllib.parse

from open_requests import open_http
from bs4 import BeautifulSoup

url = "https://www.douguo.com"
f_rest = open_http(url)
# print(f_rest)
soup = BeautifulSoup(f_rest, "html.parser")
header = soup.find(class_="imublo clearfix")

"""get channel"""
channel = []
for link in header.find_all("a"):
    channel.append(url + link.get('href'))
# print(channel)

# for link_1 in channel:
#     res_1=open_http(link_1)
#     print(res_1)
url_en = urllib.parse.quote(channel[0], safe='/:')
res_1 = open_http(url_en)
res_soup = BeautifulSoup(res_1, "html.parser")
# print(res_soup)
sort_more = res_soup.find(class_="sort-more")
# print(sort_more)
one_link = []
for more_link in sort_more.find_all("a"):
    one_link.append(url + more_link.get("href"))
one_link1 = one_link[0]
print(one_link1)

date_rest = open_http(one_link1)

deta_soup = BeautifulSoup(date_rest, "html.parser")
for data_link in deta_soup.find_all(class_='cook-img'):
    name_link = url + data_link.get("href")
    print(name_link)
    open_link_soup = open_http(name_link)
    print(open_link_soup)
# print(cook_data)
