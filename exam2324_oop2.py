#4. daļa
#2. uzdevums
import requests
import json

#1. pieprasijums uz doto API
atbilde = requests.get("https://restcountries.com/v3.1/all")

#2. vai no servera ir saņemta atbilde
if (atbilde.status_code != 200):
    print("Kaut kas nav pareizi")

# 3.  Iegūsti un izvadi visu valstu vispārpieņemtos nosaukumus (“name” → “common”)
#print(atbilde.text)
#print(atbilde.json)

atbildeDict = json.loads(atbilde.text)  #pārveido par dictionary

def visparpienemtasValstis(atbildeDict):
    for valsts in atbildeDict:
        print(valsts['name']['common'])

#visparpienemtasValstis(atbildeDict)
#print(atbildeDict[0]['name']['common']) #izprinte pasu pirmo ierakstu

#4. kopejais valsts skaits
def kopejaisValstuSkaits(atbildeDict):
    skaits = len(atbildeDict)
    print(f"Kopā ir dati par {skaits} valstīm")
    return skaits

visparpienemtasValstis(atbildeDict)
kopejaisValstuSkaits(atbildeDict)