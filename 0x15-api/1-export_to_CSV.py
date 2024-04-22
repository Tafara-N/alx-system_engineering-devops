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

if __name__ == "__main__":
    user = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/users/" + user
    response = requests.get(url_user)
    username = response.json().get("username")
    task = url_user + "/todos"
    response = requests.get(task)
    tasks = response.json()

    with open("{}.csv".format(user), "w") as csvfile:
        for task in tasks:
            complete = task.get("complete")
            title_task = task.get("title")
            csvfile.write('"{}","{}","{}","{}"\n'.format(
                user, username, complete, title_task))
