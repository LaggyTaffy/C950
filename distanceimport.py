import csv

dList = []

class Distance:
    def __init__(self, distance):
        self.distance = distance

    def __str__(self):
        return self.distance

def distanceimport():
    with open('CSVs/distances.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for distance in reader:
            dList.append(distance)

distanceimport()

def distancecheck():
    distance = float(dList[start][end])

    return distance