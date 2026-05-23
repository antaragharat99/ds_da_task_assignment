# Question 1: Write a Python program that generates a list of squares from 1 to 10 using list comprehension.
squares = [x**2 for x in range(1, 11)]
print(squares)

# Question 2: Generate a list containing only the odd numbers from 1 to 20 using list comprehension.
odd_numbers = [x for x in range(1, 21) if x % 2 != 0]
print(odd_numbers)

# Question 3: Given a list of words, use list comprehension to create a new list where all words are in uppercase.
words = ["hello", "python", "world"]
uppercase_words = [w.upper() for w in words]
print(uppercase_words)

# Question 4: Write a program that generates a list of numbers from 1 to 30 that are divisible by 3 using list comprehension.
multiples_of_3 = [x for x in range(1, 31) if x % 3 == 0]
print(multiples_of_3)

# Question 5: Take a string input from the user and use list comprehension to create a list of vowels present in the string.
string = input("Enter a string: ")
vowels = [ch for ch in string if ch.lower() in "aeiou"]
print(vowels)

# Question 6: Given a list of words, create a new list using list comprehension where each word is reversed.
words = ["python", "hello", "world"]
reversed_words = [w[::-1] for w in words]
print(reversed_words)

# Question 7: Write a Python program that takes a sentence and uses list comprehension to replace every space with a hyphen (-).
sentence = "Python is fun to learn"
hyphen_sentence = ['-' if ch == ' ' else ch for ch in sentence]
print("".join(hyphen_sentence))

# Question 8: Given a list with duplicate values, use list comprehension to create a new list that contains only unique values.
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = []
[unique_numbers.append(x) for x in numbers if x not in unique_numbers]
print(unique_numbers)

# Question 9: Generate a list of tuples where each tuple contains a number and its square for numbers from 1 to 10 using list comprehension.
tuples_list = [(x, x**2) for x in range(1, 11)]
print(tuples_list)

# Question 10: Given a list of numbers, use list comprehension to replace even numbers with "Even" and odd numbers with "Odd".
numbers = [1, 2, 3, 4, 5, 6]
result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(result)

# Question 1: Create a Car class with attributes brand and model, then create an object and print the details.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

car1 = Car("Toyota", "Fortuner")
print(car1.brand, car1.model)

# Question 2: Define a Person class with name and age attributes, and add a method introduce() to print a greeting message.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

p1 = Person("Antara", 30)
p1.introduce()

# Question 3: Implement a BankAccount class with methods deposit() and withdraw(), and test it with an account balance.

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
        else:
            print("Insufficient balance")

account = BankAccount(1000)
account.deposit(500)
account.withdraw(300)
print("Current Balance:", account.balance)

# Question 4: Create a Dog class with a bark() method that prints "Woof!". Instantiate an object and call bark().

class Dog:
    def bark(self):
        print("Woof!")

d = Dog()
d.bark()

# Question 5: Write a Student class with attributes name and marks, and add a method to check if the student has passed (marks >= 40).

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def check_pass(self):
        if self.marks >= 40:
            print(f"{self.name} has passed.")
        else:
            print(f"{self.name} has failed.")

s1 = Student("Riya", 55)
s1.check_pass()

# Question 6: Modify an attribute of an existing object in a class and print the updated value.

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

emp = Employee("John", 30000)
emp.salary = 35000  # modifying attribute
print("Updated Salary:", emp.salary)

# Question 7: Delete an attribute of an object and try accessing it to observe the result.

class Item:
    def __init__(self, name):
        self.name = name

item1 = Item("Phone")
del item1.name

# Question 8: Create a Circle class with a method area() that calculates the area based on the given radius.

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

c = Circle(5)
print("Area of Circle:", c.area())

# Question 9: Implement a Book class where each book has a title and author, and a method to display details.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def show(self):
        print(f"Title: {self.title}, Author: {self.author}")

b1 = Book("Python Programming", "John Smith")
b1.show()

# Question 10: Define a Laptop class with attributes brand and price, and create multiple objects to store different laptops.

class Laptop:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

l1 = Laptop("Dell", 55000)
l2 = Laptop("HP", 60000)
l3 = Laptop("Lenovo", 45000)

print(l1.brand, l1.price)
print(l2.brand, l2.price)
print(l3.brand, l3.price)

# Question 1: Write a program that handles a ZeroDivisionError when dividing a number by zero.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Question 2: Create a program that asks the user for a number and handles a ValueError if the input is not a valid integer.

try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid integer.")

# Question 3: Write a program that tries to open a file "data.txt", handles a FileNotFoundError, and prints "File not found!".

try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found!")

# Question 4: Implement a try-except block that catches a TypeError when adding a string and an integer.

try:
    result = "Hello" + 5
except TypeError:
    print("Error: Cannot add string and integer!")

# Question 5: Create a dictionary and attempt to access a key that does not exist, handling the KeyError.

data = {"name": "Antara", "age": 30}

try:
    print(data["salary"])
except KeyError:
    print("KeyError: The key does not exist!")

# Question 6: Use a try-except-else structure where the else block prints "No error occurred" if no exceptions happen.

try:
    num = 10 / 2
except Exception:
    print("An error occurred!")
else:
    print("No error occurred")

# Question 7: Write a try-except-finally block where the finally block prints "Execution complete".

try:
    x = int("100")
except ValueError:
    print("Invalid conversion!")
finally:
    print("Execution complete")

# Question 8: Create a program that asks the user for an index and safely accesses a list element, handling an IndexError.

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter an index: "))
    print("Value:", numbers[index])
except IndexError:
    print("IndexError: Invalid index!")
except ValueError:
    print("Please enter a valid integer.")

# Question 9: Write a function that catches any general exception using except Exception as e: and prints the error message.

def divide(a, b):
    try:
        return a / b
    except Exception as e:
        print("Error occurred:", e)

divide(10, 0)

# Question 10: Implement nested exception handling where an outer try-except block catches errors that the inner try-except block does not handle.

try:
    try:
        num = int("abc")  # Inner block handles only ValueError
    except ValueError:
        print("Inner Error: Invalid number format!")

    result = 10 / 0  # Outer try handles this
except ZeroDivisionError:
    print("Outer Error: Division by zero!")