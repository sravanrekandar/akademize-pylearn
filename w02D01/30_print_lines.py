"""Print Lines."""


def print_line(n, c):
    """Print line with n characters."""
    for i in range(n):
        print(c, end="")

    # By default a \n is included at the end of the line
    print()


def main():
    """Print lines."""
    for i in range(20):
        print_line(i+1, "*")


main()
