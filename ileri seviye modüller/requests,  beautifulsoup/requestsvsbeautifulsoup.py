import requests
from bs4 import BeautifulSoup

url = "https://yellowpages.com.tr/ara?q=Ankara"
response = requests.get(url)
htmliceriği = response.content
soup = BeautifulSoup(htmliceriği, "html.parser")
print(soup.find_all("div", {"class", "bubbles"}))
