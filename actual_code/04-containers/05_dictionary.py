"""
Ordered - Unordered
Mutable - Immutable
Allow duplicates or not
Reference by key or index
Growable or fixed

Dictionary
- Ordered/Unordered
- Mutable
- Disallow duplicate keys
- Reference by key
- Growable
"""

cities = {
    "Wales": "Cardiff",
    "Scotland": "Edinburgh",
    "England": "London",
    "NI": "Belfast"
}

print(cities)
print(cities["Wales"])
print(cities.values())
print(cities.keys())
print(cities.items())

for (country, city) in cities.items():
    print(f"We care about {country} and it's capital {city}!")

print("Newcastle" in cities)
print("London" in cities)
print("England" in cities)

api_response = {
    "user": {
        "name": "Kevin",
        "region": "NI"
    },
    "date": "2025-01-28"
}

print(api_response["user"]["name"])

print(cities.get("England", "Paris"))