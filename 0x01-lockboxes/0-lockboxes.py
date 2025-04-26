#!/usr/bin/python3
"""
0-lockboxes.py
Determines if all boxes can be opened given keys within boxes.
"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be unlocked
    :param boxes: List of lists representing boxes and their keys
    :return: True if all boxes can be opened, False otherwise
    """
    if not boxes or not isinstance(boxes, list):
        return False

    unlocked = set([0])  # Start with box 0
    keys = [0]  # Stack for DFS

    while keys:
        current = keys.pop()
        for key in boxes[current]:
            if 0 <= key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                keys.append(key)

    return len(unlocked) == len(boxes)
