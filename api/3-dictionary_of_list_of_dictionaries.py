#!/usr/bin/python3
"""This module gather data form an API"""
import json
import requests

if __name__ == "__main__":
    try:
        all_todos = requests.get(
            'https://jsonplaceholder.typicode.com/todos')
        done_user = []
        user_todo = {}
        for each in all_todos.json():
            USER_ID = each["userId"]
            while (USER_ID not in done_user):
                done_user.append(USER_ID)
                user = requests.get(
                    'https://jsonplaceholder.typicode.com/users/{}'
                    .format(USER_ID))
                USERNAME = user.json()["username"]
                todos = requests.get(
                    'https://jsonplaceholder.typicode.com/users/{}/todos'
                    .format(USER_ID))
                data_list = []
                for each in todos.json():
                    data = {}  # Create a new dictionary for each iteration
                    data["username"] = str(USERNAME)
                    data["task"] = str(each["title"])
                    data["completed"] = each["completed"]
                    data_list.append(data)
                user_todo[str(USER_ID)] = data_list
        json_file = 'todo_all_employees.json'
        with open(json_file, 'w') as file:
            json.dump(user_todo, file)
    except Exception:
        print('Request failed with status code not equal to 200')
