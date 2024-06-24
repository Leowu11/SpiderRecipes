import re
import lxml
from open_requests import open_http
from bs4 import BeautifulSoup
url="https://www.douguo.com"
f_rest=open_http(url)
# print(f_rest)
soup=BeautifulSoup(f_rest,"html.parser")
header= soup.find(class_="imublo clearfix")
print (header)
"""get channel"""
channel=[]
for link in header.find_all("a"):
    print(link.get('href'))
    channel.append(url+link.get('href'))
# print(channel)

for link_1 in channel:
    res_1=open_http(link_1)
    print(res_1)