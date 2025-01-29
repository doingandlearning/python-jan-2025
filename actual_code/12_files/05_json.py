import json

data = {
    "employees": [
        {"name": "Brian", "age": True, "city": "London"},
        {"name": "Jui", "age": -10, "city": "New York"},
        {"name": "Leoni", "age": 17.2, "city": "Paris"}
    ]
}

with open("employees.json", "w") as file:
    json.dump(data, file, indent=2)
try:
    with open("employees.json") as file:
        loaded_data = json.load(file)
        print(loaded_data)
    with open("employees.json", "w") as file:
        loaded_data["employees"].append({"name": "Luke", "age": 1003, "city": "Athens"})
        json.dump(loaded_data, file, indent=2)
except json.JSONDecodeError:
    print("The JSON looks faulty - check it!")



