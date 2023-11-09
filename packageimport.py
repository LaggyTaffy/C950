import csv

from hashtable import ChainingHashTable


'''
class Package:
    def __init__(self, packageID, packageaddress, packagecity, packagestate, packagezip, packagedeadline,
                 packageweight):
        self.packageID = packageID
        self.packageaddress = packageaddress
        self.packagecity = packagecity
        self.packagestate = packagestate
        self.packagezip = packagezip
        self.packagedeadline = packagedeadline
        self.packageweight = packageweight

    def __str__(self):
        return self.packageID, self.packageaddress, self.packagecity, self.packagestate, self.packagezip, self.packagedeadline, self.packageweight
'''


def packageimport():
    with open('CSVs/packages.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for package in reader:

            packageID = package[1]
            packageaddress = package[2]
            packagecity = package[3]
            packagestate = package[4]
            packagezip = package[5]
            packagedeadline = package[6]
            packageweight = package[7]

            package = Package(packageID, packageaddress, packagecity, packagestate, packagezip, packagedeadline, packageweight)

            myHash.insert(packageID, package)


myHash = ChainingHashTable()
myHash.insert(1, "one")
print(myHash.table)
