import requests

url = 'http://www.google.com'
response = requests.get(url).content
print(response)