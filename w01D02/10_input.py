"""Inputs."""

name = input("Enter your name: ")
age = int(input("Enter your age: "))

if age >= 18:
    print(f"{name} of {age} years old is eligible to vote")
else:
    print(f"{name} of {age} years old is not eligible to vote")
