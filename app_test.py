import requests
import json

API_ENDPOINT = "http://127.0.0.1:5000/iparse"
json_input={
    "A":2,
    "B":6
    }
response = requests.post(url = API_ENDPOINT, data = json.dumps(json_input))
result_json=response.content
print result_json