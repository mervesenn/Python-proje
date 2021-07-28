import requests
url = "https://data.fixer.io/api/latest"
birincidöviz = input("Birinci döviz:")
ikincidöviz = input("İkinci döviz:")
response =requests.get(url + birincidöviz)
jsonverisi = response.json()
print(jsonverisi["rates"])