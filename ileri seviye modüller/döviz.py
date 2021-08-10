import requests
from bs4 import BeautifulSoup

url = "https://kur.doviz.com/"
html = requests.get(url).content
soup = BeautifulSoup(html, "html.parser")
items = soup.find("div", {"class":"table"}).find_all("tr")
dovName = []
i = True
exchane = {}
for info in items:
    name = info.get('data-table-subpage-key')
    if i == True or name == None:
        i = False
        continue
        
    value = info.find_all("td")[2].text.replace(",", ".")
    value = float(value)
    exchane[name] = value
    dovName.append(name)

print("----------------------------------\n")
print("Döviz tipleri:")
print(dovName)
bozulandoviz = input("Bozulan döviz türü:")
alinandoviz = input("Alınan döviz türü:")
miktar = int(input(f"Ne kadar {bozulandoviz} bozdurmak istiyorsunuz? "))
print("\n-----------------------")
if bozulandoviz == 'TRY':
    temp = miktar / exchane[alinandoviz]
    temp2= 1/exchane[alinandoviz]
    temp = exchane[bozulandoviz] * miktar
    
elif alinandoviz == 'TRY':
    temp = exchane[bozulandoviz] * miktar
    temp2 = exchane[bozulandoviz]
    
else:
    temp = exchane[bozulandoviz] * miktar
    temp = temp /exchane[alinandoviz]
    temp2 = exchane[bozulandoviz] / exchane[alinandoviz]

print("1 {} = {:.4f} {}".format(bozulandoviz, temp2, alinandoviz))
print(f"{miktar} {bozulandoviz} = {temp:.4f} {alinandoviz}")
print("--------------------")
print("\n-------------------------------------------")
