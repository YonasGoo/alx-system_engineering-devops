#!/usr/bin/python3

"""
This script exports user's todo data to a JSON file.
Usage: python script.py USER_ID
"""

import json
from requests import get
from sys import argv


def jsonWrite(user):
    """Writes user's todo data to JSON."""
    
    # Fetch todo data
    data = get(f'https://jsonplaceholder.typicode.com/todos?userId={user}').json()
    
    # Fetch username
    name = get(f'https://jsonplaceholder.typicode.com/users/{user}').json().get('username')
    
    # Prepare ordered data
    ordered = []
    for line in data:
        ordered.append({"task": line.get('title'), "completed": line.get('completed'), "username": name})
    
    # Write to JSON file
    with open(f'{user}.json', 'w') as f:
        json.dump({user: ordered}, f)


if __name__ == "__main__":
    # Run the function with user ID provided as command-line argument
    jsonWrite(int(argv[1]))
