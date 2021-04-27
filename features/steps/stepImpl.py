import requests
from behave import *
from payload import *
from utilities.resources import *
from utilities.configuration import *

#Step:1 Login API

# note: all the response of API has been saved in same variable

@given('the URL and the login credentials {login} and {password}')
def step_impl(context,login,password):
   context.url = getConfig()['API']['endpoint'] + apiResources.login
   context.payload = loginPayload(login,password)

@when(u'we execute the Login PostAPI method')
def step_impl(context):
    context.response = requests.post(context.url,
                                      json=context.payload,
                                      headers={"Content-Type": "application/json"})

@then(u'Login should be successfull')
def step_impl(context):
    print(context.response.status_code)
    response_json = context.response.json()

@then('status code should be {statusCode:d}')
def step_imple(context,statusCode):
    #validate the status code from API response
    assert context.response.status_code == statusCode

@then('error code should be False')
def step_imple(context):
    #Validate error response field value
    context.response_json = context.response.json()
    error_response = context.response_json['error']
    assert error_response == False

@then('extract token and save it')
def step_imple(context):
    #We need to save token in a variable ,it should be accessible globally
    context.token = context.response_json['data']['key']
    payload.setToken(context.token)
    print("Token ID for the logged in user is:")
    print(payload.getToken())

#Step:2
# ----------------------Step2---------------------

@given('the Authorization')
def step_impl(context):
    context.url = getConfig()['API']['endpoint'] + apiResources.getClient
    context.Authorization = {'Authorization' : payload.getToken()}


@when(u'the Clients GetAPI is executed')
def step_impl(context):
    context.response = requests.get(context.url,
                                          headers=context.Authorization)
    context.response_json = context.response.json()


@when(u'error should be false')
def step_impl(context):
    assert context.response_json['error'] == False


@then(u'store the client ID {ClientName}')
def step_impl(context, ClientName):
    for result in context.response_json['data']['clients']:
        if(result['name']) == ClientName:
            payload.setClientID(result['id'])
            print(result['name'])
            print(payload.getClientID())
            break
    payload.setClientID(payload.setClientID(result['id']))