#Day 1
print("Hello World!")

#Day 1 Exercise 1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

#Day 1 Exercise 2
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

#Input function
print("Hello " + input("What's your name?\n") + "!")

#Day 1 Exercise 3
print(len(input("What is your name?\n")))

#Day 1 Exercise 4
a = input("a: ")
b = input("b: ")
#a,b = b,a
c = a
a = b
b = c
print("a: " + a)
print("b: " + b)

#Exercise App

#1. Create a greeting for your program.
print("Welcome to Band Name Generator.")
#2. Ask the user for the city that they grew up in.
city = input("What's name of the city you grew up in?\n")
#3. Ask the user for the name of a pet.
pet = input("What's your pet's name?\n")
#4. Combine the name of their city and pet and show them their band name.
print("Your band name could be "+ city + " " + pet)
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://band-name-generator-end.appbrewery.repl.run/