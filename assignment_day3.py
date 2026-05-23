#Q.1 Write a `for` loop to print numbers from `1` to `5`.
for i in range(1, 6):
    print(i)

# Q.2 Use a `for` loop to iterate over the list `fruits = ["apple", "banana", "cherry"]` and print each item.
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# Q.3 Create a `for` loop that prints numbers from `2` to `10` with a step of `2` using `range()`.
for i in range(2, 11, 2):
    print(i)

# Q.4 Write a `for` loop to print each character of the string `"Python"`.
for char in "Python":
    print(char)

# Q.5 Use a `for` loop to calculate and print the sum of numbers in the list `[10, 20, 30, 40]`.
numbers = [10, 20, 30, 40]
total = 0

for num in numbers:
    total += num

print("Sum:", total)

# Q.6 Write a `for` loop that stops execution when it encounters the number `5` using `break`.
for i in range(1, 10):
    if i == 5:
        break
    print(i)

# Q.7 Create a `for` loop that skips printing the number `3` using `continue`.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# Q.8 Write a nested `for` loop to print a multiplication table for numbers `1` to `3`.
for i in range(1, 4):
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()  # blank line between tables

# Q.9 Use a `for` loop to iterate through a dictionary `{ "name": "Dhiraj", "age": 25 }` and print its keys and values.
person = {"name": "Dhiraj", "age": 25}

for key, value in person.items():
    print(key, ":", value)

# Q.10 Create a `for` loop with an `else` statement that prints `"Loop completed"` when the loop finishes normally.
for i in range(1, 6):
    print(i)
else:
    print("Loop completed")