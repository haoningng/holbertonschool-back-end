#!/usr/bin/python3
"""This module gather data form an API"""
import requests
import sys


if __name__ == "__main__":
    EMPLOYEE_NAME = ""
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLE = []

    employee_id = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(employee_id))
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(employee_id))
    if user.status_code == 200 and todos.status_code == 200:
        EMPLOYEE_NAME = user.json()["name"]
        for each in todos.json():
            TOTAL_NUMBER_OF_TASKS += 1
            if each["completed"]:
                NUMBER_OF_DONE_TASKS += 1
                TASK_TITLE.append(each["title"])
        print("Employee {} is done with tasks({}/{}):"
              .format(EMPLOYEE_NAME,
                      NUMBER_OF_DONE_TASKS,
                      TOTAL_NUMBER_OF_TASKS))
        for each in TASK_TITLE:
            print("\t {}".format(each))
    else:
        print('Request failed with user status code:', user.status_code)
