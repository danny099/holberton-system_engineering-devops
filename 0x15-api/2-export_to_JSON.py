#!/usr/bin/python3
"""task 1"""


if __name__ == '__main__':

    import json
    import requests
    from sys import argv

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url+'/users/'+id)
    name = user.json().get('name')
    user = requests.get(url+'/todos?userId={}'.format(argv[1]))

    data = user.json()

    jsons = {}
    jsons['{}'.format(argv[1])] = []
    for i in data:
        jsons['{}'.format(argv[1])].append({
            'task': i.get('title'),
            'completed': i.get('completed'),
            'username': name
        })

    with open('{}.json'.format(argv[1]), 'w') as f:
        json.dump(jsons, f)
