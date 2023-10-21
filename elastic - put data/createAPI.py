from flask import Flask, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)
es = Elasticsearch(['https://localhost:9200/'], http_auth=('elastic', '0yNVDELqtj4MB2PNmnGJ'), verify_certs=False)

@app.route('/api/data', methods=['GET'])
def get_data():
    res = es.search(index='contact_table', body={'query': {'match_all': {}}, 'size': 50})
    data = [hit['_source'] for hit in res['hits']['hits']]
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)