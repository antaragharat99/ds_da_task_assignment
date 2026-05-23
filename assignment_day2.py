# Q1: Basic Output: Write a program that prints:
print("Hello, World!")

# Q2: Printing a Number: Write a Python program that prints the number 10.
print(10)

# Q3: Using Variables: Store your name in a variable and print:
name = "Antara"
print("My name is", name)

# Q4: Printing Multiple Values: Use a single print() statement to display:
print("Python is fun!")

# Q5: Using sep: Print three words with a '-' between them.
print("Python", "is", "fun", sep="-")

# Q6: Using end: Print two sentences using two print() statements, but make sure they appear on the same line.
print("Hello", end=" ")
print("World")

# Q7: Concatenation: Print a sentence by combining strings using +.
print("Python " + "is " + "awesome!")

# Q8: Printing a Calculation: Write a program that prints the sum of two numbers.
a = 10
b = 5
print("Sum =", a + b)

# Q9: Using f-strings: Print your name and age in the following format:
name = "Antara"
age = 30
print(f"My name is {name} and I am {age} years old.")

# Q10: Fun Fact: Print an interesting fact about Python using the print() function.
print("Python is named after Monty Python, not the snake!")

# Q1: Write a Python program that adds two numbers using the + operator and prints the result.
a = 10
b = 5
print(a + b)

# Q2: Create a program that takes two numbers and finds their remainder using the % operator.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a % b)

# Q3: Use a comparison operator to check if 10 is greater than 5 and print the result.
print(10 > 5)

# Q4: Write a program that checks if two variables have the same value using the == operator.
a = 10
b = 10
if a == b:
    print("Both values are equal")

# Q5: Implement a program that uses the and logical operator to check if both conditions
if 10 > 5 and 20 > 15:
    print("Both conditions are True")

# Q6: Use an assignment operator to increase the value of x = 10 by 5 using +=.
x = 10
x += 5
print(x)

# Q7: Write a program that checks if a number is not greater than 100 using the not operator.
num = int(input("Enter a number: "))
if not (num > 100):
    print("Number is not greater than 100")

# Q8: Use range() and the * multiplication operator to print the first 10 multiples of 5.
for i in range(1, 11):
    print(i * 5)

# Q9: Create a program that asks the user for two numbers and finds their quotient using the / operator.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print(a / b)

# Q10: Implement a program that swaps two numbers using a mathematical operator
a = 10
b = 5
a = a + b
b = a - b
a = a - b
print("a =", a)
print("b =", b)

# Q1: Write a program that checks if a number is positive. If it is, print "Positive Number".
num = int(input("Enter a number: "))
if num > 0:
    print("Positive Number")

# Q2: Create an if-else statement that checks if a person is eligible to vote (age ≥ 18).
age = int(input("Enter your age: "))
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# Q3: Write an if-elif-else condition to categorize a number as positive, negative, or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Q4: Create a program that checks if a number is even or odd using if-else.
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Q5: Use a nested if condition to check if a number is positive and even.
num = int(input("Enter a number: "))
if num > 0:
    if num % 2 == 0:
        print("Positive and Even")

# Q6: Write a one-line if condition to print "Python is cool" if x = 10.
x = 10
if x == 10: print("Python is cool")

# Q7: Implement a one-line if-else condition to print "Even" if a number is even, otherwise "Odd".
num = int(input("Enter a number: "))
print("Even" if num % 2 == 0 else "Odd")

# Q8: Write an if statement that checks if a given string contains the word "Python".
text = input("Enter a string: ")
if "Python" in text:
    print("Python found")

# Q9: Check whether a number is divisible by both 3 and 5 using if-else.
num = int(input("Enter a number: "))
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both 3 and 5")
else:
    print("Not divisible by both 3 and 5")

# Q10: Write an if condition that checks whether a year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")