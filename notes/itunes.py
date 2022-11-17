import requests
import sys
import json

if len(sys.argv) !=2:
    sys.exit()

#Requests 50 responses from the itunes API
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

#Grab the response and put it into json format
o = response.json()
#For every song we find, get data of each track
for result in o["results"]:
    #Print the track name that's in the result dictionary
    print(result["trackName"])