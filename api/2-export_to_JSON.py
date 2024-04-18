#!/usr/bin/python3
"""This module gather data form an API"""
import json
import requests
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
            data["task"] = str(each["title"])
            data["completed"] = each["completed"]
            data["username"] = str(USERNAME)
            data_list.append(data)

        user_todo = {}
        user_id = str(USER_ID)
        user_todo[user_id] = data_list

        json_file = '{}.json'.format(USER_ID)

        with open(json_file, 'w') as file:
            json.dump(user_todo, file)
    else:
        print('Request failed with user status code:', user.status_code)
