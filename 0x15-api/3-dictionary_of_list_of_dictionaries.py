#!/usr/bin/python3
"""
Script that, using jsonplaceholder API, for a given employee ID,
returns information about his/her TODOs list progress,
export data in the JSON format.
"""
import json
import requests

if __name__ == "__main__":
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_res = requests.get(users_url)
    users = users_res.json()

    user_dict = {}

    for user in users:
        todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".\
            format(user.get("id"))
        todos_res = requests.get(todos_url)
        todos = todos_res.json()
        user_dict[user.get("id")] = []

        for todo in todos:

            task = {"username": user.get("username"),
                    "task": todo.get("title"),
                    "completed": todo.get("completed"),
                    }
            user_dict[user.get("id")].append(task)

    with open("todo_all_employees.json", 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
