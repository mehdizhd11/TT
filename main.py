from fastapi import FastAPI
import sqlite3
from bs4 import BeautifulSoup
import requests

app = FastAPI()

@app.get("/")
def scrape_and_store_data():
    conn = sqlite3.connect('website_data.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS website_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price TEXT,
            change TEXT
        )
    ''')

    url = 'https://www.tgju.org/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    ul_elements = soup.find('ul', class_='info-bar')
    li_elements = ul_elements.find_all('li')

    h3_tags = []
    for li in li_elements:
        h3_tags.append(li.find('h3'))
    titles = [element.text.strip() for element in h3_tags]

    info_price_elements = soup.find_all(class_='info-price')
    prices = [element.text.strip() for element in info_price_elements]

    change_elements = soup.find_all('span', class_='info-change')
    changes = [element.text.strip() for element in change_elements]

    # Inserting the data into the table
    json = []
    for index in range(9):
        
        title = titles[index]
        price = prices[index]
        change = changes[index]
        
        json.append(
            {
                'title': titles[index],
                'price': prices[index],
                'change': changes[index]
            }
        )
        
        cursor.execute('INSERT INTO website_data (title, price, change) VALUES (?, ?, ?)', (title, price, change))
        conn.commit()

    # Closing the connection
    conn.close()

    return json
