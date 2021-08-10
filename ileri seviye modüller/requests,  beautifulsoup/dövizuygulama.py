import requests

url = "https://data.fixer.io/api/latest"
birincidoviz = input("Birinci döviz:")
ikincidoviz = input("İkinci döviz:")
response = requests.get(url + birincidoviz)
jsonverisi = response.json()

print(jsonverisi["rates"])
