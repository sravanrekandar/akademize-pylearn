"""25_print_groups_of_statements."""


def print_characters_from_DC(group_number):
    """Print DC Character Names."""
    print(f"-----{group_number}-----")
    print("Wonder Woman")
    print("Bat man")
    print("Aqua man")


def print_characters_from_Marvel(group_number):
    """Print Marvel Characters."""
    print(f"-----{group_number}-----")
    print("Capten Marvel")
    print("Thanos")
    print("Iron Man")


def main():
    """Print character names multiple times from different universes."""
    for i in range(100):
        print_characters_from_DC(i + 1)
    for i in range(100):
        print_characters_from_Marvel(i + 1)


main()
