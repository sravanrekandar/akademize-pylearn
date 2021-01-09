"""Factorial."""


def print_factorial(n):
    """Print factorial."""
    fact = 1
    for i in range(2, n+1):
        fact = fact * i

    print(f"{n}! = {fact}")


def main():
    """Print factorials."""
    print_factorial(3)
    print_factorial(5)
    print_factorial(6)


main()


"""
Finding the factorial of 5

fact = 1

Iteration 1
-----------
fact = fact * 2 (1 * 2)
fact = 2

Iteration 2
-----------
fact = fact * 3 (2 * 3)
fact = 6

Iteration 3
-----------
fact = fact * 4 (6 * 4)
fact = 24

Iteration 4
-----------
fact = fact * 5 (24 * 5)
fact = 120


"""
