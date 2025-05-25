"""In acest fisier am dezvoltat un script care extrage autorul, data si textul recenziei de pe un site cu recenzii de carti (goodreads.com).
S-a folosit libraria BeautifulSoup4 pentru a parcurge site-ul.
Bibliografie:https://www.crummy.com/software/BeautifulSoup/bs4/doc/#find-all

autori:Razvan-Cristian Cos, Bianca Bulzan"""
from bs4 import BeautifulSoup
import requests
import json
URL = 'https://www.goodreads.com/book/show/325779.Next_of_Kin'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
# print(soup.prettify()) In variabila soup se gaseste HTML-ul complet a paginii
autori_fin = []
date_fin=[]
text_fin=[]
for autor in soup.find_all('div', class_='ReviewerProfile__name'):
    autori_fin.append(autor.get_text())

for date in soup.find_all('span', class_='Text Text__body3'):
    date_fin.append(date.get_text())

for text in soup.find_all('span', class_='Formatted'):
    text_fin.append(text.get_text())

with open('reviews.json', 'w',encoding='utf-8' ) as f:
    json.dump(autori_fin, f, indent=4)
    json.dump(date_fin, f, indent=4)
    json.dump(text_fin, f, indent=4)


