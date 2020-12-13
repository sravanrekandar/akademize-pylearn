"""Grades."""

MAX_MARKS_PER_SUBJECT = 100
PASS_MARK = 35
marks_1 = int(input("Marks 1: "))
marks_2 = int(input("Marks 2: "))
marks_3 = int(input("Marks 3: "))

total = marks_1 + marks_2 + marks_3
avg = total / (3 * MAX_MARKS_PER_SUBJECT)
percent = avg * 100

is_passed = False
if (
    (marks_1 >= PASS_MARK) and
    (marks_2 >= PASS_MARK) and
    (marks_3 >= PASS_MARK)
):
    is_passed = True

print("Report")
print("Total = " + str(total))
print("Percent = " + str(percent))

if is_passed:
    print("Passed")
else:
    print("Failed")

"""
Exercise:

- If Failed, give a report of which subject(s) is failing

- Give a Marks sheet

Explore: \n and \t
"""
