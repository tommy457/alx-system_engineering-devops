#!/usr/bin/python3
"""
Script that, using jsonplaceholder API, for a given employee ID,
returns information about his/her TODOs list progress,
export data in the JSON format.
"""
import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    users_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        user_id)

    users_res = requests.get(users_url)
    todos_res = requests.get(todos_url)

    user = users_res.json()
    todos = todos_res.json()

    total_taks = len(todos)
    nmbr_of_done_task = 0
    todos_titles = ""

    for todo in todos:
        if todo.get("completed"):
            nmbr_of_done_task += 1
            todos_titles += "\t" + " " + todo.get("title") + "\n"

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"),
        nmbr_of_done_task,
        total_taks)
        )
    print(todos_titles, end="")

    user_dict = {}
    user_dict[user_id] = []
    for todo in todos:
        task = {"task": todo.get("title"),
                "completed": todo.get("completed"),
                "username": user.get("username"),
                }
        user_dict[user_id].append(task)

    with open("{}.json".format(user_id), 'w') as jsonfile:
        json.dump(user_dict, jsonfile)
