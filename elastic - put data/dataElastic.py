import pandas as pd
from elasticsearch import Elasticsearch, helpers

df = pd.read_csv('data1.csv')

es = Elasticsearch(
    ['https://localhost:9200/'],
    http_auth=('elastic', '0yNVDELqtj4MB2PNmnGJ'),
    verify_certs=False
)

data = df.to_dict(orient='records')

index_name = 'data1_table'

def gendata(data):
    for doc in data:
        yield {
            "_index": index_name,
            "_source": doc
        }
        
helpers.bulk(es, gendata(data))