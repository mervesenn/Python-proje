import requests
from bs4 import BeautifulSoup
url = "https://yellowpages.com.tr/ara?q=Ankara"
response = requests.get(url)
htmliçeriği = response.content
soup = BeautifulSoup(htmliçeriği,"html.parser")
print(soup.find_all("div",{"class","bubbles"}))
