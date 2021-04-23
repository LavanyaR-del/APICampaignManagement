import token

import payload

def loginPayload():
    body = {
        "email" : "test@aiquire.com",
        "password" : "123456"
    }
    return body

def setToken(token):
    payload.token = token

def getToken():
    return "Token "+token