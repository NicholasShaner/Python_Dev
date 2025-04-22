# get name as a string
print('What is your name? ',end='')
user_name = input()
print()
# get age as an int
print('How old are you? ',end='')
user_age = int(input())
print()

# calculate birth year
from datetime import date
current_yr = date.today().year
year_born = current_yr - user_age
# print greeting
print(f'Hello {user_name}! You were born in {year_born}.')