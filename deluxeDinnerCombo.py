from dinnerCombo import Dinner_combo


class DeluxeDinnerCombo(Dinner_combo):

    def __init__(self):
        super().__init__()
        self._appetizer = ""

    def choose_appetizer(self):
        appetizer = int(input("Enter 1 for spring roll, 2 for chicken wing: "))
        if appetizer == 1:
            self._appetizer = "spring roll"
        elif appetizer == 2:
            self._appetizer = "chicken wing"

    def displayOrder(self):
        dish_cost = 0
        soup_cost = 0
        appetizer_cost = 0
        if self._main_dish == "sweet and sour pork":
            dish_cost = 7
        elif self._main_dish == "sesame chicken":
            dish_cost = 8
        elif self._main_dish == "shrimp fried rice":
            dish_cost = 9
        if self._soup == "egg drop soup":
            soup_cost = 1.25
        elif self._soup == "wanton soup":
            soup_cost = 1.50
        if self._appetizer == "spring roll":
            appetizer_cost = 1.25
        elif self._appetizer == "chicken wing":
            appetizer_cost = 1.50
        self._total = dish_cost + soup_cost + appetizer_cost
        print("Your order is: ", self._main_dish + ", " + self._soup + ", " + self._appetizer)
        print("Your total is: ${:.2f}".format(self._total))

