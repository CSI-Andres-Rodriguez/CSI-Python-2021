import json, ssl
import urllib.request
from Cannabis import Cannabis

# This is discouraged but it will avoid certificate validation (prevents error)
ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
cannabisURL = "https://random-data-api.com/api/cannabis/random_cannabis"


req = urllib.request.Request(cannabisURL)
r = json.loads(urllib.request.urlopen(req).read())


cannabis:Cannabis = Cannabis(**r)

IncorrectLetters = []

print(len(cannabis.strain) * "_ ")

 #print(cannabis.strain)

def getInput():
    while(True):
        guess=input("Your guess is")
        if guess .isnumeric()== True :
            print("Needs to be a letter")
            continue

        if len(guess) !=1 :
            print("Needs to be only one letter")
            continue 

        if not guess.isalpha():
            print("No special characters")
            continue

        if (guess in IncorrectLetters):
            print("Letter is already used")
            continue

        IncorrectLetters.append(guess)
        return guess

print(getInput())
    

