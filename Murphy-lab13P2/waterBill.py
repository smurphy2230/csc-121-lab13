from utilityBill import UtilityBill

class WaterBill(UtilityBill):

    def __init__(self, name, address):
        super().__init__(name, address)
        self._gallonsUsed = 0

    def calculateCharge(self):
        cost = 0
        water_used = float(input("Enter number of gallons used:"))
        self._gallonsUsed = water_used
        if self._gallonsUsed <= 6000:
            cost = self._gallonsUsed * .005
        elif self._gallonsUsed > 6000:
            cost = (6000 * .005) + ((self._gallonsUsed - 6000) * .007)
        self._total = cost
        print()

    def displayBill(self):
        print("Water bill")
        print("Name: ", self._name)
        print("Address: ", self._address)
        print("Water used: ", self._gallonsUsed)
        print("Amount due: ", self._total)


