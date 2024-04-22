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
    user_id = sys.argv[1]
    url_user = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url_user + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url_user + "todos", params={"userId": user_id}).json()

    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, username, t.get("completed"), t.get("title")]
         ) for t in todos]
