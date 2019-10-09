import pyfiglet
import termcolor
from random import choice
import requests
import time



text = pyfiglet.figlet_format("Dad Joke 3000" )
color = choice(['grey','red','green','yellow','blue','magenta','cyan','white'])

attri1 = choice(['bold','underline','blink','reverse'])
attri2 = choice(['bold','underline','blink','reverse'])

print(termcolor.colored(text,color, attrs=[attri1, attri2]))


the_search = input("Welcome to the awefull dad jokes!\nOn which topic do you want awefull jokes: ")


start = time.time()
url = "https://www.icanhazdadjoke.com/search"

response = requests.get(
    url,
    headers = {"Accept" : "application/json"},
    params = {'term' : the_search}
) # getting request in json format

data = response.json()['results'] # .json() converts the string in json format into dictionary
if len(data) != 0:
    print(f"Found {len(data)} jokes on {the_search}")
    print("Showing you one!!!\n\n")

    the_joke = choice(data)
    print(the_joke['joke'])
else:
    print(f"There are no jokes on {the_search}")

print(f"Time taken: {time.time()-start}")