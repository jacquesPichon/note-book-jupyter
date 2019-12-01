import csv

films=[]

with open('films.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter =';')
    next(spamreader)
    for row in spamreader:
        print(row)
    
    