def meal_cost():
    meal = float(input()) # cost of meal before tax an tip
    tip = float(input()) # percentage of tip
    tax = float(input()) # percentage of tax
    tip = tip / 100 # decimal of tip
    tax = tax / 100 # decimal of tax
    totalCost = meal + (meal * tip) + (meal * tax) # cost of meal including tax and tip
    print('The total meal cost is {0} dollars.'.format(round(totalCost)))

meal_cost()