#!/usr/bin/python3
"""
This module contains a function that returns a list of lists of integers 
representing the Pascal’s triangle of n.
"""


def pascal_triangle(n):
    """
    Function that returns a list of lists of integers representing the
    Pascal’s triangle of n.

    Args:
        n (int): The number of rows in Pascal's triangle.

    Returns:
        List[List[int]]: A list of lists of integers representing Pascal's
        triangle up to n rows.
    """
    if n <= 0:
        return []
    
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[i - 1]
        row.extend([sum(pair) for pair in zip(last_row, last_row[1:])])
        row.append(1)
        triangle.append(row)
    
    return triangle
