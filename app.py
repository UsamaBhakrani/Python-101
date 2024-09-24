
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
def save_user(**user):
    print(user['name'])


save_user(id=1, name='John', age=22)
