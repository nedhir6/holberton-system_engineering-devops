#!/usr/bin/python3
"""Gather data from an API """
import csv
import requests
from sys import argv

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
    for scope in user:
        name = scope.get("username")
        id = scope.get("id")
    file = argv[1] + ".csv"
    with open(file, mode='w') as file1:
        delm = csv.writer(file1, delimiter=',', quoting=csv.QUOTE_ALL)
        for tasks in todolist:
            donetasks = tasks.get("completed")
            tasktitle = tasks.get("title")
            delm.writerow([id, name, donetasks, tasktitle])
