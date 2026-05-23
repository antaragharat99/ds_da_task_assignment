# Q 1: Use range() to print numbers from 0 to 4.
for i in range(5):
    print(i)

# Q 2: Create a loop that prints numbers from 5 to 10 using range().
for i in range(5, 11):
    print(i)

# Q 3: Generate numbers from 2 to 20 with a step of 3 using range() and print them.
for i in range(2, 21, 3):
    print(i)

# Q 4: Write a loop that prints numbers in reverse from 10 to 1 using range().
for i in range(10, 0, -1):
    print(i)

# Q 5: Convert range(1, 6) into a list and print it.
numbers = list(range(1, 6))
print(numbers)

# Q 6: Use range() in a for loop to print only even numbers between 1 and 10.
for i in range(2, 11, 2):
    print(i)

# Question 7: Create a loop using range() that prints "Python" five times.
for i in range(5):
    print("Python")

# Q 8: Use range() to generate numbers from -10 to -1 and print them.
for i in range(-10, 0):
    print(i)

# Q 9: Generate numbers from 50 to 30 with a step of -5 using range() and print them.
for i in range(50, 29, -5):
    print(i)

# Q 10: Write a program using range() that calculates the sum of numbers from 1 to 100.
total = sum(range(1, 101))
print(total)

# Q 1 : Create a list fruits with values ["apple", "banana", "cherry"] and print the first element.
fruits = ["apple", "banana", "cherry"]
print(fruits[0])

# Q 2 : Define a list numbers with values [10, 20, 30, 40, 50] and print the last element using negative indexing.
numbers = [10, 20, 30, 40, 50]
print(numbers[-1])

# Q 3 : Add "mango" to the fruits list using append() and print the updated list.
fruits = ["apple", "banana", "cherry"]
fruits.append("mango")
print(fruits)

# Q 4 : Insert "grape" at index 1 in the fruits list and print the updated list.
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "grape")
print(fruits)

# Q 5 : Remove "banana" from the fruits list using remove() and print the updated list.
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)

# Q 6 : Use pop() to remove the last element from numbers and print the updated list.
numbers = [10, 20, 30, 40, 50]
numbers.pop()
print(numbers)

# Q 7 : Sort the numbers list in ascending order and print the result.
numbers = [20, 10, 40, 50, 30]
numbers.sort()
print(numbers)

# Q 8 : Reverse the numbers list and print the result.
numbers = [20, 10, 40, 50, 30]
numbers.reverse()
print(numbers)

# Q 9 : Slice the fruits list to get the first two elements and print them.
fruits = ["apple", "banana", "cherry"]
print(fruits[:2])

# Q 10 : Create a nested list matrix = [[1, 2], [3, 4], [5, 6]] and print the element 4 using indexing.
matrix = [[1, 2], [3, 4], [5, 6]]
print(matrix[1][1])