import requests

url = 'https://ped.uspto.gov/api/queries/c5a16271-23dc-4715-b599-8d41c95c9e82/download'

response = requests.get(url)
print(response.text)

with open('blockchain.zip', 'wb') as f:
    f.write(response.content)
