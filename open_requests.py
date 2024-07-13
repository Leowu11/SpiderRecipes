import logging
from time import sleep

import requests


def open_http(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers,timeout=120,stream=True)
    sleep(5)
    if res.status_code==500:
        logging.error("Internal Server Error occurred ")
    elif res.status_code==200:
        logging.info(200,"当前爬取的网址为：" + url)
        html_doc = res.text
        return html_doc
    else:
        return ''