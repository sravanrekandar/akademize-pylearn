"""43_sum_of_first_n_numbers.py."""


def print_sum(n):
    """Print sum of Natural numbers for given n."""
    sum = 0
    for i in range(n+1):
        sum = sum + i
    print(f"Sum of first {n} Natural numbers is {sum}")


def main():
    """Print sum of Natural numbers for given limits."""
    print_sum(5)
    print_sum(10)
    print_sum(20)


main()
