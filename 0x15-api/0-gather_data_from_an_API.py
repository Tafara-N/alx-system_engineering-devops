#!/usr/bin/python3

"""
Script that, for a given employee ID,
returns information about his/her TODO list progress.

First line: Employee EMPLOYEE_NAME is done with tasks
(NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
    :EMPLOYEE_NAME: name of the employee
    :NUMBER_OF_DONE_TASKS: number of completed tasks
        :TOTAL_NUMBER_OF_TASKS: total number of tasks, which is the sum
        of completed and non-completed tasks
"""

import re
import requests
import sys

REST_API = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if re.fullmatch(r"\d+", sys.argv[1]):
            id = int(sys.argv[1])
            req = requests.get("{}/users/{}".format(REST_API, id)).json()
            task_request = requests.get("{}/todos".format(REST_API)).json()
            employee_name = req.get("name")
            tasks = list(filter(lambda x: x.get("userId") == id, task_request))
            complete_tasks = list(filter(lambda x: x.get("completed"), tasks))
            print(
                "Employee {} is done with tasks({}/{}):".format(
                    employee_name,
                    len(complete_tasks),
                    len(tasks)
                )
            )
            if len(complete_tasks) > 0:
                for task in complete_tasks:
                    print("\t {}".format(task.get("title")))
