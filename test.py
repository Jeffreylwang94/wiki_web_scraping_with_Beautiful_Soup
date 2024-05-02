from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/Car_classification"


page = requests.get(url)

content = page.content

soup = BeautifulSoup(content,'html.parser')

f = open("test.txt", "a")
f.write((soup.prettify()))
f.close()
