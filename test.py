import requests

local_url = 'http://localhost:8080/2015-03-31/functions/function/invocations'
stage_url = 'https://e6yc5urqh1.execute-api.eu-central-1.amazonaws.com/test/predict'
data = { 'url': 'http://bit.ly/mlbookcamp-pants'}

result = requests.post(local_url, json=data).json()
print(result)