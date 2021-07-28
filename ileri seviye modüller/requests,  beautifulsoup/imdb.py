import requests
from bs4 import BeautifulSoup
url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
htmliçeriği = response.content
soup = BeautifulSoup(htmliçeriği,"html.parser")
a = float(input("Rating'i giriniz:"))
başlıklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class","ratingColumn imdbRating"})
for başlık,rating in zip(başlıklar,ratingler):
    başlık = başlık.text
    rating = rating.text
    başlık = başlık.strip()
    başlık = başlık.replace("\n","")
    rating = rating.strip()
    rating = rating.replace("\n","")
    if (float(rating) > a):
        print("Film ismi: {} Filmin Ratingi:{}".format(başlık,rating))
