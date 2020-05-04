class UtilityBill:

    """constructor"""

    def __init__(self, name, address):
        self._name = name
        self._address = address
        self._total = 0

    def calculate_charge(self):
        raise NotImplementedError("Method calculate_charge not implemented")

    def display_bill(self):
        raise NotImplementedError("Method display_bill not implemented")
