# import requests
# import json

# res = requests.get("https://jsonplaceholder.typicode.com/todos")
# todos = json.loads(res.text)

# users = [1, 2, 3]   

# def find(todo):
#     check = todo["completed"]
#     max_var = todo["userId"] in users
#     return check and max_var

# Value = list(filter(find, todos))
# # Read Data
# with open("sample.json", "w") as data:
#     json.dump(Value, data, indent=2)

# Writtind data
import json
data = {
    "name": "sathiyajith",
    "rollno": 56,
    "cgpa": 8.6,
    "phone": "9976770500"
}
# indent: defines the number of units for indentation
json_str = json.dumps(data, indent=4)
with open("sample.json", "w") as f:
    f.write(json_str)