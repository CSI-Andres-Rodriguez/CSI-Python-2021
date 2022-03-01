import json, ssl
import urllib.request
from Cannabis import Cannabis
import urllib.request

#characters used list
used=[]

def get_cannabis():
# This is discouraged but it will avoid certificate validation (prevents error)
    ssl._create_default_https_context = ssl._create_unverified_context

# This is the URL from which we will request the data
    cannabisURL = "https://random-data-api.com/api/cannabis/random_cannabis"

#Api request
    req = urllib.request.Request(cannabisURL)
    r = json.loads(urllib.request.urlopen(req).read())

    cannabis:Cannabis = Cannabis(**r)

    return cannabis.strain.upper()


# create var to store the value of get_cannabis()

myCannabis = get_cannabis()

IncorrectLetters = []

print(len(myCannabis) * "_ ")

#drawings of my hangman

hang = ["""
H A N G M A N - 

   <====>
   |   l
       l
       l
       l
       l
<=======>""", 
"""
H A N G M A N - 

  <====>
  I   l
  *   l
      l
      l
      l
<=======>""", 
"""
H A N G M A N -

  <====>
  I    l
  *    l
  I    l
       l
       l
<=======>""", 
"""
H A N G M A N - 

  <====>
  I    l
  *    l
 $I    l
       l
       l
=========""", 
"""
H A N G M A N - 

  <====>
  I    l
  *    l
 $I$   l
       l
       l
<=======>""", 
"""
H A N G M A N - 

  <====>
  I    l
  *    l
 $I$   l
 ( )   l
       l
<=======>""", 
"""
H A N G M A N - 

 <=====>
  I    l
  *    l
 $I$   l
 ( )   l
       l
<=======>""",
]

#incorrect letters in my hangman
print(myCannabis)
def getInput():
    invalid_characters = ("1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")","{","}","[","]",";","'","<",",",".",">","/","?","|")
    
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

# print(getInput())

def printword():
    temp:str=""
    len(myCannabis)
    for letter in myCannabis :
        print(letter)
        # letter in(IncorrectLetters)
        if letter not in IncorrectLetters :
            temp+="_"
        else:
            temp+=letter

        return temp

def printStep():
    counter = 0
    for letter in used:
        if letter not in myCannabis:
         counter= counter + 1

    print(hang[counter])

while True :
    printStep()
    getInput()
    printword()
