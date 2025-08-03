# Sure! Let's go through loops in Python in detail, covering all types of loops: for, while, nested loops, loop control statements, and some examples.

# 🔁 What is a Loop?
# A loop is used to repeat a block of code multiple times until a condition is met or over a sequence.

# ✅ Types of Loops in Python
# 1. for loop
# Used for iterating over a sequence (list, tuple, string, range, etc.)

# Syntax:

# python
# Copy
# Edit
# for variable in sequence:
#     # code block
# Example:
# python
# Copy
# Edit
# for i in range(5):
#     print(i)
# Output:

# Copy
# Edit
# 0
# 1
# 2
# 3
# 4
# 2. while loop
# Repeats a block as long as a condition is True.

# Syntax:

# python
# Copy
# Edit
# while condition:
#     # code block
# Example:
# python
# Copy
# Edit
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# Output:

# Copy
# Edit
# 1
# 2
# 3
# 4
# 5
# 💡 range() function (used with for)
# python
# Copy
# Edit
# range(start, stop, step)
# Examples:
# python
# Copy
# Edit
# for i in range(2, 10, 2):
#     print(i)
# Output:

# Copy
# Edit
# 2
# 4
# 6
# 8
# 🔄 Nested Loops
# Loops inside loops.

# Example:
# python
# Copy
# Edit
# for i in range(3):
#     for j in range(2):
#         print(f"i = {i}, j = {j}")
# 🔚 Loop Control Statements
# 1. break
# Terminates the loop immediately.

# python
# Copy
# Edit
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
# 2. continue
# Skips the current iteration, moves to the next.

# python
# Copy
# Edit
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)
# 3. pass
# A null statement — does nothing.

# python
# Copy
# Edit
# for i in range(5):
#     if i == 3:
#         pass  # Placeholder
#     print(i)
# 🔁 else with Loops
# Python supports an optional else clause with both for and while loops.

# It runs only if the loop did not exit via break.

# Example with for:
# python
# Copy
# Edit
# for i in range(5):
#     print(i)
# else:
#     print("Loop completed without break")
# Example with break:
# python
# Copy
# Edit
# for i in range(5):
#     if i == 3:
#         break
#     print(i)
# else:
#     print("Will not print this")
# 📌 Summary Table
# Type	Use Case	Terminates with break	Can use else	Typical Usage
# for	Fixed repetitions or sequences	Yes	Yes	Lists, strings, range
# while	Condition-based repetition	Yes	Yes	Input loops, conditions
# break	Stop loop early	-	-	Exit when condition met
# continue	Skip current iteration	-	-	Skip invalid input
# pass	Placeholder	-	-	Write code later

# 🧪 Practical Example: Sum of numbers from 1 to 100
# python
# Copy
# Edit
# total = 0
# for i in range(1, 101):
#     total += i
# print("Sum is:", total)