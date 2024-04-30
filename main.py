import random 

gems = 100
diamonds = 0

def 
#challenge to make gems
def challenge(): 
    questions = {"What color is a frog?": "green", "What color is a flamingo?": "pink", "What color is the sky?": "blue"} 
    question, answer = random.choice(list(d.items()))
    if user_answer == answer:
        print("Congradulations, you earned 10 diamonds!")
    else:
        print("Wrong answer! Try again.")
#game that gives you the prizes
def spin_wheel():
        if GemGame.gems < 10:
            print("Sorry, you don't have enough gems to spin.")
            return
        GemGame.gems -= 10
        prize = random.choice(["Pencil", "Eraser", "Gum", "Nothing"])
        print(f"Spinning the wheel... You won: {prize}")

#UI that the user sees when game starts.
game = GemGame()
while True:
    print("\n=== Gem Game ===")
    print("1. Play a Challenge (gives 5 gems)")
    print("2. Spin Wheel (costs 10 gems)")
    print("3. Show Gem Balance")
    print("4. Quit")
    print("wheel prizes: pencil, eraser, gum, nothing")
    
    choice = input("Enter your choice: ")
#Choices that the user can chose
    if choice == "1":
        challenge()
    elif choice == "2":
        spin_wheel()
    elif choice == "3":
        display_balance()
    elif choice == "4":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please choose again.")
    
