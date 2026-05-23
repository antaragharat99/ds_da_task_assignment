# 1. Write a program using map() to convert a list of integers [1, 2, 3, 4, 5] into their squares.
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x * x, numbers))
print(squares)

# 2. Use map() to convert a list of temperatures in Celsius [0, 10, 20, 30, 40] to Fahrenheit.
celsius = [0, 10, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit)

# 3. Given a list of names ["alice", "bob", "charlie"], use map() to capitalize each name.
names = ["alice", "bob", "charlie"]
capitalized = list(map(lambda n: n.capitalize(), names))
print(capitalized)

# 4. Write a program using map() to convert a list of numbers [1, 2, 3, 4, 5] into their string representations.
nums = [1, 2, 3, 4, 5]
string_list = list(map(str, nums))
print(string_list)

# 5. Use map() to add corresponding elements of two lists [1, 2, 3] and [4, 5, 6].
list1 = [1, 2, 3]
list2 = [4, 5, 6]
sum_list = list(map(lambda a, b: a + b, list1, list2))
print(sum_list)

# 6. Write a program that uses map() with lambda to multiply each element in a list [2, 4, 6, 8] by 3.
values = [2, 4, 6, 8]
multiplied = list(map(lambda x: x * 3, values))
print(multiplied)

# 7. Convert a list of words ["hello", "world", "python"] into their lengths using map().
words = ["hello", "world", "python"]
lengths = list(map(len, words))
print(lengths)

# 8. Given a list of mixed data types [1, "2", "three", 4, "5"], use map() to convert only numeric values to integers.
mixed = [1, "2", "three", 4, "5"]
converted = list(map(lambda x: int(x) if str(x).isdigit() else x, mixed))
print(converted)

# 9. Use map() to compute the cube of each number in a list [1, 2, 3, 4, 5].
nums_list = [1, 2, 3, 4, 5]
cubes = list(map(lambda x: x**3, nums_list))
print(cubes)

# 10. Write a function that takes a sentence and uses map() to convert each word to uppercase.
def upper_words(sentence):
    return list(map(str.upper, sentence.split()))

print(upper_words("python is amazing"))

# 1. Write a program using `filter()` to extract even numbers from a list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_nums = list(filter(lambda x: x % 2 == 0, numbers))
print(even_nums)

# 2. Use `filter()` to find all numbers greater than 5 in a list [3, 6, 2, 8, 5, 10].
nums = [3, 6, 2, 8, 5, 10]
greater_than_5 = list(filter(lambda x: x > 5, nums))
print(greater_than_5)

# 3. Given a list of words ["apple", "banana", "cherry", "avocado", "grape"], use `filter()` to extract words that start with "a".
words = ["apple", "banana", "cherry", "avocado", "grape"]
starts_with_a = list(filter(lambda w: w.startswith("a"), words))
print(starts_with_a)

# 4. Write a program using `filter()` to select only positive numbers from [-5, -2, 0, 3, 7, -1].
values = [-5, -2, 0, 3, 7, -1]
positive = list(filter(lambda x: x > 0, values))
print(positive)

# 5. Use `filter()` to extract only odd numbers from a list [10, 15, 20, 25, 30, 35].
nums_list = [10, 15, 20, 25, 30, 35]
odd_nums = list(filter(lambda x: x % 2 != 0, nums_list))
print(odd_nums)

# 6. Given strings ["Python", "", "Java", " ", "C++", ""], use `filter()` to remove empty strings.
strings = ["Python", "", "Java", " ", "C++", ""]
non_empty = list(filter(lambda s: s.strip() != "", strings))
print(non_empty)

# 7. Write a function using `filter()` to extract numbers that are divisible by 3 from [1, 2, 3, 4, 5, 6, 7, 9, 12, 15].
def divisible_by_3(numbers):
    return list(filter(lambda x: x % 3 == 0, numbers))

print(divisible_by_3([1, 2, 3, 4, 5, 6, 7, 9, 12, 15]))

# 8. Use `filter()` with lambda to find words with more than 5 letters from ["short", "longer", "big", "small", "elephant"].
words_list = ["short", "longer", "big", "small", "elephant"]
more_than_5 = list(filter(lambda w: len(w) > 5, words_list))
print(more_than_5)

# 9. Write a program that uses `filter()` to remove negative numbers from a list [-3, -1, 2, 4, -6, 8].
values2 = [-3, -1, 2, 4, -6, 8]
remove_negative = list(filter(lambda x: x >= 0, values2))
print(remove_negative)

# 10. Given a list of names ["Alice", "Bob", "Anna", "Charlie"], use `filter()` to extract names that start with "A".
names = ["Alice", "Bob", "Anna", "Charlie"]
names_start_with_A = list(filter(lambda n: n.startswith("A"), names))
print(names_start_with_A)

# 1. Write a program using reduce() to calculate the sum of all numbers in a list [10, 20, 30, 40, 50].
from functools import reduce
import math

numbers = [10, 20, 30, 40, 50]
sum_result = reduce(lambda a, b: a + b, numbers)
print(sum_result)

# 2. Use reduce() to find the maximum number in the list [12, 45, 78, 34, 89, 23].
nums = [12, 45, 78, 34, 89, 23]
max_num = reduce(lambda a, b: a if a > b else b, nums)
print(max_num)

# 3. Write a program that uses reduce() to multiply all elements in [2, 3, 5, 7].
values = [2, 3, 5, 7]
product = reduce(lambda a, b: a * b, values)
print(product)

# 4. Use reduce() to concatenate all strings in ["Hello", " ", "World", "!"].
strings = ["Hello", " ", "World", "!"]
concat = reduce(lambda a, b: a + b, strings)
print(concat)

# 5. Given a list [3, 6, 9, 12, 15], use reduce() to find the greatest common divisor (GCD).
numbers_gcd = [3, 6, 9, 12, 15]
gcd_result = reduce(math.gcd, numbers_gcd)
print(gcd_result)

# 6. Write a program using reduce() to compute the factorial of 5 using the list [1, 2, 3, 4, 5].
num = [1, 2, 3, 4, 5]
factorial = reduce(lambda a, b: a * b, num)
print(factorial)

# 7. Use reduce() to calculate the product of all even numbers in [1, 2, 3, 4, 5, 6, 8, 10].
nums_even = [1, 2, 3, 4, 5, 6, 8, 10]
product_even = reduce(lambda a, b: a * b, filter(lambda x: x % 2 == 0, nums_even))
print(product_even)

# 8. Write a function using reduce() to compute the sum of squares of [2, 4, 6, 8].
def sum_of_squares(lst):
    return reduce(lambda a, b: a + b, map(lambda x: x * x, lst))

print(sum_of_squares([2, 4, 6, 8]))

# 9. Use reduce() to find the longest word in ["apple", "banana", "cherry", "avocado"].
words = ["apple", "banana", "cherry", "avocado"]
longest_word = reduce(lambda a, b: a if len(a) > len(b) else b, words)
print(longest_word)

# 10. Given a list [100, 50, 25, 5], use reduce() to perform cumulative division (i.e., 100 / 50 / 25 / 5).
values_div = [100, 50, 25, 5]
division_result = reduce(lambda a, b: a / b, values_div)
print(division_result)