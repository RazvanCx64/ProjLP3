import textwrap
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
        nume_autor = autor.get_text(strip=True)
        autori_fin.append(nume_autor)
    for date in review.find_all('span', class_='Text Text__body3'):
        date_text = date.get_text(strip=True)
        date_fin.append(date_text)
    for text in review.find_all('span', class_='Formatted'):
        extra_text = text.get_text(strip=True)
        text_fin.append(extra_text)




reviews_fin = []

for author, date, text in zip(autori_fin, date_fin, text_fin):
    aut_date = {"author": author, "date": date}

    reviews_fin.append({
        "author_date": aut_date,
        "text": text
    })
    formatted_text = '\n'.join(textwrap.wrap(text, width=100))

with open('reviews.json', 'w', encoding='utf-8') as f:
    json.dump(reviews_fin, f, ensure_ascii=False, indent=2)
print(reviews_fin)