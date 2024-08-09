import requests
import json


def get_all_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts").json()
    for x in response:
        print(x)


def get_one_post():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/42").json()
    print(response)


def post_new_post():
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    body = json.dumps({
        "title": "Auto_test",
        "body": "Python3",
        "userId": "5"
    })
    response = requests.post(
        "https://jsonplaceholder.typicode.com/posts",
        data=body,
        headers=headers
    )
    print(response.json())
    print(response.status_code)


def update_post():
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    body = json.dumps({
        "title": "Auto_test1",
        "body": "Python4",
        "userId": "7"
    })
    response = requests.put(
"https://jsonplaceholder.typicode.com/posts/42",
        data=body,
        headers=headers
    ).json()
    print(response)


def patch_post():
    headers = {
        'Content-type': 'application/json; charset=UTF-8'
    }
    body = json.dumps({
        "title": "Auto_test4",
        "userId": "9"
    })
    response = requests.patch(
        "https://jsonplaceholder.typicode.com/posts/42",
        data=body,
        headers=headers
    ).json()
    print(response)
    print(response.status_code)


def delete_post():
    response = requests.delete("https://jsonplaceholder.typicode.com/posts/42")
    print(response.text)
    print(response.status_code)


delete_post()

