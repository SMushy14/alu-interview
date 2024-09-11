#!/usr/bin/python3
"""

This method that calculates the fewest number of operations needed to result in exactly n H characters in the file.

Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
"""
import math

def minOperations(n):

if n <= 1:

    return 0

operations = 0

current = 1

factor = 2

while current < n:

    # If the current number is divisible by the factor

    if n % factor == 0:

        # Perform the Copy All and Paste operations

        while n % factor == 0:

            operations += factor

            n /= float(factor)

    if factor > 1:

    factor += 1



current += 1


return operations

