import pyfiglet
import termcolor
from random import choice
import requests
import time
start = time.time()

text = pyfiglet.figlet_format("Hindi Jokes" )
color = choice(['grey','red','green','yellow','blue','magenta','cyan','white'])

attri1 = choice(['bold','underline','blink','reverse'])
attri2 = choice(['bold','underline','blink','reverse'])

print(termcolor.colored(text,color, attrs=[attri1, attri2]))

url = "https://gofugly.in/api/content/18/"

response = requests.get(
    url,
    headers = {"Accept" : "application/json"}
) # getting request in json format
#print(response.text)
data = response.json()['result'] # .json() converts the string in json format into dictionary

print("Showing you one!!!\n\n")

the_joke = choice(data)
print(the_joke['joke'])
print(f"Time taken: {time.time()-start}")

