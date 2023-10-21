import sqlite3
from elasticsearch import Elasticsearch, helpers

conn = sqlite3.connect('tgju-FastAPI-prices/website_data.db')
cursor = conn.cursor()

es = Elasticsearch(['https://localhost:9200/'], http_auth=('elastic', '0yNVDELqtj4MB2PNmnGJ'), verify_certs=False)

cursor.execute('SELECT title, price, change FROM website_data')
data = cursor.fetchall()

index_name = 'scraped_table'

actions = [
    {
        "_index": index_name,
        "_source": {
            "title": row[0],
            "price": row[1],
            "change": row[2]
        }
    }
    for row in data
]

helpers.bulk(es, actions)

conn.close()


