import requests

#endpoint = "http://httpbin.org/anything"
endpoint = "http://127.0.0.1:8001/"

# HTTP Request
get_response = requests.get(endpoint, data={"query": "Hello World"}) #API Method (ie get)
#Print raw text response code
print(get_response.text)
print(get_response.status_code)