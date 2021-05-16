############DEBUGGING#####################

# Describe Problem
'''
The problem here was that the for loop was defined with range (1,20) 
where as range function doesn't iterate over upper limit
'''
def my_function():
  for i in range(1, 21):
    if i == 20:
      print("You got it")
my_function()

# Reproduce the Bug
'''
The problem here was that the randint(1,6) was used which when returns 6 
makes list throw index out of range error
'''
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0,5)
print(dice_imgs[dice_num])

# Play Computer
'''
The problem here was that the condition for year 1994 was not catched as if checks for < 1994
and elif checks for > 1994, we were able to fix it by making one of them as >= / <=
'''
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year >= 1994:
  print("You are a Gen Z.")

# Fix the Errors
'''
The problem here was that the print statement after if was not indented
'''
age = int(input("How old are you?"))
if age > 18:
  print("You can drive at age {age}.")

#Print is Your Friend
'''
The problem here was that the words per page input line had '=='
replacing it with assigment operator ('=') solved the bug
'''
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words)

#Use a Debugger
'''
The problem here was that the b_list.append statement was outside the for loop
thus only appending last item instead of all the items.
'''
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])

#Day 13 Exercise 1
'''
The problem here was that the if statement had '=' instead of '=='
'''
number = int(input("Which number do you want to check?"))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")

#Day 13 Exercise 2
'''
The problem here was that the year input was not typecasted to int
'''
year = int(input("Which year do you want to check?"))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
    print("Leap year.")
else:
  print("Not leap year.")
  
#Day 13 Exercise 3
'''
The problem here was that the first if was given or condition instead of and
also they were defined as parallel if statements instead of elif
'''
for number in range(1, 101):
  if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
  elif number % 3 == 0:
    print("Fizz")
  elif number % 5 == 0:
    print("Buzz")
  else:
    print(number)