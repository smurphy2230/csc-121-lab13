from dinnerCombo import Dinner_combo
from deluxeDinnerCombo import DeluxeDinnerCombo


def main():
    choice = int(input("Enter 1 for dinner combo, 2 for deluxe dinner combo: "))
    if choice == 1:
        dinner_combo = Dinner_combo()
        dinner_combo.choose_dish()
        dinner_combo.choose_soup()
        dinner_combo.displayOrder()
    if choice == 2:
        deluxe_combo = DeluxeDinnerCombo()
        deluxe_combo.choose_dish()
        deluxe_combo.choose_soup()
        deluxe_combo.choose_appetizer()
        deluxe_combo.displayOrder()


main()
