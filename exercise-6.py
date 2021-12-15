# exercise-06 What's the  Season?

# Write the code that:
# 1. Prompts the user to enter the month (as three characters):
#      Enter the month of the year (Jan - Dec):
# 2. Then prompts the user to enter the day of the month: 
#      Enter the day of the month:
# 3. Calculate what season it is based upon this chart:
#      Dec 21 - Mar 19: Winter
#      Mar 20 - Jun 20: Spring
#      Jun 21 - Sep 21: Summer
#      Sep 22 - Dec 20: Fall
# 4. Print the result as follows:
#      <Mmm> <dd> is in <season> 

# Hints:
# Consider using the in operator to check if a string is in a particular list/tuple like this:
# if input_month in ('Jan', 'Feb', 'Mar'):
#
# After setting the likely season, you can use another if...elif...else statement to "adjust" if
# the day number falls within a certain range.
month = input('Enter the month of the year (as three characters)').lower()
day = input(' Enter the day of the month: ')

# if day in 'dec' >= 21 or day in 'mar' <= 19:

if month in ( 'jan', 'feb', 'mar'):
  print(f'{month} {day} is in winter')
elif month in ('apr', 'may', 'jun'):
  print(f'{month} {day} is in spring')
elif month in ('jul', 'aug', 'sep'):
  print(f'{month} {day} is in summer')
elif month in ('oct', 'nov', 'dec'):
  print(f'{month} {day} is in fall')
  
if month == 'dec' and int(day) > 20:
  print(f'{month} {day} is in winter')
elif month == 'mar' and int(day) > 19:
  print(f'{month} {day} is in spring')
elif month == 'jun' and int(day) > 20:
  print(f'{month} {day} is in summer')
elif month == 'sep' and int(day) > 21:
  print(f'{month} {day} is in fall')