import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = 'http://quotes.toscrape.com/page/{}/'

def get_quotes_from_page(page_number):
    url = base_url.format(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []
    
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        quotes.append({
            'texte': text,
            'auteur': author,
            'tags': tags
        })
    
    return quotes

all_quotes = []
for i in range(1, 6):
    all_quotes.extend(get_quotes_from_page(i))

top_tags = ['love', 'inspirational', 'life', 'humor']

filtered_quotes = [quote for quote in all_quotes if any(tag in top_tags for tag in quote['tags'])]

print(filtered_quotes)