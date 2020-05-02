class Dinner_combo:

    """constructor"""

    def __init__(self):
        self._main_dish = ""
        self._soup = ""
        self._total = 0.0

    def choose_dish(self):
        main_dish = int(input("Enter 1 for sweet and sour pork, 2 for sesame chicken, "
                             "3 for shrimp fried rice: "))
        if main_dish == 1:
           self._main_dish = "sweet and sour pork"
        elif main_dish == 2:
            self._main_dish = "sesame chicken"
        elif main_dish == 3:
            self._main_dish = "shrimp fried rice"

    def choose_soup(self):
        soup = int(input("Enter 1 for egg drop soup, 2 for wanton soup: "))
        if soup == 1:
            self._soup = "egg drop soup"
        elif soup == 2:
            self._soup = "wanton soup"

    def displayOrder(self):
        dish_cost = 0
        soup_cost = 0
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
        self._total = dish_cost + soup_cost
        print("Your order is: ", self._main_dish, self._soup)
        print("Your total is: ${:.2f}".format(self._total))
