#!/usr/bin/python3
"""
A Python script that, using a given REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import csv
import requests
import sys


def get_employee_todo_progress(employee_id):
    """ Fetches and prints the TODO list progress of a given employee. """
    base_url = 'https://jsonplaceholder.typicode.com/'
    user_url = base_url + 'users/' + str(employee_id)
    todo_url = base_url + 'todos?userId=' + str(employee_id)

    try:
        user = requests.get(user_url).json()
        user_todos = requests.get(todo_url).json()

        user_id = user.get('id')
        with open('{}.csv'.format(user_id), 'w', encoding='utf-8') as f:
            username = user.get('username')
            writer = csv.writer(f, quoting=csv.QUOTE_ALL)
            for todo in user_todos:
                status = todo.get('completed')
                title = todo.get('title')
                data = [user_id, username, status, title]
                writer.writerow(data)

    except Exception as e:
        print("Error:", e)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
