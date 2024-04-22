#!/usr/bin/python3

"""
Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}
"""

import csv
import json
import requests
import sys


if __name__ == "__main__":
    USER_ID = sys.argv[1]
    url_to_user = "https://jsonplaceholder.typicode.com/users/" + USER_ID
    response = requests.get(url_to_user)
    USERNAME = response.json().get("username")
    url_to_task = url_to_user + "/todos"
    response = requests.get(url_to_task)
    tasks = response.json()

    dictionary_data = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get("completed")
        TASK_TITLE = task.get("title")
        dictionary_data[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})

    """ Outputs 'dictionary_data' """
    with open("{}.json".format(USER_ID), "w") as f:
        json.dump(dictionary_data, f)
