from bs4 import BeautifulSoup
import requests
import json
URL = 'https://www.goodreads.com/book/show/325779.Next_of_Kin'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
autori_fin = []
date_fin=[]
text_fin=[]
for review in soup.find_all('div', class_='ReviewsList'):
    for autor in review.find_all('div', class_='ReviewerProfile__name'):
       autori_fin.append(autor.get_text())

    for date in review.find_all('span', class_='Text Text__body3'):
        date_fin.append(date.get_text())

    for text in review.find_all('span', class_='Formatted'):
        text_fin.append(text.get_text())


with open('reviews.json', 'w',encoding='utf-8' ) as f:
    json.dump(autori_fin, f, indent=4)
    json.dump(date_fin, f, indent=4)
    json.dump(text_fin, f, indent=4)
