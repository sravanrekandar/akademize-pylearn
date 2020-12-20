"""Print Evens below n."""


def print_evens(n):
    """Print evens below n."""
    print(f"Printing Evens below {n}")
    print("-------------------")
    for i in range(0, n, 2):  # n/2 iterations
        print(i)

    """
    for i in range(0,    n,      2):
                ----,    --,     ---
                start    stop    step
    """


def main():
    """Print evens."""
    print_evens(10)
    print_evens(20)


main()
