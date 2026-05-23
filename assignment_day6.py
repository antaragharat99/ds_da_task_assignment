# Q 1 : Create a dictionary student with keys "name", "age", and "grade" and print it.
student = {"name": "John", "age": 20, "grade": "A"}
print(student)

# Q 2 : Access and print the value of the "name" key from the student dictionary.
print(student["name"])

# Q 3 : Use the get() method to access the "age" key safely and print its value.
print(student.get("age"))

# Q 4 : Add a new key-value pair "city": "Bangalore" to the student dictionary and print the updated dictionary.
student["city"] = "Bangalore"
print(student)

# Q 5 : Modify the "grade" value in the student dictionary to "A+" and print the dictionary.
student["grade"] = "A+"
print(student)

# Q 6 : Remove the "age" key from the student dictionary using pop() and print the updated dictionary.
student.pop("age")
print(student)

# Q 7 : Write a loop to print all keys and values from the student dictionary.
for key, value in student.items():
    print(key, ":", value)

# Q 8 : Check if the key "email" exists in the dictionary before accessing it.
if "email" in student:
    print(student["email"])
else:
    print("Key 'email' does not exist.")

# Q 9 : Use clear() to remove all elements from the dictionary and print it.
student.clear()
print(student)

# Q 10 : Create a nested dictionary containing information about multiple students and print details of one student using key access.
students = {
    "student1": {"name": "Ravi", "age": 18, "grade": "A"},
    "student2": {"name": "Sneha", "age": 19, "grade": "B+"},
    "student3": {"name": "Amit", "age": 20, "grade": "A+"}
}

print(students["student2"])

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