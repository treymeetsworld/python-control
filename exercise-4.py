# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle

a = input('Enter the length of side  a of a triangle:')
b = input('Enter the length of side b of a triangle:')
c = input('Enter the length of side c of a triangle:')
print('a:' , a)
print('b:', b)
print('c:', c)

if a == b and a == c:
  print(f'A triangle with sides of {a}, {b} & {c}is an equilateral triangle')
if a != b or a == c or b == c or a != c:
  print(f'A triangle with sides of {a}, {b} & {c}is an isosceles triangle')
if a != b and a != c and b != c :
  print(f'A triangle with sides of {a}, {b} & {c}is a scalene triangle')