import json

json_string = '{"name": "John", "age": 30, "city": "New York"}'
loaded_json = json.loads(json_string)
print(loaded_json['age'])

json_dict = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
converted_json = json.dumps(json_string)
print(converted_json)

x = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann","Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
  ]
}

# use . and a space to separate objects, and a space, a = and a space to separate keys from their values:
print(json.dumps(x, indent=4, separators=("; ", " -> "), sort_keys=True))