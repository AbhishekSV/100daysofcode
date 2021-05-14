#Day 9 Exercise 1
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
student_grades = {}
for student in student_scores:
  if student_scores[student] > 90:
    student_grades[student] = "Outstanding"
  elif student_scores[student] > 80:
    student_grades[student] = "Exceeds Expectations"
  elif student_scores[student] > 70:
    student_grades[student] = "Acceptable"
  else:
    student_grades[student] = "Acceptable"
print(student_grades)


#Day 9 Exercise 2
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
def add_new_country(country_name, no_of_visits, cities_list):
  new_item = {}
  new_item['country'] = country_name
  new_item['visits'] = no_of_visits
  new_item['cities'] = cities_list
  travel_log.append(new_item)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
#for item in travel_log:
#  print(travel_log[item])
#print(travel_log[0]['country'])
print(travel_log)


#Day 9 App
from os import system
bidders = {}
print("Welcome to blind auction")

def highest_bidder(bidders_list):
  max_bid = 0
  max_bidder = ""
  for bidder in bidders_list:
    if bidders_list[bidder] > max_bid:
      max_bid = bidders_list[bidder]
      max_bidder = bidder
  print(f"The winner is {max_bidder} with a bid of ${max_bid}")

more_bidders = True
while more_bidders:
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  bidders[name] = bid
  user_choice = input("Are there any other bidders? Type 'yes or 'no'.\n")
  if user_choice == 'no':
    more_bidders = False
    highest_bidder(bidders)
  system('clear')
