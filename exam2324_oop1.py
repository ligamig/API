#4. daļa
#1. uzdevums
import csv
with open('agenti.csv', newline='', encoding='utf-8') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    # for row in spamreader:
    #     print(', '.join(row))
    #     print("Un vēl ir")
    dati = [row for row in spamreader]

    iestades = [row for row in dati if row[0] in ['Izglītības iestāde', 'Valsts iestāde']]
    for row in iestades:
        print(iestades)

    adrese = [row for row in iestades if 'Rīga' in row [2]]
    for row in adrese:
        print(adrese)

    sorted = sorted(adrese, key=lambda x:x[1])
    for row in sorted:
        print(f"{row[1]} - {row[2]}")