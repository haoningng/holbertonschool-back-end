#!/usr/bin/python3
"""This module gather data form an API"""
import requests
import json
import sys

USER_ID = sys.argv[1]
user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                    .format(USER_ID))
todos = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                     .format(USER_ID))

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
