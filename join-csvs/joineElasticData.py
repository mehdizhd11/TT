from elasticsearch import Elasticsearch
import pandas as pd

es = Elasticsearch(
    ['https://localhost:9200/'],
    http_auth=('elastic', '0yNVDELqtj4MB2PNmnGJ'),
    verify_certs=False
)

index1 = 'data1_table'
index2 = 'data2_table'

res1 = es.search(index=index1, body={"query": {"match_all": {}}})
data1 = [doc['_source'] for doc in res1['hits']['hits']]

res2 = es.search(index=index2, body={"query": {"match_all": {}}})
data2 = [doc['_source'] for doc in res2['hits']['hits']]

df1 = pd.DataFrame(data1 , columns=['name','grade','major','year','gender'] , copy=True)
df2 = pd.DataFrame(data2 , columns=['name','city','country'] , copy=True)

merged_df = pd.merge(df1, df2, on='name')

merged_df.to_csv('joined_elastic_data.csv', index=False)