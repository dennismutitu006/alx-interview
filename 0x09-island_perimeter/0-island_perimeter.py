#!/usr/bin/python3
"""
function to calculate the perimeter of a grid.
"""


def island_perimeter(grid):
    """Calcs the perimeter

    Args:
        grid (list of list of int): 2D grid where 0 reps water and 1 land.

    Returns:
        int: perimeter of the island
    """

    perimeter = 0
    r = len(grid)
    c = len(grid[0])

    for i in range(r):
        for j in range(c):
            if grid[i][j] == 1:
                for x, y in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
                    α, β = i + x, j + y
                    # print(α, β)
                    if α >= r or β >= c or α < 0 or β < 0 or grid[α][β] == 0:
                        perimeter += 1

    return perimeter
