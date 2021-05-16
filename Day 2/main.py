#Day 2 Exercise 1
two_digit_number = input("Type a two digit number: ")
'''
first_digit = int(int(two_digit_number) / 10)
second_digit = int(two_digit_number) % 10
print(first_digit + second_digit)
'''
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])
print(first_digit + second_digit)

#Day 2 Exercise 2
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = int(weight) / float(height) ** 2
print(int(BMI))

#Day 2 Exercise 3
age = input("What is your current age?")
life_remaining = 90 - int(age)
print(f"You have {life_remaining * 365} days, {life_remaining * 52} weeks, and {life_remaining * 12} months left.")

#Exercise app
print("Welcome to the tip calculator.")
bill = input("What was the total bill? $")
tip_percent = input("What percentage tip would you like to give? 10,12,or 15? ")
head_count = input("How many people to split the bill? ")

percent_with_tip = 1 + (int(tip_percent) / 100)
share = round(float(bill) * percent_with_tip / int(head_count),2)
formatted_share = "{:.2f}".format(share)
print(f"Each person should pay: ${formatted_share}")
