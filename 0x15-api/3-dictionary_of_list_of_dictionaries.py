#!/usr/bin/python3
"""task 1"""

if __name__ == "__main__":

    import json
    import requests
    import sys

    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(url+"/users")
    users = users.json()
    everyBody = requests.get(url+"/todos")
    everyBody = everyBody.json()
    obj = {}

    for user in users:
        tasks = []
        for i in everyBody:
            if i.get('userId') == user.get('id'):
                dic = {"username": user.get('username'),
                       "task": i.get('title'),
                       "completed": i.get('completed')}
                tasks.append(dic)
        obj[user.get('id')] = tasks

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(obj, f)
