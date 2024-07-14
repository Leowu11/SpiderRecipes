import logging
from time import sleep

import requests


def open_http(url):
    s=requests.Session()
    while True:
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
        res = s.get(url, headers=headers, timeout=120, stream=True)

        sleep(5)
        s.close()
        if res.status_code == 200:
            logging.info(200, "当前爬取的网址为：" + url)
            html_doc = res.text
            break
    return html_doc


