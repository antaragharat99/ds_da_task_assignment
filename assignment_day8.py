# Question 1 : Write a for loop that prints numbers from 1 to 10 but stops when it reaches
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# Question 2 : Create a while loop that prints numbers starting from 1 and stops when the number is 7.
num = 1
while True:
    if num == 7:
        break
    print(num)
    num += 1

# Question 3 : A program where user enters numbers continuously, but the loop breaks when they enter 0.
while True:
    n = int(input("Enter a number (0 to stop): "))
    if n == 0:
        break
    print("You entered:", n)

# Question 4 : Use a for loop with break to stop printing even numbers when 8 is reached in [2, 4, 6, 8, 10].
evens = [2, 4, 6, 8, 10]
for n in evens:
    if n == 8:
        break
    print(n)

# Question 5 : Implement a while loop that generates random numbers (1–100) and stops when it generates 50.
import random

while True:
    num = random.randint(1, 100)
    print("Generated:", num)
    if num == 50:
        break

# Question 6 : Iterate over string "Python" but stop printing when "o" is found.
for ch in "Python":
    if ch == "o":
        break
    print(ch)

# Question 7 : Create a loop that iterates over a list of names but exits when it finds "John".
names = ["Amit", "Ravi", "John", "Sneha"]

for name in names:
    if name == "John":
        break
    print(name)

# Question 8 : Use a nested loop to print pairs (i, j) where i, j ∈ 1..3, but break inner loop when j == 2.
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break
        print((i, j))

# Question 9 : Guessing game — user keeps guessing until they enter the correct number.
secret = 7

while True:
    guess = int(input("Guess the number: "))
    if guess == secret:
        print("Correct!")
        break
    print("Wrong, try again!")

# Question 10 : Loop that reads file line by line and stops when keyword "STOP" is found.
with open("example.txt", "w") as f:
    f.write("Hello\nThis is a test file\nSTOP\nMore text")
with open("example.txt", "r") as file:
    for line in file:
        if "STOP" in line:
            break
        print(line.strip())

# Question 1 : Create a string variable text with "Hello, Python!" and print it.
text = "Hello, Python!"
print(text)

# Question 2 : Convert "python programming" to uppercase and print the result.
print("python programming".upper())

# Question 3 : Replace "Python" with "Java" in "I love Python" and print the result.
message = "I love Python"
print(message.replace("Python", "Java"))

# Question 4 : Find and print the length of "Python is fun!" using len().
print(len("Python is fun!"))

# Question 5 : Extract and print the first five characters of "Hello, World!" using slicing.
text = "Hello, World!"
print(text[:5])

# Question 6 : Use split() to turn "apple,banana,cherry" into a list.
items = "apple,banana,cherry".split(",")
print(items)

# Question 7 : Remove spaces from both ends of " Python " using strip().
text = "  Python  "
print(text.strip())

# Question 8 : Reverse the string "Python" using slicing.
print("Python"[::-1])

# Question 9 : Use join() to combine ["Hello", "Python"] into one string separated by a space.
words = ["Hello", "Python"]
print(" ".join(words))

# Question 10 : Format a string with f-strings: "My name is John and I am 25 years old."
name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")