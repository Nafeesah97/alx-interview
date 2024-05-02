#!/usr/bin/python3
"""making changes"""

def changedynamic(coins, total, n, dp):
    """To dynmically find the lowest combination"""
    dp[0] = 0
    if (total <= 0):
        return dp[0]
    
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], 1 + dp[i - coin])
    return dp[total] if dp[total] != -12 else -1

def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet
    a given amount total
    """
    n = len(coins)
    dp = [-12 for i in range(total + 1)]
    return changedynamic(coins, total, n, dp)
