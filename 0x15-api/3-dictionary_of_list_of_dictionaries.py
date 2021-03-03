#!/usr/bin/python3
"""Gather data from an API """
import json
import requests
from sys import argv

if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"
    req1 = requests.get(url1)
    req2 = requests.get(url2)
    todolist = req1.json()
    user = req2.json()
    dict = {}
    file = "todo_all_employees.json"
    with open(file, mode='w') as file1:
        for scope in user:
            name = scope.get("username")
            id = scope.get("id")
            dict[id] = []
            for tasks in todolist:
                if id == tasks["userId"]:
                    content = {}
                    content = {"username": name, "task": tasks.get("title"),
                               "completed": tasks.get("completed")}
                    dict[id].append(content)
        json.dump(dict, file1)
