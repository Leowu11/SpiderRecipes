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
# print(one_link1)

date_rest = open_http(one_link1)
link = []
deta_soup = BeautifulSoup(date_rest, "html.parser")
for data_link in deta_soup.find_all(class_='cook-img'):
    name_link = url + data_link.get("href")
    # print(name_link)
    link.append(name_link)
    # open_link_soup = open_http(name_link)
    # print(open_link_soup)
# print(cook_data)


# print(link[0])
open_one_link_date=open_http(link[0])
open_one_link_date_bea=BeautifulSoup(open_one_link_date,"html.parser")
# print(open_one_link_date_bea)
relative_data=open_one_link_date_bea.find_all(class_="cboxElement cboxElement1")
# print(relative_data)
relative_data_re=re.compile('<img alt="(.*?)"')
name=re.findall(relative_data_re,str(relative_data))[0]
# print(name)

recipe=open_one_link_date_bea.find(class_="recipe-content clearfix")
# print(recipe)
relative_tow_data=recipe.find(class_="relative")
print(relative_tow_data)
video_re=re.compile('<a href="(.*?)"')
video_link=re.findall(video_re,str(relative_tow_data))[1]
print(video_link)

metarial=open_one_link_date_bea.find(class_="metarial")
# print(metarial)
_blank=re.compile('<a href=.*?target=".*?">(.*?)</a>')
peliao_list=(re.findall(_blank,str(metarial)))
# print(peliao_list)
liang_blank=re.compile('<span class="right scnum">(.*?)</span>')
lianglist=re.findall(liang_blank,str(metarial))
# print(lianglist)
step=open_one_link_date_bea.find(class_="step")
# print(step)
set_list=[]
for step_list_data in step.find_all(class_="stepinfo"):
    # print(step_list_data)
    re_step=re.compile('<div class="stepinfo">\s*<p>.*?\d+</p>\s*(.*?)\s*</div>')
    step_list_data=re.findall(re_step,str(step_list_data))
    # print(step_list_data)
    set_list.append(step_list_data)