# Q 1. Create an integer variable `x` with the value `10` and print it.
x = 10
print(x)

# Q 2. Assign a decimal number to a variable `y` and print it.
y = 12.5
print(y)

# Q 3. Store your name in a variable `name` and print it.
name = "Antara"
print(name)

# Q 4. Create a boolean variable `is_python_easy` with the value `True` and print it.
is_python_easy = True
print(is_python_easy)

# Q 5. Define a list `colors` with values "red", "green", "blue" and print the list.
colors = ["red", "green", "blue"]
print(colors)

# Q 6. Create a tuple `numbers` with values (1, 2, 3) and print it.
numbers = (1, 2, 3)
print(numbers)

# Q 7. Define a dictionary `person` with keys "name" and "age", assign values, and print it.
person = {"name": "Antara", "age": 28}
print(person)

# Q 8. Create a set `fruits` with values "apple", "banana", "cherry" and print it.
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Q 9. Use the type() function to check the data type of 10 and print the result.
print(type(10))

# 10. Convert the integer `10` into a string and print the new value.
num_str = str(10)
print(num_str)

# Q 1. Write a function `greet()` that prints `"Hello, Welcome to Python!"` when called.

def greet():
    print("Hello, Welcome to Python!")

greet()

# Q 2. Create a function `add(a, b)` that takes two numbers as parameters and returns their sum.

def add(a, b):
    return a + b

print(add(19, 27))

# Q 3. Define a function `square(n)` that returns the square of a given number.
def square(n):
    return n * n

print(square(7))

# Q 4. Write a function `is_even(n)` that returns `True` if a number is even, otherwise `False`.
def is_even(n):
    return n % 2 == 0

print(is_even(10))  # True
print(is_even(7))   # False

# Q 5. Create a function `greet_user(name="Guest")` that prints `"Hello, [name]!"`, using `"Guest"` as the default value.
def greet_user(name="Guest"):
    print(f"Hello, {name}!")

greet_user()
greet_user("Antara")

# Q 6. Implement a function `multiply(a, b=2)` that multiplies two numbers but has a default value of `2` for `b`.
def multiply(a, b=2):
    return a * b

print(multiply(5))
print(multiply(5, 4))

# Q 7. Write a function `factorial(n)` that calculates the factorial of a given number using a loop.
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print(factorial(5))

# Q 8. Create a function `count_vowels(text)` that returns the number of vowels in a given string.
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

print(count_vowels("Python Programming"))

# Q 9. Define a function `reverse_string(text)` that returns the reversed version of a given string.
def reverse_string(text):
    return text[::-1]

print(reverse_string("Python"))

# Q 10. Write a function `is_palindrome(text)` that checks if a string is a palindrome (same forward and backward).
def is_palindrome(text):
    return text == text[::-1]

print(is_palindrome("madam"))
print(is_palindrome("python"))

# Q 1. Write a lambda function to add two numbers and print the result.
add = lambda a, b: a + b
print(add(5, 3))

# Q 2. Create a lambda function to find the square of a given number.
square = lambda x: x * x
print(square(6))

# Q 3. Write a lambda function to check if a number is even or odd.
even_odd = lambda n: "Even" if n % 2 == 0 else "Odd"
print(even_odd(7))

# Q 4. Define a lambda function that returns the larger of two numbers.
larger = lambda a, b: a if a > b else b
print(larger(10, 20))

# Q 5. Use a lambda function to concatenate two strings with a space in between.
concat = lambda a, b: a + " " + b
print(concat("Hello", "Python"))

# Q 6. Create a lambda function that takes a number and returns "Positive" if > 0, otherwise "Negative".
check_num = lambda n: "Positive" if n > 0 else "Negative"
print(check_num(-5))

# Q 7. Use a lambda function inside map() to double all numbers in a list [1, 2, 3, 4, 5].
numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

# Q 8. Use a lambda function inside filter() to get only even numbers from a list [10, 15, 20, 25, 30].
nums = [10, 15, 20, 25, 30]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# Q 9. Write a lambda function inside sorted() to sort a list of tuples based on the second value: [(1, 5), (2, 3), (4, 1)].
data = [(1, 5), (2, 3), (4, 1)]
sorted_list = sorted(data, key=lambda x: x[1])
print(sorted_list)

# Q 10. Create a lambda function that returns the length of a given string.
length = lambda s: len(s)
print(length("Python"))