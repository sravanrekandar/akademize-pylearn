"""25_print_group_of_statements_100_times.py."""


def print_statements(i):
    """Print Group of Statements."""
    print(f"-----{i+1}-----")
    print("I am Super Man")
    print("I am Bat man")
    print("I am the God\n")


for i in range(100):
    print_statements(i)
