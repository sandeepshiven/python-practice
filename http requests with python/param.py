import requests

url = "https://www.icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers = {"Accept" : "application/json"},
    params = {'term' : "cat"}
) # getting request in json format

data = response.json() # .json() converts the string in json format into dictionary
print(data['results'][2]['joke'])