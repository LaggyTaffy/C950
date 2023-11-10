import csv

from hashtable import ChainingHashTable
from packages import Packages


def packagesimport():
    with open('CSVs/packages.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for packages in reader:
            packagesID = packages[0]
            packagesaddress = packages[1]
            packagescity = packages[2]
            packagesstate = packages[3]
            packageszip = packages[4]
            packagesdeadline = packages[5]
            packagesweight = packages[6]


            packages = Packages(packagesID, packagesaddress, packagescity, packagesstate, packageszip, packagesdeadline, packagesweight, "HUB", "8:00 AM", "N/A")

            myHash.insert(packagesID, packages)


myHash = ChainingHashTable()
packagesimport()
