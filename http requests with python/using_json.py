import requests

url = "https://www.icanhazdadjoke.com"

response = requests.get(url,headers = {"Accept" : "application/json"}) # getting request in json format

data = response.json() # .json() converts the string in json format into dictionary
print(data['joke'])