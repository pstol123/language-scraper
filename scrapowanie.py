import requests

url = "https://www.tiobe.com/tiobe-index/"
response = requests.get(url)

if(response.status_code !=200):
    print("Bład pobrania strony.")
else:
    print(response.text)