"""25_print_group_of_statements_100_times.py."""


def print_group_of_statements(group_number):
    """Print Group of Statements."""
    print(f"-----{group_number}-----")
    print("I am Super Man")
    print("I am Bat man")
    print("I am the God\n")


def main():
    """Start the logic here."""
    for i in range(100):
        print_group_of_statements(i + 1)


main()
