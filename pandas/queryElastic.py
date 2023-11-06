from elasticsearch import Elasticsearch
import pandas as pd

es = Elasticsearch(
    ['https://localhost:9200/'],
    http_auth=('elastic', '0yNVDELqtj4MB2PNmnGJ'),
    verify_certs=False
)

index = 'contact_table'

res = es.search(index=index, body={"query": {"match_all": {}}})
data = [doc['_source'] for doc in res['hits']['hits']]

df = pd.DataFrame(data)
# print(df.columns)
print('DF is :')
print(df)

filter_grade = df[df[' grade '] > 10]
print('Grade more than 10 :')
print(filter_grade)

filter_gender = df[df[' gender'] == ' f']
print('Female Gender : ')
print(filter_gender)

filter_major = df[df[' major '] == ' CE ']
print('CE major :')
print(filter_major)