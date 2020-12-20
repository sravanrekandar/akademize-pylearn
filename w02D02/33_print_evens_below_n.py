"""Print Evens below n."""


def print_evens(n):
    """Print evens below n."""
    print(f"Printing Evens below {n}")
    print("-------------------")
    for i in range(0, n):  # n iterations
        if i % 2 == 0:
            print(i)


def main():
    """Print evens."""
    print_evens(10)
    print_evens(20)


main()
