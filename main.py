import random


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

choice = ["rock", "paper", "scissors"]
comp_choice = random.choice(choice)
my_choice = int(input("Enter a choice - 0 to choose rock, 1 to choose paper, 2 to choose scissors: "))

try:
    
    if comp_choice == choice[0]:
        print("\n The computer chose: rock " + rock)
        if choice[my_choice] == choice[0]:
            print("You chose: rock " + rock)
            print("IT'S A DRAW! \n")
        elif choice[my_choice] == choice[1]:
            print("You chose: paper " + paper)
            print("YOU WIN!! \n")
        else:
            print("You chose: scissors " + scissors)
            print("YOU LOSE!! \n")
            
    elif comp_choice == choice[1]:
        print("\n The computer chose: paper " + paper)
        if choice[my_choice] == choice[0]:
            print("You chose: rock " + rock)
            print("YOU LOSE!! \n")
        elif choice[my_choice] == choice[1]:
            print("You chose: paper " + paper)
            print("IT'S A DRAW! \n")
        else:
            print("You chose: scissors " + scissors)
            print("YOU WIN!! \n")
            
    else:
        print("\n The computer chose: scissors " + scissors)
        if choice[my_choice] == choice[0]:
            print("You chose: rock " + rock)
            print("YOU WIN!! \n")
        elif choice[my_choice] == choice[1]:
            print("You chose: paper " + paper)
            print("YOU LOSE!! \n")
        else:
            print("You chose: scissors " + scissors)
            print("IT'S A DRAW! \n")

except IndexError:
    print("\n You may have given wrong input. Please try again! \n")
