"""Factorial."""


def print_factorial(n):
    """Print factorial."""
    fact = 1
    """
        Iterating backwards
        start n
        stop 1
        step by -1
    """
    for i in range(n, 0, -1):
        fact = fact * i

    print(f"{n}! = {fact}")


def main():
    """Print factorials."""
    print_factorial(3)
    print_factorial(5)
    print_factorial(6)


main()
