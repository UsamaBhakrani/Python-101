
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

high_income = False
good_credit = False

if not high_income or not good_credit:
    print('Eligible for loan')
else:
    print('Not eligible for loan')
