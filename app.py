
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

age = 22
message = 'Eligible' if age >= 18 else 'Not eligible'
print(message)

high_income = True
good_credit = True
student = False

if (high_income or good_credit) and not student:
    print('Eligible for loan')
else:
    print('Not eligible for loan')


age2 = 22
if 18 <= age2 < 65:
    print('Adult')
