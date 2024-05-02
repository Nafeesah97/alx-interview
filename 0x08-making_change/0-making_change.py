#!/usr/bin/python3
"""making changes"""

def changedynamic(coins, total, n, dp):
    """To dynmically find the lowest combination"""
    if (total <= 0):
        return 0
    
    if n == 0:
        return float('inf')

    if (dp[n][total] != -1):
        return dp[n][total]
    
    if total < coins[n - 1]:
        dp[n][total] = changedynamic(coins, total, n - 1, dp)
    else:
        dp[n][total] = min(1 + changedynamic(coins, total - (coins[n - 1]), n, dp),
                       changedynamic(coins, total, n -1, dp))
    return dp[n][total]

def makeChange(coins, total):
    """
    determine the fewest number of coins needed to meet
    a given amount total
    """
    n = len(coins)
    dp = [[-1 for i in range(total + 1)] for j in range(n + 1)]
    return changedynamic(coins, total, n, dp)