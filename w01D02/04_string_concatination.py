"""String Concatenation."""

name = "Sravan"
location = "Bengaluru"

print(name + " lives in " + location)

age = 80

# The below line Throws an Error: TypeError:
# can only concatenate str (not "int") to str
# print(name + " is an " + age + " year oldman.")
print(name + " is an " + str(age) + " year oldman.")
