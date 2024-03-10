#!/usr/bin/python3
"""
This module contains function
which creates Pascal triangle
Author: Nafeesah
"""


def pascal_triangle(n):
    """creates pascal triangle"""
    resList= []
    if n <= 0:
        return resList
    for i in range(n):
        temp = []
        for j in range(n + 1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                temp.append(resList[i][j] + resList[i][j - 1])
        resList.append(temp)
    return resList