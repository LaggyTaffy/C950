import csv

from distance import Distance


distancetable = []

def distanceimport():
    with open('CSVs/distances.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for distance in reader:
            distancetable.append(distance)

distanceimport()

def distancecheck(start, end):
    distance = distancetable[start][end]
    if distance == '':
        distance = distancetable[end][start]
    return float(distance)