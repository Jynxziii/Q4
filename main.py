import random 
print('''               _             
              (_)            
  ___ __ _ ___ _ _ __   ___  
 / __/ _` / __| | '_ \ / _ \ 
| (_| (_| \__ \ | | | | (_) |
 \___\__,_|___/_|_| |_|\___/ ''')
gems = 0 
 
print("mr williams i worked on my project for most of the class period today plz dont take off points i will update later ")
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
        display_balance()
def Pick_A_Number():
  global gems
  if gems < 10:
            print("\nSorry, you don't have enough gems to spin.")
  if random.random()==3:
    gems*=15
    print("you have x15 your gems!!")
    display_balance()
  else: 
    gems*=0
    print("you have lost all your gems!!!")
    display_balance()
def DoubleGems():
  global gems
  if gems < 20:
            print("\nSorry, you don't have enough gems to double.")
            return
  if random.random() >= .5: 
     gems *= 2
     print("You have doubled your gems!")
     display_balance()
  else:
    gems = 0
    print("You lost all your gems!")
    display_balance()
  
#UI that the user sees when game starts.
while True:
    print("\n<<=== Gem Game ===>>")
    print("1. Play a Challenge (gives 10 gems)")
    print("2. Spin Wheel (costs 10 gems)")
    print("3. Show Gem Balance")
    print("4. Double Gems (costs 20 gems)")
    print("5. Quit")
    print("6. Pick a number 1-10(costs 30 gems) x15 your gems!")
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
    elif choice == "6":
        Pick_A_Number()
      break
    else:
        print("Invalid choice. Please choose again.")


