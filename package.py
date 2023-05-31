import requests

url = 'https://ped.uspto.gov/api/queries/c5a16271-23dc-4715-b599-8d41c95c9e82/package'

params = {
    'format': 'XML'
}

response = requests.put(url, params=params)

print(response.text)

