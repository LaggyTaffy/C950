class Packages:
    def __init__(self, packagesID, packageaddress, packagedeadline, packagecity, packagesstate, packagezip, packageweight, packagesstatus, packagesdeparturetime, packagesdeliverytime):
        self.packagesID = packagesID
        self.packagesaddress = packageaddress
        self.packagesdeadline = packagedeadline
        self.packagescity = packagecity
        self.packagesstate = packagesstate
        self.packageszip = packagezip
        self.packagesweight = packageweight
        self.packagesstatus = packagesstatus
        self.packagesdeparturetime = packagesdeparturetime
        self.packagesdeliverytime = packagesdeliverytime

    def __str__(self):
        return self.packagesID, self.packagesaddress, self.packagescity, self.packagesstate, self.packageszip, self.packagesdeadline, self.packagesweight, self.packagesstatus, self.packagesdeparturetime, self.packagesdeliverytime
