"""Print Odds below n."""


def print_odds(n):
    """Print odds below n."""
    print(f"Printing Odds below {n}")
    print("-------------------")
    for i in range(1, n, 2):  # n/2 iterations
        print(i)


def main():
    """Print odds."""
    print_odds(10)
    print_odds(20)


main()
