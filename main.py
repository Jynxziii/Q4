import random 

gems = 0

def display_balance():
  print("\n{|You have", gems, "gems|}")
#challenge to make gems
def challenge(): 
    global gems
    questions = {"\nWhat color is a frog?": "green", "\nWhat color is a flamingo?": "pink", "\nWhat color is the sky?": "blue"} 
    question, answer = random.choice(list(questions.items()))
    print(question)
    user_answer=input("\nEnter your answer: ")
    if user_answer == answer:
        print("\n Congradulations, you earned 10 diamonds!")
        gems += 10
    else:
        print("\n Wrong answer! Try again.")
#game that gives you the prizes
def spin_wheel():
        global gems
        if gems < 10:
            print("\nSorry, you don't have enough gems to spin.")
            return
        gems -= 10
        prize = random.choice(["Pencil", "Eraser", "Gum", "Nothing"])
        print(f"Spinning the wheel... You won: {prize}")
def DoubleGems():
  global gems
  if random.random() >= .5: 
     gems *= 2
     print("You have doubled your gems!")
  else:
    gems = 0
   
  
#UI that the user sees when game starts.
while True:
    print("\n<<=== Gem Game ===>>")
    print("1. Play a Challenge (gives 5 gems)")
    print("2. Spin Wheel (costs 10 gems)")
    print("3. Show Gem Balance")
    print("4. Double Gems (costs 20 gems)")
    print("5. Quit")
    print("wheel prizes: pencil, eraser, gum, nothing \n")
    print("\n")

    choice = input("Enter your choice: ")
#Choices that the user can chose
    if choice == "1":
        challenge()
    elif choice == "2":
        spin_wheel()
    elif choice == "3":
        display_balance()
    elif choice == "4":
        DoubleGems()
    elif choice == "5":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please choose again.")
