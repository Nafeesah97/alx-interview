#!/usr/bin/python3
"""making changes"""


def changedynamic(coins, total, dp):
    """To dynmically find the lowest combination"""
    dp[0] = 0
    if (total <= 0):
        return 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[total] if dp[total] != float('inf') else -1


def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet
    a given amount total
    """
    dp = [float('inf')] * (total + 1)
    sorted_coins = sorted(coins, reverse=True)
    return changedynamic(sorted_coins, total, dp)
