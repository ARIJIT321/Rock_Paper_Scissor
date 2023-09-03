import random


def get_choices():
  player_choice = input("Enter a choice (rock, paper, scissor) : ")
  options = ["rock", "paper", "scissor"]
  comuter_choice = random.choice(options)
  choices = {"Player": player_choice, "computer": comuter_choice}
  return choices


def check_win(player, computer):
  print(f"you choose {player}, computer choose {computer}")
  if (player == computer):
    return "It's a tie"
  elif (player == "rock"):
    if computer == "scissor":
      return "rock smashes scissor! you win!"
    else:
      return "paper covers rock! you loose!"
  elif (player == "paper"):
    if computer == "rock":
      return "paper covers rock! you win!"
    else:
      return "scissors cuts paper! you loose!"
  elif (player == "scissors"):
    if computer == "rock":
      return "rock smashes scissor! you loose!"
    else:
      return "scissors cuts paper! you win!"


choices = get_choices()

result = check_win(choices["Player"], choices["computer"])

print(result)
