#!/usr/bin/python3
"""task 0"""
import requests
from sys import argv


if __name__ == '__main__':
    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url+'/users/'+id)
    name = user.json().get('name')
    all = requests.get(url+'/todos')

    data = all.json()
    total = 0
    completed = 0

    for i in data:
        total += 1
        if i.get('completed'):
            completed += 1

    print("""Employee {} is done with tasks({}/{}):
        """.format(name, completed, total))
    for i in data:
        if i.get('completed'):
            print('\t {}'.format(i.get('title')))
