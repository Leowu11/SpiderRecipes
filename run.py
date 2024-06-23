from open_requests import open_http
from bs4 import BeautifulSoup
url="https://www.douguo.com"
f_rest=open_http(url)
print(f_rest)
html_doc = f_rest.text
soup = BeautifulSoup(html_doc,"lxml")
recipe_img = soup.select("imublo clearfix")
print(recipe_img)