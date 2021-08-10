import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)
htmlicerigi = response.content
soup = BeautifulSoup(htmlicerigi, "html.parser")

a = float(input("Rating'i giriniz:"))
baslıklar = soup.find_all("td",{"class":"titleColumn"})
ratingler = soup.find_all("td",{"class", "ratingColumn imdbRating"})

for baslık,rating in zip(baslıklar,ratingler):
    baslık = baslık.text
    rating = rating.text
    baslık = baslık.strip()
    baslık = baslık.replace("\n", "")
    rating = rating.strip()
    rating = rating.replace("\n", "")
    
    if (float(rating) > a):
        print("Film ismi: {} Filmin Ratingi:{}".format(baslık, rating))
