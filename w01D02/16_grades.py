"""Grades."""

# Max marks is 100 in each subject
# Pass mark is 35
marks_1 = int(input("Marks 1: "))
marks_2 = int(input("Marks 2: "))
marks_3 = int(input("Marks 3: "))

total = marks_1 + marks_2 + marks_3
avg = total / (3 * 100)
percent = avg * 100
is_passed = True

if marks_1 < 35:
    is_passed = False
if marks_2 < 35:
    is_passed = False
if marks_3 < 35:
    is_passed = False

print("Report")
print("Total = " + str(total))
print("Percent = " + str(percent))

if is_passed:
    print("Passed")
else:
    print("Failed")
