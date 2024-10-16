#!/usr/bin/python3


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in exactly n 'H' characters.
    
    Parameters:
    n (int): The desired number of 'H' characters.
    
    Returns:
    int: The minimum number of operations needed, or 0 if impossible.
    """
    if n <= 1:
        return 0  # No operations needed if n is 1 or less
    
    operations = 0
    # Start with the current count of 'H' being 1
    current = 1
    
    # Loop through potential factors from 2 to n
    for i in range(2, n + 1):
        while n % i == 0:  
            operations += i  
            n //= i  
            
    return operations


