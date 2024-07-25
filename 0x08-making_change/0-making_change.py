#!/usr/bin/python3
'''given a pile of coins of diff values,
det the fewest no of coins needed to meet a given amount.
'''


def makeChange(coins, total):
    '''function to solve above question.
    args:
        coins: list of the values of coins in ur possesion.
        total: the amount to be met by the coins
    Returns:
        fewest no of coins needed to meet total
        if total is <= 0 return 0
        elif total cannot be meet by the no of coins you have return -1
    '''
    if total <= 0:
        return 0

    if (coins == 0):
        return -1

    ans = 0  # the number of coins needed
    my_coins = sorted(coins,  reverse=True)  # in decreasing order
    rem = total  # money we are left with after subtracting a coin

    for coin in my_coins:
        if rem == 0:
            break
        if coin <= rem:
            ans += rem // coin
            rem %= coin

    ans = ans if rem == 0 else -1

    return ans
