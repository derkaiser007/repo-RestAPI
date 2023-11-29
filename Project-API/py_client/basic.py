import requests

#endpoint = "https://httpbin.org"
#endpoint = "https://httpbin.org/anything"
#endpoint = "https://httpbin.org/status/200/"

#endpoint = "http://127.0.0.1:8000/"
endpoint = "http://127.0.0.1:8000/api/"
#endpoint = "http://127.0.0.1:8000/api/?abc=123" #endpoint = "http://127.0.0.1:8000/api/?this_arg=this_value"


#get_response = requests.get(endpoint)
#get_response = requests.get(endpoint, params={"abc":"123"}, json={"query":"Niraj"})
get_response = requests.post(endpoint, json={"title":"Niraj"})

#print(get_response.text)
print(get_response.json())
#print(get_response.status_code)
#print(get_response.json()['message'])



