"""43_sum_of_first_n_numbers.py."""


def print_sum(n):
    """Print sum of Natural numbers for given n."""
    sum = 0
    s = ""  # Declaring a string variable and assigning it with empty string
    for i in range(1, n+1):
        sum = sum + i
        s = s + str(i)
        if i != n:  # Add a + sign if this is not the last iteration
            s = s + " + "

    print(f"{s} = {sum}")
    # print(f"\nSum of first {n} Natural numbers is {sum}")


def main():
    """Print sum of Natural numbers for given limits."""
    print_sum(5)
    print_sum(10)


main()
