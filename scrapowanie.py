import requests
from bs4 import BeautifulSoup

url = "https://www.tiobe.com/tiobe-index/"
response = requests.get(url)
response.encoding = "utf-8"

if(response.status_code !=200):
    print("Bład pobrania strony.")
else:

    soup = BeautifulSoup(response.text, "html.parser")
    markdown = ""
    tabela = soup.find("table")
    
    wiersze = tabela.find_all("tr")
    print(wiersze)
    j =1
    for wiersz in wiersze:
        komorki = wiersz.find_all("td")
        print(komorki)
        print("huhu")
        if(len(komorki) > 6):
            markdown += "# "  + komorki[4].text + "\n"
            j+=1
            markdown += "- Ratings: " + komorki[5].text + "\n"
            markdown += "- Change: " + komorki[6].text + "\n"
            markdown += "- Picture: " + komorki[3].text +"\n"
    print(markdown)
    with open ("strona.md", 'w', encoding="utf-8") as plik:
        plik.write(markdown)