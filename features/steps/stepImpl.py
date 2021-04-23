import requests
from behave import *
from payload import *
from utilities.resources import *
from utilities.configuration import *


@given('the provided credential')
def step_impl(context):
   context.url = getConfig()['API']['endpoint'] + apiResources.login

@when(u'we execute the Login PostAPI method')
def step_impl(context):
    context.loginapi_response = requests.post(context.url,
                                      json=loginPayload(),
                                      headers={"Content-Type": "application/json"})

@then(u'Login should be successfull')
def step_impl(context):
    print(context.loginapi_response.status_code)
    response_json = context.loginapi_response.json()

@then('status code should be 200')
def step_imple(context):
    #validate the status code from API response
    assert context.loginapi_response.status_code == 200

@then('error code should be False')
def step_imple(context):
    #Validate error response field value
    context.response_json = context.loginapi_response.json()
    error_response = context.response_json['error']
    assert error_response == False

@then('extract token and save it')
def step_imple(context):
    #We need to save token in a variable ,it should be accessible globally
    context.token = context.response_json['data']['key']
    payload.setToken(context.token)
    print("Token ID for the logged in user is:")
    print(payload.getToken())

