import random
import art_highlow
import game_data
from os import system

def check_score(guess, a_b):
  """
  Checks followers against user's guess
  and returns True if they got it right.
  Or False if they got it wrong.
  """
  if a_b['a']['follower_count'] > a_b['b']['follower_count']:
    return guess == 'a'
  else:
    return guess == 'b'


def game_play(game_list, score):
  """
  Let's user play game, takes in sequential list to compare and base score.
  Returns score based on user play.
  """
  a_vs_b = {}
  for index in range(len(game_list)):
    a_vs_b['a'] = game_list[index]
    a_vs_b['b'] = game_list[index + 1]
    system('clear')
    print(art_highlow.logo)
    if score > 0:
      print(f"You're right! Current score: {score}.")
    print(f"Compare A: {a_vs_b['a']['name']}, {a_vs_b['a']['description']}, from {a_vs_b['a']['country']}")
    print(art_highlow.vs)
    print(f"Against B: {a_vs_b['b']['name']}, {a_vs_b['b']['description']}, from {a_vs_b['b']['country']}")
    choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    result = check_score(choice,a_vs_b)
    if result:
      score += 1
    else:
      return score

def main():
  score = 0
  game_list = random.sample(game_data.data,len(game_data.data))
  score = game_play(game_list, score)
  system('clear')
  print(f"Sorry, that's wrong. Final score: {score}")

if __name__ == "__main__":
    main()