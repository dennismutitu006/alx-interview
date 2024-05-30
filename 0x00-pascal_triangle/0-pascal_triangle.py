#!/usr/bin/python3
"""
Pascal's Triangle generator
This module def a fnctn for generation of pascals triangle based on the rows.
"""
def pascal_triangle(n):
    """
    Generates Pascal's triangle for a given positive integer n.

    Args:
        n (int): The number of rows in the triangle.

    Returns:
        List[List[int]]: A list of lists representing Pascal's triangle.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

if __name__ == "__main__":
    # Run the test cases using pytest
    pytest.main([__file__])
