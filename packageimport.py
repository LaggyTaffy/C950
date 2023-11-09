import csv

from hashtable import ChainingHashTable


class Package:
    def __init__(self, packageID, packageaddress, packagecity, packagestate, packagezip, packagedeadline, packageweight):
        self.packageID = packageID
        self.packageaddress = packageaddress
        self.packagecity = packagecity
        self.packagestate = packagestate
        self.packagezip = packagezip
        self.packagedeadline = packagedeadline
        self.packageweight = packageweight

    def __str__(self):
        return self.packageID, self.packageaddress, self.packagecity, self.packagestate, self.packagezip, self.packagedeadline, self.packageweight

def packageimport():
    with open('CSVs/packages.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        next(reader)
        for package in reader:
            packageID = package[0]
            packageaddress = package[1]
            packagecity = package[2]
            packagestate = package[3]
            packagezip = package[4]
            packagedeadline = package[5]
            packageweight = package[6]


            package = Package(packageID, packageaddress, packagecity, packagestate, packagezip, packagedeadline, packageweight)

            myHash.insert(packageID, package)



myHash = ChainingHashTable()
packageimport()



