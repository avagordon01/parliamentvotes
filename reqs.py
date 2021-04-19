import json
import requests

def get_publications(count=10, page=0):
    response = requests.get('https://lda.data.parliament.uk/publicationlogs.json?_pageSize={count}&_page={page}&_sort=-publicationDate'.format(count=count, page=page))
    endpoint = json.loads(response.text)
    return [item for item in endpoint['result']['items']]

def get_resource_id_from_item(item):
    url = item['_about']
    id = url.rsplit('/', 1)[1]
    return id

def get_pdf_link(id):
    response = requests.get('https://lda.data.parliament.uk/publicationlogs/{id}.json'.format(id=id))
    endpoint = json.loads(response.text)
    pdf_link = endpoint['result']['primaryTopic']['externalLocation']
    return pdf_link

def get_divisions(count=10, page=0):
    response = requests.get('https://lda.data.parliament.uk/commonsdivisions.json?_pageSize={count}&_page={page}&_sort=-publicationDate'.format(count=count, page=page))
    endpoint = json.loads(response.text)
    return [item for item in endpoint['result']['items']]

from pprint import pprint as print
divisions = get_divisions()
division = divisions[0]
id = get_resource_id_from_item(division)
print(id)


response = requests.get('https://lda.data.parliament.uk/commonsdivisions/{id}.json'.format(id=id))
endpoint = json.loads(response.text)
print(endpoint)
id = get_resource_id_from_item(endpoint['result']['primaryTopic'])
print((id))
