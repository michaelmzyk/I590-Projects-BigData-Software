"""This python program accepts an integer n from the command line. 
   The fizzbuzz function then iterates from 1 to n. 
   If the ith number is a multiple of two, “fizz” is printed, 
   if a multiple of three, “buzz” is printed,
   if a multiple of both “fizzbuzz” is printed,
   else the value is printed.
"""
import sys
highest_number = input("Highest number in series: ")
try:
    mark = int(highest_number)
except ValueError:
    print('\nYou did not enter a valid integer')
    sys.exit(0)
for x in range(1, int(highest_number)+1):
    if x % 2 == 0 and x % 3 == 0:
        print('fizzbuzz')
    elif x % 2 == 0:
        print('fizz')
    elif x % 3 == 0:
        print('buzz')
    else:
        print(x)
