import logging
import re
from time import sleep

import lxml
import urllib.parse

import WriteDb
from open_requests import open_http
from bs4 import BeautifulSoup


def data_pages(deta,tepy_name):
    for data_link in deta.find_all(class_='cook-img'):
        name_link = url + data_link.get("href")
        ulr_id = name_link.split("/")[-1].split(".")[0]
        print(ulr_id)
        link.append(name_link)
        open_one_link_date = open_http(name_link)
        if open_one_link_date:
            open_one_link_date_bea = BeautifulSoup(open_one_link_date, "html.parser")

            name_data = open_one_link_date_bea.find(class_="title text-lips")
            # print(str(name_data))
            re_name = re.compile('<h1 class=".*?" style="display: inline-block">(.*?)</h1>')
            rename = re.findall(re_name, str(name_data))
            print(rename)

            recipe = open_one_link_date_bea.find(class_="recipe-content clearfix")

            metarial = open_one_link_date_bea.find(class_="metarial")
            # print(metarial)
            peliao_list = []
            if "scname" in str(metarial):
                for ran in metarial.find_all('span', class_="scname"):
                    # data_scname=ran.get_text("")
                    # print(ran)
                    _blank = re.compile('<a href=.*?target=".*?">(.*?)</a>')
                    peliao = (re.findall(_blank, str(ran)))
                    if peliao:
                        pass
                    else:
                        not_blank = re.compile('<span class=.*?>(.*?)</span>')
                        peliao = (re.findall(not_blank, str(ran)))
                    peliao_list.append(peliao[0])
            else:
                peliao_list = []

            # _blank = re.compile('<a href=.*?target=".*?">(.*?)</a>')
            # peliao_list = (re.findall(_blank, str(metarial)))
            print(peliao_list)
            liang_blank = re.compile('<span class="right scnum">(.*?)</span>')
            lianglist = re.findall(liang_blank, str(metarial))
            # print(lianglist)
            new_liang = [item if item else '适量' for item in lianglist]
            print(new_liang)
            mate = []
            for i in range(0, len(peliao_list)):
                mate.append(peliao_list[i] + " " + new_liang[i])

            step = open_one_link_date_bea.find(class_="step")
            # print(step)
            set_list = []
            img_link_list = []
            if "stepinfo" in str(step):
                for step_list_data in step.find_all(class_="stepinfo"):
                    # print(step_list_data)
                    pattern = r"[\u4e00-\u9fa5，。、；：？！]+"
                    matches = re.findall(pattern, re.sub('<[^<]+?>', '', str(step_list_data)))
                    extracted_text = ''.join(matches)
                    set_list.append(extracted_text.replace("步骤", ""))

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
            if len(img_link_list) == len(set_list):
                print(ulr_id + " xiaotong")
            else:
                print(ulr_id + " buxiaotong " + str(len(img_link_list)) + "-------" + str(len(set_list)))
            sleep(5)
            # WriteXml.write(id,name,set_list,set_list)
            if all([ulr_id, rename[0],mate, img_link_list, set_list]):
                data = [{
                    'id': ulr_id,
                    'name': rename[0],
                    'type':tepy_name,
                    'materials': mate,
                    'links': img_link_list,
                    'actions': set_list
                }, ]
                print(data)
                WriteDb.writeDb(data)

        else:
            pass


url = "https://www.douguo.com"
f_rest = open_http(url)
# print(f_rest)
soup = BeautifulSoup(f_rest, "html.parser")
header = soup.find(class_="imublo clearfix")

"""get channel"""
channel = [
    # 'https://www.douguo.com/caipu/热菜',
    # 'https://www.douguo.com/caipu/凉菜',
    # 'https://www.douguo.com/caipu/主食',
    # 'https://www.douguo.com/caipu/汤',
    # 'https://www.douguo.com/caipu/早餐',
    # 'https://www.douguo.com/caipu/午餐',
    # 'https://www.douguo.com/caipu/海鲜',
    # 'https://www.douguo.com/caipu/孕妇',
    # 'https://www.douguo.com/caipu/甜品',
    # 'https://www.douguo.com/caipu/粥',
    # 'https://www.douguo.com/caipu/宝宝食谱',
    # 'https://www.douguo.com/caipu/糕点',
    'https://www.douguo.com/caipu/微波炉'
]
# for link in header.find_all("a"):
#     channel.append(url + link.get('href'))
# print(channel)
# #
for link_1 in channel:
    print(link_1)
    tepy_name=link_1.split("/")[-1]
    print(tepy_name)
    url_en = urllib.parse.quote(link_1, safe='/:')
    res_1 = open_http(url_en)
    res_soup = BeautifulSoup(res_1, "html.parser")
    # print("++++++++++++++++++++++++++++++++++")
    # print(res_soup)
    # print("++++++++++++++++++++++++++++++++++")
    sort_more = res_soup.find(class_="sort-more")
    # print(sort_more)
    one_link = []
    # sleep(5)
    if "sort-more" in str(sort_more):
        for more_link in sort_more.find_all("a"):
            one_link.append(url + more_link.get("href"))
        one_link1 = one_link[0]
    else:
        continue

    # print(one_link1)

    date_rest = open_http(one_link1)
    link = []
    deta_soup = BeautifulSoup(date_rest, "html.parser")
    mt20 = deta_soup.find(class_='pages')
    # print(mt20)
    while True:
        data_pages(deta_soup,tepy_name)
        if ("下一页" in str(mt20)):
            link_list_anext = []
            for anext_link in mt20.find_all(class_="anext"):
                # print(anext_link)
                link_list_anext.append(anext_link.get("href"))
            print(link_list_anext)
            date_rest = open_http(link_list_anext[0])
            deta_soup = BeautifulSoup(date_rest, "html.parser")
            mt20 = deta_soup.find(class_='pages')
            print(mt20)
        else:
            print("end"+"==========================")
            break
