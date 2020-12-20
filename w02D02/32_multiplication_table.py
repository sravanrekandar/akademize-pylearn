"""Print a multiplication table."""


def print_table(n):
    """Print nth table."""
    print(f"Table {n}\n----------")
    for i in range(1, 11):
        print(f"{n} * {i} = {n*i}")
    print("\n\n")


def main():
    """Print multiplication tables."""
    print_table(2)
    print_table(5)
    print_table(10)


main()
