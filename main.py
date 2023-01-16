import requests
import json

url = 'https://opentdb.com/api.php?amount=10&type=boolean'

response = requests.get(url)
data = response.json()

json_data = json.dumps(data, indent=1)
with open('data.json', 'w') as file:
    file.write(json_data)

# ___________________________________________________________________________________________________________




