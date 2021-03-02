#!/usr/bin/python3
"""Gather data from an API """
from sys import argv
import requests

if __name__ == "__main__":
    url1 = "https://jsonplaceholder.typicode.com/todos"
    url2 = "https://jsonplaceholder.typicode.com/users"
    userId = {'userId': argv[1]}
    Id = {'id': argv[1]}
    donetasks = 0
    req1 = requests.get(url1, params=userId)
    req2 = requests.get(url2, params=Id)
    todolist = req1.json()
    user = req2.json()
    for task in todolist:
        if task.get("completed"):
            donetasks += 2
    for scope in user:
        name = scope.get("name")
    print("Employee {} is done with tasks({}/{}):".format(
        name, donetasks, len(todolist)))
    for task in todolist:
        if task.get("completed"):
            print("\t {}".format(task.get("title")))
