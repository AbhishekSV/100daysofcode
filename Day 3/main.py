# Day 3 Exercise 1
number = int(input("Which number do you want to check? "))

if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")


# Day 3 Exercise 2
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = round(weight / height ** 2,2)
bmi_print = int(bmi)
if bmi < 18.5:
  print(f"Your BMI is {bmi_print}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi_print}, you a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi_print}, you slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi_print}, you obese.")
else:
  print(f"Your BMI is {bmi_print}, you are clinically obese.")


# Day 3 Exercise 3
year = int(input("Which year do you want to check? "))
#isLeapYear = None
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap Year.")
    else:
      print("Not Leap Year.")
  else:
    print("Leap Year.")
else:
  print("Not Leap Year.")


# Day 3 Exercise 4
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

bill = 0
if size == "S":
  bill += 15
elif size == "M":
  bill += 20
else:
  bill += 25

if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3
    
if extra_cheese == "Y":
  bill += 1
  
print(f"Your final bill is: ${bill}.")


# Day 3 Exercise 5
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name = name1 + name2

t = name.lower().count("t")
r = name.lower().count("r")
u = name.lower().count("u")
e = name.lower().count("e")

l = name.lower().count("l")
o = name.lower().count("o")
v = name.lower().count("v")

true_love_percent = (t+r+u+e) * 10 + (l+o+v+e)

if true_love_percent < 10 or true_love_percent > 90:
  print(f"Your score is {true_love_percent}, you go together like coke and mentos.")
elif true_love_percent >=40 and true_love_percent <= 50:
  print(f"Your score is {true_love_percent}, you are alright together.")
else:
  print(f"Your score is {true_love_percent}.")


#Exercise App
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("You get attacked by an angry trout. Game Over.")
else:
  print("You fell into a hole. Game Over.")


#Day 3 End
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("What is your age? "))
  if age < 12:
    bill = 5
    print("Child tickets are $5.")
  elif age <= 18:
    bill = 7
    print("Youth tickets are $7.")
  elif age >= 45 and age <= 55:
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets are $12.")
  
  wants_photo = input("Do you want a photo taken? Y or N. ")
  if wants_photo == "Y":
    bill += 3
  
  print(f"Your final bill is ${bill}")

else:
  print("Sorry, you have to grow taller before you can ride.")
