# create rock scissors paper program that asks for user input
# 0 = rock 1 = scissors 2 = paper

import random

def whatIsIt(num):
  if num < 0 or num > 2: 
    return "You gave a wrong number! Number has to be between 0 and 2"
  choices = ["Rock", "Scissors", "Paper"]
  return choices[num]

#gives back 0-2 at random
def computerChoice():
  return random.randint(0, 2)

def rockScissorsPaper():
  #Code Here
  user_choice = input ("choose rock, paper or scisors: ")
  print(user_choice)
  # if statement that checks if user's choice is correct 
  if user_choice == "rock" or user_choice == "scisors" or user_choice == "paper":
    print("Your response is valid")
  else:
    print("Your respone is not valid")
        
  #print tie if user and computer response is the same 
  computer_choice = whatIsIt(computerChoice())
  print("computer_choice: ")
  print(computer_choice)

  #print tie if user and computer resposne is the same 
  if user_choice == computer_choice:
    print("it's a tie")
  else:
    if user_choice == "rock":
      if computer_choice == "scisors":
        print("The users won!")
        if computer_choice == "paper":
          print("The computer won!")
    elif user_choice == "scisors":
      if user_choice == "paper":
        print("The user won!")
      if computer_choice == "rock":
        print("The computer won!")
    elif user_choice == "paper":
      if computer_choice == "rock":
        print("The user won!")
        if computer_choice == "scisors":
          print("The computer won!")

  #print random computer response
  # print(whatIsIt(computerChoice()))

rockScissorsPaper()
