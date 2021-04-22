import requests
from postAPI import *


#response = requests.get('https://report-staging.aiquire.com/api/api/clients/',
#                        headers = {'authorization':'Token f0b3ff6d5da1431c3ba92dc690174a3183567490','Content-Type':'application/json'},)

response = requests.get('https://report-staging.aiquire.com/api/api/clients/',
                     headers = {'authorization':'Token key_value','Content-Type':'application/json'},)


#print(response.text)
# print(type(response.text))

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
