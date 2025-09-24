import requests

get_url = "http://127.0.0.1:5000/handle_get"
post_url = "http://127.0.0.1:5000/handle_post"

# Test GET
# 
data = {"temperature": "25"}
get_response = requests.get(get_url, params=data)
print("GET status:", get_response.status_code)
print("GET response text:", get_response.text)

# Test POST
# 
data = {"temperature": "30"}
post_response = requests.post(post_url, data=data)
print("POST status:", post_response.status_code)
print("POST response text:", post_response.text)