#!/usr/bin/python3
"""Python script that, using this RE/her TODO list progress
"""
import csv
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
        user_name = user_request.get("username")

        with open("{}.csv".format(user_id), "w", encoding="utf-8") as f:
            for todo in todos:
                f.write(
                        '"{}","{}","{}","{}"\n'.format(
                            user_id,
                            user_name,
                            todo.get("completed"),
                            todo.get("title")
                            )
                        )
