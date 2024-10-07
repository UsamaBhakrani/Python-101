
from pprint import pprint
from sys import getsizeof
from array import array
from collections import deque
import math
is_loading = False
number = 1000
name = 'Usama Bhakrani'


# \"
# \'
# \\
# \n

# print(len(name))
# print(name[0])
# print(name[-1])
# print(name[0:3])


first = 'Usama'
last = 'Bhakrani'

full = f"{len(first)} {last}"
# print(full)


# print(round(2.9))


# Logic

# temperature = 15
# if temperature > 30:
#     print('It is too hot.')
#     print('Please Start the Aircon')
# elif temperature > 20:
#     print('Please Stop the Aircon')
# else:
#     print('It is cold.')
#     print('Please Start the Heater')

# age = 22
# message = 'Eligible' if age >= 18 else 'Not eligible'
# print(message)

# high_income = True
# good_credit = True
# student = False

# if (high_income or good_credit) and not student:
#     print('Eligible for loan')
# else:
#     print('Not eligible for loan')


# age2 = 22
# if 18 <= age2 < 65:
#     print('Adult')


# loops

# for number in range(1, 10, 2):
#     print('Attempt', number+1, number * '.')

# successful = True
# for number in range(3):
#     print('Attempt')
#     if successful:
#         print('Success')
#         break
# else:
#     print('Failed after 3 attempts')

# nested Loops

# for x in range(5):
#     for y in range(3):
#         print(f'{x}, {y}')


# Iterables

# print(type(5))
# print(type(range(5)))

# for x in [1, 2, 3, 4]:
#     print(x)

# While Loops

# number = 100
# while number > 0:
#     print(number)
#     number //= 2
#     if number == 2:
#         break


# exercise 1
# count = 0
# for x in range(1, 10):
#     if x % 2 == 0:
#         count += 1
#         print(x)
# print(f'We have {count} even numbers')


# Creating Functions

# def greet(first_name, last_name):
#     print(f'{first_name}, {last_name}')
#     print(f'{first_name}, {last_name} 2')


# greet('Usama', 'Bakhrani')


# def increment(number, by=2):
#     return number + by


# print(increment(5))

# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         total *= number
#     return total


# print(multiply(2, 3, 4, 5))

# Dictionary
# def save_user(**user):
#     print(user['name'])


# save_user(id=1, name='John', age=22)

# def multiply(*numbers):
#     result = 1
#     for number in numbers:
#         result *= number
#     return result


# print('Start')
# print(multiply(1, 2, 3))


# FizzBuzz

# def fizz_buzz(input):
#     if (input % 3 == 0) and (input % 5 == 0):
#         return 'FizzBuzz'
#     if input % 3 == 0:
#         return 'Fizz'
#     if input % 5 == 0:
#         return 'Buzz'
#     return input


# print(fizz_buzz(15))


# Data Structures

# letters = ['a', 'b', 'c']
# matrix = [[0, 1], [2, 3]]
# zeros = [0] * 5
# combined = zeros + letters
# print(list(range(20)))
# print(combined)

# chars = list('Hello World')
# print(chars)


# unpacking lists
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# first, second, *other = numbers

# first = numbers[0]
# second = numbers[1]
# third = numbers[2]

# print(first)
# print(other)

# Index unpacking from lists
# letters = ['a', 'b', 'c']
# for index, letter in enumerate(letters):
#     print(index, letter)

# adding or removing items from lists
# letters = ['a', 'b', 'c']
# letters.append('d')
# letters.insert(0, 'e')
# letters.pop(0)
# letters.remove('b')
# del letters[0]
# letters.clear()
# print(letters)

# finding items in lists
# letters = ['a', 'b', 'c']
# letters.count('d')
# if 'd' in letters:
#     print(letters.index('d'))


# sorting lists
# numbers = [3, 42, 23, 12, 24]
# numbers.sort(reverse=True)
# print(sorted(numbers, reverse=True))
# print(numbers)

# Sorting Tuples with lambda functions
# numbers = [(1, 'a'), (2, 'b'), (3, 'c')]

# numbers.sort(key=lambda item: item[1])
# print(numbers)

# Map function with tuples
# items = [('a', 10), ('b', 20), ('c', 30)]
# x = list(map(lambda item: item[1], items))
# print(x)


# Filtering Lists
# items = [('a', 10), ('b', 20), ('c', 30)]
# x = list(filter(lambda item: item[1] >= 30, items))
# print(x)

# List comprehension
# items = [('a', 10), ('b', 20), ('c', 30)]
# prices = [item for item in items if item[1] >= 30]
# print(prices)

# numbers = [('a', 10), ('b', 20), ('c', 30)]
# price = [item for item in items if item[1] >= 30]

# combine lists
# list1 = [1, 2, 3]
# list2 = [10, 20, 30]
# print(list(zip(list1, list2)))

# append and pop stacks
# stack = [1, 2, 3, 4, 5, 6, 7, 8]
# stack.append(15)
# stack.pop()
# print(stack)

# Deque
# queue = deque([])
# queue.append(1)
# queue.append(2)
# queue.append(3)
# queue.popleft()
# print(queue)

# if not queue:
#     print('empty')

# tuples
# point = 1, 2
# point1 = tuple([1, 2])


# swapping varaiables
# x = 10
# y = 11
# x, y = y, x
# print(x, y)

# Arrays
# numbers = array('i', [1, 2, 3, 4, 5, 6, 7, 8])
# numbers.append(9)


# Sets
# numbers = [1, 1, 2, 3, 4, 3, 5]
# first = set(numbers)
# second = {1, 11}
# print(first | second)
# print(first & second)
# print(first - second)
# print(first ^ second)

# if 1 in first:
#     print('yes')


# Dictionaries
# point = {'x': 1, 'y': 2}
# point = dict(x=1, y=2)
# point['z'] = 10
# if 'a' in point:
#     print(point['a'])
# print(point.get('a', 0))

# for key, value in point.items():
#     print(key, value)


# Dictionary comprehension
# values = {}
# for x in range(5):
#     values[x] = x * 2
# print(values)

# Or

# values = {x: x * 2 for x in range(5)}
# print(values)

# List comprehensions

# values = (x * 2 for x in range(100000))
# print(getsizeof(values))

# values = [x * 2 for x in range(100000)]
# print(getsizeof(values))

# values = {x * 2 for x in range(100000)}
# print(getsizeof(values))


# Unpacking numbers
# numbers = [1, 2, 3]
# numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print([*numbers, *numbers2])


# Exercise
# sentence = 'This is a common interview question'
# char_frequency = {}
# for x in sentence:
#     if x in char_frequency:
#         char_frequency[x] += 1
#     else:
#         char_frequency[x] = 1

# char_frequency_sorted = sorted(
#     char_frequency.items(), key=lambda x: x[1], reverse=True)
# print(char_frequency_sorted[0])

# Exceptions

# try:
#     age = int(input('Age: '))
# except ValueError:
#     print('Not valid age')
# else:
#     print('no Exception found')

# try:
#     with open('app.py') as file:
#         print('File Opened')
#     age = int(input('Age: '))
#     xfactor = 10/age
# except (ValueError, ZeroDivisionError):
#     print('You didnt enter a valid age')
# else:
#     print('No exceptions were thrown')
# finally:
#     file.close()

# raising exceptions

# def calculate_xfactor(age):
#     if age <= 0:
#         raise ValueError('Age must be a positive number')
#     return 10 / age


# try:
#     calculate_xfactor(-1)
# except ValueError as error:
#     print(error)
