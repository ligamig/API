#4. daļa
#1. uzdevums
import csv
with open('agenti.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        print(', '.join(row))
        print("Un vēl ir")