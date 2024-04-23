#!/usr/bin/python3

"""
This script exports todo data of all employees to a JSON file.
"""

import json
from requests import get

def jsonWrite():
    """Writes todo data of all employees to JSON."""

    # Fetch user data
    users_data = get('https://jsonplaceholder.typicode.com/users').json()

    # Prepare data for each user
    dumped = {}
    for user in users_data:
        user_id = user.get('id')
        username = user.get('username')

        # Fetch todo data for the user
        todo_data = get(f'https://jsonplaceholder.typicode.com/todos?userId={user_id}').json()

        # Prepare ordered data
        ordered = [{"task": line.get('title'), "completed": line.get('completed'), "username": username} for line in todo_data]
        
        # Store the data for the user
        dumped[user_id] = ordered
    
    # Write to JSON file
    with open('todo_all_employees.json', 'w') as f:
        json.dump(dumped, f)


if __name__ == "__main__":
    jsonWrite()
