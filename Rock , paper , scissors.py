import random
computer_choice = random.randint(0,2)
choice = [""""

    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)  
""",  """" 
 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
""" , """

    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

print("welcome to rock, paper, scissors")
user_choice=int(input("""it's time to make your choice 
      type 0 for rock
      type 1for paper
      type 2 for scissors  
      :  

"""))
if user_choice not in [0,1,2]:
    print("you have entered an invalid choice")
    exit()
print(choice[user_choice])
print("computer choice is : " )
print(choice[computer_choice])

print("")


if user_choice==computer_choice:
    print("it's a draw")
elif user_choice==0 and computer_choice==1 or user_choice==1 and computer_choice==2 or user_choice==2 and computer_choice==0:

    print("you lose")

elif user_choice==0 and computer_choice==2 or user_choice==1 and computer_choice==0 or user_choice==2 and computer_choice==1:

    print("you win")




