#Day 26 Exercise 1
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)


#Day 26 Exercise 2
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num%2 == 0]
print(result)


#Day 26 Exercise 3
with open("file1.txt", "r") as f:
  f1_list = [int(l.strip('\n')) for l in f.readlines()]

with open("file2.txt", "r") as fl:
  f2_list = [int(m.strip('\n')) for m in fl.readlines()]

result = [n for n in f1_list if n in f2_list]
print(result)


#Day 26 Exercise 4
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
result = {word:len(word) for word in sentence.split()}
print(result)


#Day 26 Exercise 5
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {key:(value*1.8)+32 for (key,value) in weather_c.items()}
print(weather_f)


#Day 26 Exercise 6
#For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

#List Comprehension
new_list = [n + 1 for n in numbers]

#String as List
name = "Angela"
letters_list = [letter for letter in name]

#Range as List
range_list = [n * 2 for n in range(1, 5)]

#Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

#Dictionary Comprehension
import random
student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)