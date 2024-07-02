import logging
import re
from time import sleep

import lxml
import urllib.parse

import WriteXml
from open_requests import open_http
from bs4 import BeautifulSoup



def data_pages(deta):
    for data_link in deta.find_all(class_='cook-img'):
        name_link = url + data_link.get("href")
        ulr_id=name_link.split("/")[-1].split(".")[0]
        print(ulr_id)
        link.append(name_link)
        open_one_link_date = open_http(name_link)
        if open_one_link_date :
            open_one_link_date_bea = BeautifulSoup(open_one_link_date, "html.parser")

            name_data = open_one_link_date_bea.find(class_="title text-lips")
            # print(str(name_data))
            re_name=re.compile('<h1 class=".*?" style="display: inline-block">(.*?)</h1>')
            name=re.findall(re_name,str(name_data))
            print(name)

            recipe = open_one_link_date_bea.find(class_="recipe-content clearfix")

            metarial = open_one_link_date_bea.find(class_="metarial")
            # print(metarial)
            peliao_list=[]
            if  "scname" in str(metarial):
                for ran in metarial.find_all('span', class_="scname"):
                    # data_scname=ran.get_text("")
                    print(ran)
                    _blank = re.compile('<a href=.*?target=".*?">(.*?)</a>')
                    peliao = (re.findall(_blank, str(ran)))
                    if peliao:
                        pass
                    else:
                        not_blank = re.compile('<span class=.*?>(.*?)</span>')
                        peliao = (re.findall(not_blank, str(ran)))
                    peliao_list.append(peliao[0])
            else:
                peliao_list=[]



            # _blank = re.compile('<a href=.*?target=".*?">(.*?)</a>')
            # peliao_list = (re.findall(_blank, str(metarial)))
            print(peliao_list)
            liang_blank = re.compile('<span class="right scnum">(.*?)</span>')
            lianglist = re.findall(liang_blank, str(metarial))
            # print(lianglist)
            new_liang=[item if item else '适量' for item in lianglist]
            print(new_liang)


            step = open_one_link_date_bea.find(class_="step")
            # print(step)
            set_list = []
            img_link_list = []
            for step_list_data in step.find_all(class_="stepinfo"):
                # print(step_list_data)
                pattern = r"[\u4e00-\u9fa5，。、；：？！]+"
                matches = re.findall(pattern, re.sub('<[^<]+?>', '', str(step_list_data)))
                extracted_text = ''.join(matches)
                set_list.append(extracted_text.replace("步骤",""))
                # re_step = re.compile('<div class="stepinfo">\s*<p>.*?\d+</p>\s*(.*?)\s*</div>')
                # step_list_data = re.findall(re_step, str(step_list_data))
                # # print(step_list_data)
                # if step_list_data:
                #     set_list.append(step_list_data[0])
                # else:
                #     set_list.append("null")

            for img_link in step.find_all(class_="stepcont clearfix"):
                # print("------------------------------------------------------------------------------------------------------")
                re_link_com = re.compile('data-origin="(.*?)"')
                re_link = re.findall(re_link_com, str(img_link))[0]
                img_link_list.append(re_link)
            print(img_link_list)
            print(set_list)
            if len(img_link_list)==len(set_list):
                print(ulr_id + " xiaotong")
            else:
                print(ulr_id+" buxiaotong " + str(len(img_link_list)) +"-------" +str(len(set_list)))
            sleep(5)
            # WriteXml.write(id,name,set_list,set_list)
        else:
            pass


url = "https://www.douguo.com"
f_rest = open_http(url)
# print(f_rest)
soup = BeautifulSoup(f_rest, "html.parser")
header = soup.find(class_="imublo clearfix")

"""get channel"""
channel = []
for link in header.find_all("a"):
    channel.append(url + link.get('href'))

for link_1 in channel:
    # res_1 = open_http(link_1)
    # print(res_1)
    url_en = urllib.parse.quote(link_1, safe='/:')
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
    mt20=deta_soup.find(class_='pages')
    # print(mt20)
    while True:
        data_pages(deta_soup)
        if ("下一页" in str(mt20)):
            link_list_anext=[]
            for anext_link in mt20.find_all(class_="anext"):
                # print(anext_link)
                link_list_anext.append(anext_link.get("href"))
            print(link_list_anext)
            date_rest = open_http(link_list_anext[0])
            deta_soup = BeautifulSoup(date_rest, "html.parser")
            mt20 = deta_soup.find(class_='pages')
        else:
            break



