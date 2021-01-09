"""Is Prime."""


def is_prime(n):
    """Is Prime.

    ----
    Args:
        n : An integer
    Returns
        Boolean (Prime or not)
    """

    if n == 0 or n == 1:
        return "Invalid number"
    if n == 2:
        return True
    for i in range(2, n):
        if n % i == 0:
            return False

    return True


if __name__ == "__main__":
    print("25 ", is_prime(25))
    print("121 ", is_prime(121))
    print("123 ", is_prime(123))
    print("127 ", is_prime(127))
    print("5 ", is_prime(5))
    print("0 ", is_prime(0))
    print("2 ", is_prime(2))
    print("4 ", is_prime(4))
    print("14 ", is_prime(14))
    print("144 ", is_prime(144))
    print("1445 ", is_prime(1445))
