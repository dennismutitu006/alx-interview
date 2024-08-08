#!/usr/bin/python3
'''Sieve of Eratosthenes.'''


def sieve(n):
    '''the function whose algorithmn will det the prime numbers'''
    primes = [True] * (n+1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n + 1, p):
                primes[i] = False
        p += 1
        primes[0], primes[1] = False, False
        return primes


def isWinner(x, nums):
    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    primes = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = sum(primes[2:n+1])
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
