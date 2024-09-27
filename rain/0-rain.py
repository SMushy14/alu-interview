#!/usr/bin/python3

def rain(walls):
    """
    Given a list of non-negative integers representing the heights of walls with unit width 1, 
    as if viewing the cross-section of a relief map, calculate how many square units of water will be retained after it rains.

    Prototype: def rain(walls)
    walls is a list of non-negative integers.
    Return: Integer indicating total amount of rainwater retained.
    Assume that the ends of the list (before index 0 and after index walls[-1]) are not walls, meaning they will not retain water.
    If the list is empty return 0

    """

    # If there are no walls, no water can be trapped
    if not walls:
        return 0

    # Initialize pointers to the beginning (left) and end (right) of the walls list
    left = 0
    right = len(walls) - 1

    # These variables track the highest walls we've seen so far from the left and right
    left_max = 0
    right_max = 0

    # This will hold the total amount of water trapped
    water_trapped = 0

    # Loop until the left pointer meets the right pointer
    while left < right:
        # Compare the height of the left and right walls
        if walls[left] < walls[right]:
            # If the current left wall is taller than the highest so far, update left_max
            if walls[left] >= left_max:
                left_max = walls[left]
            # Otherwise, we can trap water at this position
            else:
                water_trapped += left_max - walls[left]
            # Move the left pointer to the right
            left += 1
        else:
            # If the current right wall is taller than the highest so far, update right_max
            if walls[right] >= right_max:
                right_max = walls[right]
            # Otherwise, we can trap water at this position
            else:
                water_trapped += right_max - walls[right]
            # Move the right pointer to the left
            right -= 1

    # Return the total amount of water trapped
    return water_trapped

