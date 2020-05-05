#!/usr/bin/python3
"""task 1"""


if __name__ == '__main__':
    import requests
    import csv
    from sys import argv

    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url+'/users/'+id)
    name = user.json().get('name')
    user = requests.get(url+'/todos?userId={}'.format(argv[1]))

    data = user.json()

    with open('{}.csv'.format(argv[1]), mode='w') as f:
        file = csv.writer(f, delimiter=',', quotechar='"',
                          quoting=csv.QUOTE_ALL)
        for i in data:
            file.writerow([argv[1], name, i.get('completed'),
                           i.get('title')])
