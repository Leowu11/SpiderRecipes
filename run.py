from open_requests import open_http
from bs4 import BeautifulSoup
url="https://www.douguo.com"
f_rest=open_http(url)
# print(f_rest)
soup = BeautifulSoup(f_rest,"lxml")
recipe_material = soup.findAll("div", {"class":"imublo clearfix"})
print(recipe_material)