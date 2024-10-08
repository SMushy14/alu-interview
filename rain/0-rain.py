#!/usr/bin/python3
"""
This module contains a function that calculates the amount of rainwater
trapped between walls after rainfall.

The rain() function takes in a list of wall heights and determines the
total volume of water that can be trapped between the walls.
"""


def rain(walls):
    """
    Calculate total amount of rainwater trapped between walls after rainfall.

    Given a list of non-negative integers where each integer represents
    the height of a wall with unit width 1, this function calculates
    how many square units of water can be trapped between the walls.

    Parameters:
    walls (list of int): A list of non-negative integers representing wall
    heights.

    Returns:
    int: The total amount of rainwater trapped in square units.

    Example:
    >>> rain([2, 0, 0, 4, 0, 0, 1, 0])
    6
    """

    # If there are no walls, no water can be trapped
    if not walls:
        return 0

    # Initialize pointers to the beginning (left) and end (right) of the walls
    # list
    left = 0
    right = len(walls) - 1

    # These variables track the highest walls we've seen so far from the left
    # and right
    left_max = 0
    right_max = 0

    # This will hold the total amount of water trapped
    water_trapped = 0

    # Loop until the left pointer meets the right pointer
    while left < right:
        # Compare the height of the left and right walls
        if walls[left] < walls[right]:
            # If the current left wall is taller than the highest so far,
            # update left_max
            if walls[left] >= left_max:
                left_max = walls[left]
            # Otherwise, we can trap water at this position
            else:
                water_trapped += left_max - walls[left]
            # Move the left pointer to the right
            left += 1
        else:
            # If the current right wall is taller than the highest so far,
            # update right_max
            if walls[right] >= right_max:
                right_max = walls[right]
            # Otherwise, we can trap water at this position
            else:
                water_trapped += right_max - walls[right]
            # Move the right pointer to the left
            right -= 1

    # Return the total amount of water trapped
    return water_trapped
