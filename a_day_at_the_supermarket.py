"""
solution for a_day_at_the_supermarket
"""
"""
Make the following changes to your compute_bill function:

While you loop through each item of food, only
add the price of the item to total if the item's
stock count is greater than zero.
If the item is in stock and after you add the
price to the total, subtract one from the item's stock count.
"""


def a_day_at_the_supermarket():
    """
    a_day_at_the_supermarket
    """
    shopping_list = ["banana", "orange", "apple"]
    stock = {
        "banana": 6,
        "apple": 0,
        "orange": 32,
        "pear": 15
        }
    prices = {
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
        }

    def compute_bill(food):
        """
        Calculates the bill based on list of groceries
        """
        total = 0
        for item in food:
            print item
            if stock[item] > 0:
                total += prices[item]
                stock[item] -= 1
        return total
    print "Grocery Bill ${:0.2f}".format(compute_bill(shopping_list))

a_day_at_the_supermarket()
