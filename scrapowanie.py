import requests
from bs4 import BeautifulSoup
from googlesearch import search
url = "https://www.tiobe.com/tiobe-index/"
url2 = "https://www.tiobe.com"
response = requests.get(url)
response.encoding = "utf-8"


if(response.status_code !=200):
    print("Bład pobrania strony.")
else:

    soup = BeautifulSoup(response.text, "html.parser")
    markdown = ""
    tabela = soup.find("table")
    
    wiersze = tabela.find_all("tr")
    j =1
    
    for wiersz in wiersze:
        podstrona = ""
        komorki = wiersz.find_all("td")

        if(len(komorki) > 6):
            jezyk = komorki[4].text
            podstrona += "# "  + jezyk + "\n"
            j+=1
            
            podstrona += "- Ratings: " + komorki[5].text + "\n"
            podstrona += "- Change: " + komorki[6].text + "\n"
            pom = url2 + komorki[3].find("img")["src"]
            
            podstrona += "- Logo: ![logo](" + pom +")\n"
            wiki = list(search(jezyk + " wikipedia", num_results = 1))[0]
            tymczasowe = "https://en.wikipedia.org/wiki/Python_(programming_language)"
            
            response_w = requests.get(wiki)
            response_w.encoding = "utf-8"
            markdown += podstrona
            markdown += "- [Zobacz więcej](" + jezyk+".html" + ")" + "\n"
            if(response.status_code ==200):
                
                soup_w = BeautifulSoup(response_w.text, "html.parser")
                
                opisy = list(soup_w.find_all("p"))
                if(len(opisy)>1):
                    opis = opisy[1].text
                tabelka = list(soup_w.find_all("td"))
                if(len(tabelka)>1):
                    parm = tabelka[1].text
                podstrona += "- Opis: " + opis
                podstrona += "- Paradygmat: " + parm + "\n"
                podstrona += "- [Więcej informacji](" + wiki + ")" + "\n"
            for i in range(len(jezyk)):
                if(jezyk[i] == '/'):
                    jezyk = jezyk[:i]
                    break
            with open(jezyk+".md",'w', encoding="utf-8") as plik:
                plik.write("--- \n title: " + jezyk + " \n layout: default \n--- \n")     
                plik.write(podstrona)
                
            


    with open ("strona.md", 'w', encoding="utf-8") as plik:
        plik.write("--- \n title: lista \n layout: default \n--- \n\n")     
        plik.write(markdown)

    with open("index.md",'w', encoding="utf-8") as plik:
        plik.write("--- \n title: Strona Główna\n layout: default \n--- \n")        
        plik.write("# Języki programowania\n")
        plik.write("Istnieje wiele różnych języków programowania o różnej popularności i użyteczności. Spróbuj przejrzeć wszystkie z nich! \n")
        plik.write("[Zobacz listę języków](strona.html) \n")