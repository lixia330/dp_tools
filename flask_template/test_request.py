import requests, json

url = "http://127.0.0.1:8888/test_api"
input = {"test":"hello my name is zhanglixia"}
response = requests.get(url=url, params=input)

print(json.loads(response.text))