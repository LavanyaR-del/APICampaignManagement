import token
import payload

# global variable
token = "Key value to be used"

def loginPayload(login,
                 password):
    body = {
        "email": login,
        "password": password
    }
    return body

def setToken(token):
    payload.token = token

def getToken():
    return "Token " + token

def setClientID(clientID):
    payload.clientID = clientID

def getClientID():
    return payload.clientID