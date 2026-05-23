# Question 1 : Create a set fruits with values {"apple", "banana", "cherry"} and print it.
fruits = {"apple", "banana", "cherry"}
print(fruits)

# Question 2 : Add "grape" to the fruits set using add() and print the updated set.
fruits.add("grape")
print(fruits)

# Question 3 : Remove "banana" from the fruits set using remove() and print the updated set.
fruits.remove("banana")
print(fruits)

# Question 4 : Try removing an element that does not exist using discard(). Observe if an error occurs.
fruits.discard("orange")
print(fruits)

# Question 5 : Create two sets A = {1, 2, 3, 4} and B = {3, 4, 5, 6}, and print their union.
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A.union(B))

# Question 6 : Find the intersection of sets A and B and print the result.
print(A.intersection(B))

# Question 7 : Compute the difference between sets A and B (A - B) and print the result.
print(A - B)

# Question 8 : Convert a list [1, 2, 2, 3, 4, 4, 5] to a set and print it to remove duplicates.
numbers_list = [1, 2, 2, 3, 4, 4, 5]
numbers_set = set(numbers_list)
print(numbers_set)

# Question 9 : Use a loop to iterate through the fruits set and print each element.
for item in fruits:
    print(item)

# Question 10 : Check if "apple" exists in the fruits set using the in keyword and print the result.
print("apple" in fruits)

# Question 1 : Create a tuple fruits with values ("apple", "banana", "cherry") and print it.
fruits = ("apple", "banana", "cherry")
print(fruits)

# Question 2 : Access and print the first and last elements of the fruits tuple using indexing.
print(fruits[0])
print(fruits[-1])

# Question 3 : Use slicing to print the first two elements of the fruits tuple.
print(fruits[:2])

# Question 4 : Create a tuple numbers with values (10, 20, 30, 40), and find its length using len().
numbers = (10, 20, 30, 40)
print(len(numbers))

# Question 5 : Check how many times "apple" appears in the tuple ("apple", "banana", "apple", "cherry") using count().
sample = ("apple", "banana", "apple", "cherry")
print(sample.count("apple"))

# Question 6 : Find the index of "banana" in the tuple using index().
sample2 = ("apple", "banana", "cherry")
print(sample2.index("banana"))

# Question 7 : Concatenate two tuples (1, 2, 3) and (4, 5, 6) and print the resulting tuple.
t1 = (1, 2, 3)
t2 = (4, 5, 6)
result = t1 + t2
print(result)

# Question 8 : Repeat the tuple (1, 2) three times and print the result.
t = (1, 2)
print(t * 3)

# Question 9 : Convert the tuple ("red", "green", "blue") into a list, add "yellow", and convert it back into a tuple.
colors = ("red", "green", "blue")
colors_list = list(colors)
colors_list.append("yellow")
colors = tuple(colors_list)
print(colors)

# Question 10 : Write a loop to iterate through the tuple ("Python", "Java", "C++") and print each item.
languages = ("Python", "Java", "C++")
for lang in languages:
    print(lang)