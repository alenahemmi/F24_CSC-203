"""
Alena Hemminger
Aug 26 2024
Application Development 1
This is to enforce the idea that a browser is just an easy way to access this 'discussion' between a client and server
"""

import requests

url = "https://wikipedia.org"
response = requests.get(url)

print(response.content) # this pulls the html to the console