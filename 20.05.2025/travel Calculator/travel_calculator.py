# travel_calculator.py

def get_distance_between_cities(city1, city2):
    fake_distances = {
        ("София", "Пловдив"): 145,
        ("София", "Варна"): 470,
        ("Пловдив", "Бургас"): 250,
        ("Русе", "Варна"): 195,
        ("София", "Бургас"): 390,
    }

    key = (city1, city2)
    reverse_key = (city2, city1)

    if key in fake_distances:
        return fake_distances[key]
    elif reverse_key in fake_distances:
        return fake_distances[reverse_key]
    else:
        return None

def calculate_travel_cost(city1, city2, price_per_km=0.25):
    distance = get_distance_between_cities(city1, city2)

    if distance is None:
        return f"Нямаме данни за разстоянието между {city1} и {city2}."

    cost = distance * price_per_km
    return f"Разстоянието между {city1} и {city2} е {distance} км. Цена за пътуване: {cost:.2f} лв."
if __name__ == "__main__":
    city1 = input("Въведи първи град: ")
    city2 = input("Въведи втори град: ")
    print(calculate_travel_cost(city1, city2))
