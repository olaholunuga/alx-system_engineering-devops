#!/usr/bin/python3
"""Python script that, using this RE/her TODO list progress
"""

import requests
import sys

API = "https://jsonplaceholder.typicode.com"
"""API URL"""

if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = int(sys.argv[1])
        user_request = requests.get(
                "{}/users/{}".format(API, str(user_id))).json()
        user_todos = requests.get(
                "{}/todos".format(API)).json()
        todos = list(filter(lambda x: x.get("userId") == user_id,  user_todos))
        todos_done = list(filter(lambda x: x.get("completed"), todos))
        user_name = user_request.get("name")
        print(
                "Employee {} is done with tasks({}/{}):".format(
                    user_name,
                    len(todos_done),
                    len(todos)
                    )
                )

        for todo_done in todos_done:
            print("\t {}".format(todo_done.get("title")))
