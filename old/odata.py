import requests
import pyodata

metadata_ = requests.get('https://api.parliament.uk/odata/$metadata', headers={'Accept': 'application/xml'}).text.encode()

client = pyodata.Client('https://api.parliament.uk/odata', requests.Session(), metadata=metadata_)
