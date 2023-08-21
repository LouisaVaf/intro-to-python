print("My first project")

print("Hi and welcome to Watson's version of Rock, paper, Scissors! \nIn this version we use Cuddles, Treats and Walkies. \n Walkies beats Treats. \n Cuddles beats Walkies, \n Treats beats Cuddles.")

print("Before we play, you may be wondering who's Watson? Well...Watson AKA Mr.Watson is Louisa's mum's 7 year old dachshund! \nAs you may be able to tell, Louisa loves him very much :D")
f = open("Watson.txt", "r")
file_content = f.read()
print(file_content)
f.close()

print("Now that you're familiar with who inspired this customised game, let's go ahead and play!")


import random
import os
import re

def check_play_status():
  valid_responses = ["yes", "no"]
  while True:
    try:
      response = input("Do you wish to play again? (Yes or No): ")
      if response.lower() not in valid_responses:
        raise ValueError("Yes or No only")

      if response.lower() == "yes":
        return True
      else:
        os.system("cls" if os.name == "nt" else "clear")
        print("Thanks for playing!")
        exit()

    except ValueError as err:
      print(err)
      

def play_rps():
  play = True
  while play:
    print("Cuddles, Treats, Walkies - Go!")

    user_choice = input("Make your choice"
                       " [C]uddles, [T]reats or [W]alkies: ")
    if not re.match("[CcTtWw]", user_choice):
      print("Please choose a letter: ")
      print("[C]uddles, [T]reats or [W]alkies")
      continue
    print("You chose " + user_choice)

    choices = ["C", "T", "W"]
    opp_choice = random.choice(choices)
    print("I chose " + opp_choice)


    if opp_choice == user_choice.upper():
     print("Tie!")
     play = check_play_status()
    elif opp_choice == "C" and user_choice.upper() == "W":
     print("Cuddles beats Walkies, I win!")
     play = check_play_status()
    elif opp_choice == "W" and user_choice.upper() == "T":
     print("Walkies beats Treats, I win!")
     play = check_play_status()
    elif opp_choice == "T" and user_choice.upper() == "C":
     print("Treats beats Cuddles, I win!")
     play = check_play_status()
    else:
     print("You win!")
     play - check_play_status()

play_rps()
  