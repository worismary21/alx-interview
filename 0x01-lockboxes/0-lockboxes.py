#!/usr/bin/python3

def canUnlockAll(boxes):
    # Start with the first box unlocked (box 0)
    unlocked_boxes = set([0])
    keys = set(boxes[0])  # Get the keys from the first box

    # Iterate over the keys until no new keys are found
    while keys:
        new_key = keys.pop()  # Get a key
        if new_key < len(boxes) and new_key not in unlocked_boxes:  # Check if it's a valid box
            unlocked_boxes.add(new_key)  # Mark the box as unlocked
            keys.update(boxes[new_key])  # Add new keys found in the newly unlocked box

    # If all boxes are unlocked, the size of unlocked_boxes will be equal to the total number of boxes
    return len(unlocked_boxes) == len(boxes)
