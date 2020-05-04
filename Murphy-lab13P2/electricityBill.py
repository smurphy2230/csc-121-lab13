from utilityBill import UtilityBill


class ElectricityBill(UtilityBill):

    def __init__(self, name, address):
        super().__init__(name, address)
        self._kwhUsed = 0

    def calculateCharge(self):
        cost = 0
        kilowatt_used = float(input("Enter kilowatt hours used: "))
        self._kwhUsed = kilowatt_used
        if self._kwhUsed <= 500:
            cost = self._kwhUsed * .12
        elif self._kwhUsed > 500:
            cost = (500 * .12) + ((self._kwhUsed - 500) * .15)
        self._total = cost
        print()

    def displayBill(self):
        print("Electricity bill")
        print("Name: ", self._name)
        print("Address: ", self._address)
        print("kilowatt Hours used: ", self._kwhUsed)
        print("Amount due: ", self._total)
