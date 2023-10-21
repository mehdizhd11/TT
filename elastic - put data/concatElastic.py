import pandas as pd
from elasticsearch import Elasticsearch, helpers

df = pd.read_csv('concatenated_file.csv')
# print(df)

es = Elasticsearch(
    ['https://localhost:9200/'],
    http_auth=('elastic', '0yNVDELqtj4MB2PNmnGJ'),
    verify_certs=False
)

data = df.to_dict(orient='records')

index_name = 'contact_table'

def gendata(data):
    for doc in data:
        yield {
            "_index": index_name,
            "_source": doc
        }
        
helpers.bulk(es, gendata(data))