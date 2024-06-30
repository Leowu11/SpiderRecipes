import requests


def open_http(url):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'}
    res = requests.get(url, headers=headers,timeout=120,stream=True)
    # print("当前爬取的网址为：" + url)
    html_doc = res.text
    if html_doc :
        return html_doc
    else:
        return ""