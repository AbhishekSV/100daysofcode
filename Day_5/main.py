#Day 5 Assignment 1
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
no_of_students = 0
sum_of_heights = 0
for height in student_heights:
  no_of_students+=1
  sum_of_heights+=height
print(round(sum_of_heights/no_of_students))


#Day 5 Assignment 2
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
max_score = 0 #student_scores[0]
for score in student_scores:
  if score > max_score:
    max_score = score
print(f"The highest score in the class is: {max_score}")


#Day 5 Assignment 3
total = 0
for number in range(2, 101, 2):
  total += number
print(total)


#Day 5 App
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for letter in range(0, nr_letters):
  password += random.choice(letters)
for letter in range(0, nr_symbols):
  password += random.choice(symbols)
for letter in range(0, nr_numbers):
  password += random.choice(numbers)
print(f"Easy password: {password}")

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_password = ""
password_length = nr_letters + nr_numbers + nr_symbols

password_l = random.sample(letters, nr_letters)
password_s = random.sample(symbols, nr_symbols)
password_n = random.sample(numbers, nr_numbers)
password_t = password_l + password_s + password_n

for letter in random.sample(password_t, password_length):
  hard_password += letter
print(f"Hard password: {hard_password}")

