from waterBill import WaterBill
from electricityBill import ElectricityBill


def main():
    name = input("Enter name: ").upper()
    address = input("Enter address: ").upper()
    choice = int(input("Enter 1 for water bill, 2 for electricity bill: "))
    if choice == 1:
        water_bill = WaterBill(name, address)
        water_bill.calculateCharge()
        water_bill.displayBill()
    elif choice == 2:
        electric_bill = ElectricityBill(name, address)
        electric_bill.calculateCharge()
        electric_bill.displayBill()


main()


