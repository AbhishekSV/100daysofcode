#Day 11 App
import random
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

def draw_card(card_set):
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  new_card = random.choice(cards)
  new_set = card_set
  new_set.append(new_card)
  return new_set

def count_score(cards_list):
  score = 0
  for card in cards_list:
    score += card
  return score

def check_blackjack(choice_list):
  score = count_score(choice_list)
  if score == 21:
    return True
  return False

def check_for_ace(cards_set):
  scores = count_score(cards_set)
  while scores > 21:
    for cards in range(len(cards_set)):
      if cards_set[cards] == 11:
        cards_set[cards] = 1
    scores -= 10
  return cards_set

def check_rule(cards_stack):
  score = count_score(cards_stack)
  if score > 21:
    return 1
  return 0

def check_score(player, computer):
  return player - computer

def show_cards(dealer_cards):
  score = count_score(dealer_cards)
  print(f"Dealer Cards: {dealer_cards}, Dealer Score: {score}\n")

def computer_play(computer_card):
  score = count_score(computer_card)
  dealer_card = computer_card
  while score < 17:
    dealer_card = draw_card(dealer_card)
    score = count_score(dealer_card)
  return dealer_card

def blackjack(user_cards, computer_cards):
  should_continue = True
  while should_continue:
    print(f"Your cards: {user_cards}\n")
    user_cards = check_for_ace(user_cards)
    user_score = count_score(user_cards)
    computer_cards = check_for_ace(computer_cards)
    computer_score = count_score(computer_cards)
    
    if check_blackjack(user_cards) or check_blackjack(computer_cards):
      if check_blackjack(user_cards):
        print("You Won! by getting a blackjack")
        show_cards(computer_cards)
        should_continue = False
        continue
      print("You lose as dealer has blackjack")
      show_cards(computer_cards)
      should_continue = False
      continue

    if check_rule(user_cards):
      print("You lose due to 21 rule")
      show_cards(computer_cards)
      should_continue = False
      continue
    
    print(f"Computer's first card: {computer_cards[0]}\n")

    choice = input("Do you want to draw another card Enter 'y' or 'n'? \n")
    if choice == 'y':
      user_cards = draw_card(user_cards)
      continue
    
    computer_cards = computer_play(computer_cards)
    computer_score = count_score(computer_cards)
    if check_rule(computer_cards):
      print("You Won! as dealer lost by 21 rule")
      show_cards(computer_cards)
      should_continue = False
      continue

    if check_score(user_score, computer_score) > 0:
      print("You win! by score")
      show_cards(computer_cards)
      should_continue = False
    elif check_score(user_score, computer_score) < 0:
      print("You lose by score")
      show_cards(computer_cards)
      should_continue = False
    else:
      print("It's a tie!")
      show_cards(computer_cards)
      should_continue = False

new_game = True
while new_game:
  print("Welcome to Black Jack")
  user_deck = [] #= [random.choice(cards), random.choice(cards)]
  computer_deck = [] #= [random.choice(cards), random.choice(cards)]
  for i in range(2):
    user_deck = draw_card(user_deck)
    computer_deck = draw_card(computer_deck)
  blackjack(user_deck, computer_deck)
  go_on = input("Do you want to play a new game? Enter 'y' or 'n': ")
  if go_on == 'n':
    print("Thanks for playing, Goodbye!\n")
    new_game = False


##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

