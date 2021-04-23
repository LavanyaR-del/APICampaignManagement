import requests
import json
import configparser
from payLoad import *
from utilities.configuration import *
from utilities.resources import *


loginapi_response = requests.post('https://report-staging.aiquire.com/api/auth/login/',json =loginAPI(),
    headers = {"Content-Type":"application/json"},)

# url = getConfig()['API']['endpoint'] + apiResources.login
#
# loginapi_response = requests.post(url,
#                                   json =loginAPI(),
#                                   headers ={"Content-Type":"application/json"})



print("API Response")
print(loginapi_response.json())
print("Status Code for the given API is :")
print(loginapi_response.status_code)
response_json  = loginapi_response.json()

error_response = response_json['error']
key_value = response_json['data']['key']
print("Key which is generated for the provided API is:")
print(key_value)
print(error_response)
assert error_response == False
assert loginapi_response.status_code == 200

print("***************************************************************")

response = requests.get('https://report-staging.aiquire.com/api/api/clients/',
                        headers = {'authorization': "Token f0b3ff6d5da1431c3ba92dc690174a3183567490", 'Content-Type': 'application/json'}, )
#print(response.text)
# print(type(response.text))
#need to know how to capture the Key from previous file to here

json_response = response.json()
print(json_response)
print(json_response['error'])

#assert json_response['error'] == 'True'
# how to do Validation for the value which is returned by error Key?????

#assert response.error == 'True'
print(response.status_code)
print("Value of response is:")
print(response.json())
print(response.url)
assert response.headers['Content-Type'] == 'application/json'