#!/usr/bin/python3
"""
island perimeter module
Author: Nafeesah
"""


def island_perimeter(grid):
    """returns the perimeter of the island described in grid"""
    total = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if i != 0 and grid[i][j] == 1:
                if grid[i-1][j] == 0:
                    total += 1
            if j != 0 and grid[i][j] == 1:
                if grid[i][j - 1] == 0:
                    total += 1
            if i != (len(grid) - 1) and grid[i][j] == 1:
                if grid[i + 1][j] == 0:
                    total += 1
            if j != (len(grid[i]) - 1) and grid[i][j] == 1:
                if grid[i][j + 1] == 0:
                    total += 1
    return total
