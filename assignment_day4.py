#1. Write a for loop to print numbers from 1 to 5.
for i in range(1, 6):
    print(i)

#2. Use a for loop to iterate over the list fruits = ["apple", "banana", "cherry"] and print each item.
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

#3. Create a for loop that prints numbers from 2 to 10 with a step of 2 using range().
for i in range(2, 11, 2):
    print(i)

#4. Write a for loop to print each character of the string "Python".
for ch in "Python":
    print(ch)

#5. Use a for loop to calculate and print the sum of numbers in the list [10, 20, 30, 40].
numbers = [10, 20, 30, 40]
total = 0
for num in numbers:
    total += num
print(total)

#6. Write a for loop that stops execution when it encounters the number 5 using break.
for i in range(1, 10):
    if i == 5:
        break
    print(i)

#7. Create a for loop that skips printing the number 3 using continue.
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

#8. Write a nested for loop to print a multiplication table for numbers 1 to 3.
for i in range(1, 4):
    for j in range(1, 4):
        print(i, "x", j, "=", i * j)
    print()

#9. Use a for loop to iterate through a dictionary { "name": "Dhiraj", "age": 25 } and print its keys and values.
info = {"name": "Dhiraj", "age": 25}
for key, value in info.items():
    print(key, "=", value)

#10. Create a for loop with an else statement that prints "Loop completed" when the loop finishes normally.
for i in range(3):
    print(i)
else:
    print("Loop completed")

#11. Write a program that checks if a number is positive. If it is, print "Positive Number".
num = 10
if num > 0:
    print("Positive Number")

#12. Create an if-else statement that checks if a person is eligible to vote (age ≥ 18).
age = 18
if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

#13. Write an if-elif-else condition to categorize a number as positive, negative, or zero.
n = 0
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")

#14. Create a program that checks if a number is even or odd using if-else.
num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

#15. Use a nested if condition to check if a number is positive and even.
num = 8
if num > 0:
    if num % 2 == 0:
        print("Positive and Even")

#16. Write a one-line if condition to print "Python is cool" if x = 10.
x = 10
if x == 10: print("Python is cool")

#17. Implement a one-line if-else condition to print "Even" if a number is even, otherwise "Odd".
num = 4
print("Even") if num % 2 == 0 else print("Odd")

#18. Write an if statement that checks if a given string contains the word "Python".
text = "I love Python programming"
if "Python" in text:
    print("Python found")

#19. Check whether a number is divisible by both 3 and 5 using if-else.
num = 15
if num % 3 == 0 and num % 5 == 0:
    print("Divisible by both")
else:
    print("Not divisible by both")

#20. Write an if condition that checks whether a year is a leap year (divisible by 4 but not 100 unless divisible by 400).
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#21. Write a program that asks for the user’s name and prints: Hello, [name]!
name = input("Enter your name: ")
print(f"Hello, {name}!")

#22. Ask the user for their age and print: You are [age] years old.
age = input("Enter your age: ")
print(f"You are {age} years old.")

#23. Ask the user for their favorite color and print: Your favorite color is [color].
color = input("Enter your favorite color: ")
print(f"Your favorite color is {color}.")

#24. Ask the user for two numbers, add them, and print the sum.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum =", a + b)

#25. Ask the user for their first and last name separately and print: Hello, [first name] [last name]!
first = input("Enter first name: ")
last = input("Enter last name: ")
print(f"Hello, {first} {last}!")

#26. Ask the user to enter a number, then print its double.
num = int(input("Enter a number: "))
print(num * 2)

#27. Ask the user what their favorite food is and print a sentence using their input.
food = input("What is your favorite food? ")
print(f"That sounds like a fun food: {food}!")

#28. Ask the user if they like Python. Print a response based on their answer.
ans = input("Do you like Python? (yes/no): ")
if ans.lower() == "yes":
    print("Great! Python is awesome.")
else:
    print("Give it time, you’ll like it!")

#29. Ask for the user’s city and country, then print: You live in [city], [country].
city = input("Enter your city: ")
country = input("Enter your country: ")
print(f"You live in {city}, {country}.")

#30. Ask the user about their hobby and print: That sounds like a fun hobby: [hobby]!
hobby = input("What is your hobby? ")
print(f"That sounds like a fun hobby: {hobby}!")

#31. Basic Output: Write a program that prints: Hello, World!
print("Hello, World!")

#32. Printing a Number: Write a Python program that prints the number 10.
print(10)

#33. Using Variables: Store your name in a variable and print: My name is [your_name].
name = "Antara"
print("My name is", name)

#34. Printing Multiple Values: Use a single print statement to display: Python is fun!
print("Python is fun!")

#35. Using sep: Print three words with a '-' between them.
print("apple", "banana", "cherry", sep="-")

#36. Using end: Print two sentences using two print statements, but make sure they appear on the same line.
print("Hello", end=" ")
print("World")

#37. Concatenation: Print a sentence by combining strings using +.
print("Python " + "is " + "awesome!")

#38. Printing a Calculation: Write a program that prints the sum of two numbers.
print(5 + 7)

#39. Using f-strings: Print your name and age in the format: My name is [name] and I am [age] years old.
name = "Antara"
age = 30
print(f"My name is {name} and I am {age} years old.")

#40. Fun Fact: Print an interesting fact about Python using the print() function.
print("Python was named after the British comedy show 'Monty Python'.")