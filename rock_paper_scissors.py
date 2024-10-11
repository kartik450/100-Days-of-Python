import random as rd

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ls = ["rock", "paper", "scissors"]
x = rd.choice(ls)

y = input('"1) Rock"\n"2) Paper"\n"3) Scissors"\nChoose: ').lower()

# Checking for draw case first
if ((y == "rock" or y == "1") and x == "rock") or \
   ((y == "paper" or y == "2") and x == "paper") or \
   ((y == "scissors" or y == "3") and x == "scissors"):
    if y == "rock" or y == "1":
        print(f"You:\n{rock}\n\n\nComputer:\n{rock}\n\nIt's a draw.")
    elif y == "paper" or y == "2":
        print(f"You:\n{paper}\n\n\nComputer:\n{paper}\n\nIt's a draw.")
    elif y == "scissors" or y == "3":
        print(f"You:\n{scissors}\n\n\nComputer:\n{scissors}\n\nIt's a draw.")

# Player loses cases
elif (y == "rock" or y == "1") and x == "paper":
    print(f"You:\n{rock}\n\n\nComputer:\n{paper}\n\nYou lost.")
elif (y == "paper" or y == "2") and x == "scissors":
    print(f"You:\n{paper}\n\n\nComputer:\n{scissors}\n\nYou lost.")
elif (y == "scissors" or y == "3") and x == "rock":
    print(f"You:\n{scissors}\n\n\nComputer:\n{rock}\n\nYou lost.")

# Player wins cases
elif (y == "scissors" or y == "3") and x == "paper":
    print(f"You:\n{scissors}\n\n\nComputer:\n{paper}\n\nYou won.")
elif (y == "paper" or y == "2") and x == "rock":
    print(f"You:\n{paper}\n\n\nComputer:\n{rock}\n\nYou won.")
elif (y == "rock" or y == "1") and x == "scissors":
    print(f"You:\n{rock}\n\n\nComputer:\n{scissors}\n\nYou won.")
