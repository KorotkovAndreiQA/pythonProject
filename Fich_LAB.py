import requests
import json

def test_post_create():
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    body = json.dumps({
        "email": "andrewkorotkow@gmail.com",
        "password": "5002035ak"
    })
    response = requests.post(
        "http://109.68.212.118/auth/jwt/create/",
        data=body,
        headers=headers
    ).json()
    print(response)


def test_post_refresh():
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    body = json.dumps({

            "refresh": 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcxMzc3Nzc4MSwiaWF0IjoxNzEzMTcyOTgxLCJqdGkiOiI2NjAxY2EyODk5N2M0NGUxYTVjMmVlZGYyMDFhNTQ3MCIsInVzZXJfaWQiOjQ1fQ.DSGUdegADVdpB7JLEjEO8BDeEo9W5P2ZfbNRpm5m5fE'

    })
    response = requests.post(
        "http://109.68.212.118/auth/jwt/refresh/",
        data=body,
        headers=headers
    ).json()
    print(response)



def test_post_verify():
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    body = json.dumps({
        "token": 'eyJhbGciOiJIUzI1NiI   0sInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzEzMTgwNzA3LCJpYXQiOjE3MTMxNzI5ODEsImp0aSI6ImFlZTIyZjZiNTRhODRkNzU5NjEyZTFiOGU4NjMyYjE2IiwidXNlcl9pZCI6NDV9.KVvW2jCL_fJJk_JDEnK_iitzFYFe6pkecsBP9Piw76g'
    })
    response = requests.post(
        "http://109.68.212.118/auth/jwt/verify/",
        data=body,
        headers=headers
    ).json()
    print(response)



def test_get_competence():
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    response = requests.get(
        "http://109.68.212.118/api/v1/competence/",
        headers=headers
    ).json()
    print(response)




