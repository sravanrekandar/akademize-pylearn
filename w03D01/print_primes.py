"""Print Primes."""

from is_prime import is_prime

for i in range(2, 110):
    if is_prime(i):
        print(i)
