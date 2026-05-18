def hotel_cost(nights):
    return 140*nights


def plane_ride_cost(city):
    if "Charlotte" == city:
        return 183
    elif "Tampa" == city:
        return 220
    elif "Pittsburgh" == city:
        return 222
    elif "Los Angeles" == city:
        return 475

def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days


def trip_cost(city, days, spending_money) :
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money

print(" cost of our car rental:", rental_car_cost)

print("cost of our plane ride:", plane_ride_cost)

print("cost of our hotel room", hotel_cost)

print("cost of our trip", trip_cost)

print(trip_cost("Tampa", 6500))
