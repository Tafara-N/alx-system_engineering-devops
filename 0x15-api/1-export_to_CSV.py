#!/usr/bin/python3

"""
Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE",
                "complete": TASK_complete_STATUS, "username": "USERNAME"},
                {"task": "TASK_TITLE", "complete": TASK_complete_STATUS,
                "username": "USERNAME"}, ... ]}
"""

import csv
import requests
import sys

if __name__ == '__main__':
    user = sys.argv[1]
    url_user = 'https://jsonplaceholder.typicode.com/users/' + user
    res = requests.get(url_user)
    """ Whatever you want to do with the response """

    user_name = res.json().get('username')
    task = url_user + '/todos'
    res = requests.get(task)
    tasks = res.json()

    with open('{}.csv'.format(user), 'w') as csvfile:
        for task in tasks:
            complete = task.get('complete')
            """ Completed task """

            title_task = task.get('title')
            """ Task done """

            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, user_name, complete, title_task))
