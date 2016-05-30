def gcd(a, b):
    """
    returns largest integer which divides both a and b 

    >>> gcd(4, 6)
    2

    >>> gcd(128, 32)
    32
    """

    while b:
        a, b = b, a%b
    return a


def extended_euclid(a, b):
    """
    returns a tuple (g, x, y) where

    g is gcd of a and b and g = ax + by

    >>> extended_euclid(116127, 15433)
    (253, 21, -158)
    """
    xx, y, yy, x = 0, 0, 1, 1
    while b:
        q = a//b
        a, b = b, a%b
        xx, x = x-q*xx, xx
        yy, y = y-q*yy, yy
    return (a, x, y)


def modular_linear_solver(a, b, n):
    """
    returns solution to congruence ax = b ( mod n )

    >>> modular_linear_solver(13, 5, 7)
    [2]

    >>> modular_linear_solver(82, 30, 62)
    [17, 48]
    """
    solutions = []
    d, x, y = extended_euclid(a, n)
    if b % d == 0 :
        x = (x*(b//d)) % n
        for i in range (d):
            solutions.append( (x + i*(n//d) ) % n )
    return sorted(solutions)
