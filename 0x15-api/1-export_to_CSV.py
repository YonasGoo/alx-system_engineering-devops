#!/usr/bin/python3

"""
This script exports user's todo data to a CSV file.
Usage: python script.py USER_ID
"""

import csv
import requests
from sys import argv


def export_to_csv(user_id):
    """Export user's todo data to CSV."""

    try:
        todo_data = requests.get(
                f'https://jsonplaceholder.typicode.com/todos?userId={user_id}').json()
        username = requests.get(
                f'https://jsonplaceholder.typicode.com/users/{user_id}').json().get('username')

        with open(f'{user_id}.csv', 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
            for task in todo_data:
                row = [task.get('userId'), username, task.get('completed'), task.get('title')]
                csv_writer.writerow(row)

        print(f"Data exported to: {user_id}.csv")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    if len(argv) == 2:
        export_to_csv(argv[1])
    else:
        print("Usage: python script.py USER_ID")
