import requests

# response = requests.get("https://skyscendbs.com")
# print(response, type(response))
# # print(dir(response))
# print(response.text)
# print(response.url)

user_dict = {
    "jsonrpc": "2.0",
    "params": {
        "db": "trn_14_2",
        "login": "admin",
        "password": "admin"
    }
}
# #
response = requests.post('http://0.0.0.0:8069/web/session/authenticate', json=user_dict)
print(response.json())
