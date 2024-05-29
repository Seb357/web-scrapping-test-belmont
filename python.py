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

token = 'rJiUnbpvBMZqXVEYfLuomTeQAWhDyIGxCtaOwSzgFdPKjlcRHsNk'

df = pd.DataFrame(filtered_quotes)
df['token'] = token
df.to_csv('results.csv', index=False)

print("Token ajouté à results.csv")

print("Les résultats ont été écrits dans results.csv")

books_url = 'http://quotes.toscrape.com/tag/books/page/{}/'

def get_books_quotes(page_number):
    url = books_url.format(page_number)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = []
    
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text()
        author = quote.find('small', class_='author').get_text()
        tags = [tag.get_text() for tag in quote.find_all('a', class_='tag')]
        quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })
    
    return quotes

books_url = 'http://quotes.toscrape.com/tag/books/page/{}/'

def get_books_quotes(page_number):
    url = books_url.format(page_number)
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

books_quotes = []
for i in range(1, 3):
    books_quotes.extend(get_books_quotes(i))

print("Citations avec le tag 'books' récupérées dans les pages souhaitées")

existing_quotes = df.to_dict('records')

all_quotes = existing_quotes + books_quotes

seen_quotes = set()
unique_quotes = []
for quote in all_quotes:
    quote_tuple = (quote['texte'], quote['auteur'])
    if quote_tuple not in seen_quotes:
        seen_quotes.add(quote_tuple)
        unique_quotes.append(quote)

df = pd.DataFrame(unique_quotes)
df.to_csv('results.csv', index=False)