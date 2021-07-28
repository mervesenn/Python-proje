import requests
from bs4 import BeautifulSoup
url = "https://kur.doviz.com/"
html = requests.get(url).content
soup = BeautifulSoup(html,"html.parser")
items = soup.find("div",{"class":"table"}).find_all("tr")
dovName = []
i = True
exchane = {}
for info in items:
    name = info.get('data-table-subpage-key')
    if i == True or name == None:
        i = False
        continue
    value = info.find_all("td")[2].text.replace(",",".")
    value = float(value)
    exchane[name] = value
    dovName.append(name)

print("----------------------------------\n")
print("Döviz tipleri:")
print(dovName)
bozulandöviz = input("Bozulan döviz türü:")
alınandöviz = input("Alınan döviz türü:")
miktar = int(input(f"Ne kadar {bozulandöviz} bozdurmak istiyorsunuz? "))
print("\n-----------------------")
if bozulandöviz == 'TRY':
    temp = miktar / exchane[alınandöviz]
    temp2= 1/exchane[alınandöviz]
    temp = exchane[bozulandöviz] * miktar
elif alınandöviz == 'TRY':
    temp = exchane[bozulandöviz] * miktar
    temp2 = exchane[bozulandöviz]
else:
    temp = exchane[bozulandöviz] * miktar
    temp = temp /exchane[alınandöviz]
    temp2 = exchane[bozulandöviz] / exchane[alınandöviz]

print("1 {} = {:.4f} {}".format(bozulandöviz,temp2,alınandöviz))
print(f"{miktar} {bozulandöviz} = {temp:.4f} {alınandöviz}")
print("--------------------")
print("\n-------------------------------------------")