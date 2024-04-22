#!/usr/bin/python3

"""
Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS,
"username": "USERNAME"}, ... ]}
"""

import json
import requests

if __name__ == "__main__":
    url_user = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url_user + "users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url_user + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, jsonfile)
