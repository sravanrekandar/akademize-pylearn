"""Function example."""


def print_age_group(age):
    """Print Age group for a given age."""
    if age < 5:
        print(f"Age = {age}, Age Group = Infant")
    else:
        if age < 12:
            print(f"Age = {age}, Age Group = Toddler")


# Start executing...
print_age_group(3)
print_age_group(7)


"""
Functions in python

Defining a function:


def print_age_group(age):
--- --------------- ---
 1    2              3


 1. def : A keyword (reserved identifier): full form: Define
 2. print_age_group: Name of the function.
 3. Argument, a variable named 'age'


Invoking a function:

print_age_group(3)


"""
