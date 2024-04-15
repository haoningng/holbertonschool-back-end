#!/usr/bin/python3
"""This module gather data form an API"""
import requests
import csv
import sys


if __name__ == "__main__":
    USER_ID = sys.argv[1]
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(USER_ID))
    todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                         .format(USER_ID))
    if user.status_code == 200 and todos.status_code == 200:
        USERNAME = user.json()["username"]

        data_list = []

        for each in todos.json():
            data = {}  # Create a new dictionary for each iteration
            data["USER_ID"] = str(USER_ID)
            data["USERNAME"] = str(USERNAME)
            data["TASK_COMPLETED_STATUS"] = str(each["completed"])
            data["TASK_TITLE"] = str(each["title"])
            data_list.append(data)

        keys = data.keys()
        csv_file = '{}.csv'.format(USER_ID)

        with open(csv_file, 'w', newline='') as file:
            writer = csv.DictWriter(file,
                                    fieldnames=keys,
                                    quoting=csv.QUOTE_ALL)
            for row in data_list:
                writer.writerow(row)
    else:
        print('Request failed with user status code:', user.status_code)
