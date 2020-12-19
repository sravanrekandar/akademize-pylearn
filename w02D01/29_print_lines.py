"""Print Lines."""


def print_line(n):
    """Print line with n characters."""
    for i in range(n):
        print("-", end="")

    # By default a \n is included at the end of the line
    print()


def main():
    """Print lines."""
    for i in range(10):
        print_line(i+1)


main()
