"""
taking_a_vacation
"""
def hotel_cost(nights):
    """
    hotel_cost
    """
    return nights * 140
def plane_ride_cost(city):
    """
    plane_ride_cost
    """
    switcher = {
        "Charlotte" : 183,
        "Tampa" : 220,
        "Pittsburgh" : 222,
        "Los Angeles" : 475
        }
    return switcher.get(city, -1)
def rental_car_cost(days):
    """
    rental_car_cost
    """
    if days >= 7:
        return (days * 40) - 50
    elif days >= 3 and days < 7:
        return days * 40 - 20
    else:
        return days * 40
def trip_cost(city, days, spending_money):
    """
    trip_cost
    """
    return rental_car_cost(days) + plane_ride_cost(city) + hotel_cost(days) + spending_money
print trip_cost("Los Angeles", 5, 600)
