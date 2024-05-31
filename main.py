import pygame
import sys
import random
import time
print('''               _             
              (_)            
  ___ __ _ ___ _ _ __   ___  
 / __/ _` / __| | '_ \ / _ \ 
| (_| (_| \__ \ | | | | (_) |
 \___\__,_|___/_|_| |_|\___/ ''')
gems = 0 


def display_balance():  
  print("\n{|You have", gems, "gems|}") 
#challenge to make gems


def Reaction():[BETA STILL IN PROGRESS]
    pygame.init()

    # Set up the display
    width, height = 800, 600
    display = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Reaction Time Test")

    # Define colors
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)

    # Set up fonts
    font = pygame.font.Font(None, 36)

    # Set up game variables
    start_time = None
    reaction_time = None
    click_before_green = False
    game_over = False


    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if not game_over:
                    if start_time is not None and not click_before_green:
                        end_time = time.time()
                        reaction_time = end_time - start_time - 5
                        if reaction_time < 0:
                            click_before_green = True
                        else:
                            game_over = True
            seel:l:e:e    dispspsp
                    

        display.fill(WHITE)

        if click_before_green:
            reaction_text = font.render("Clicked before green!", True, RED)
            display.blit(reaction_text, (width // 2 - reaction_text.get_width() // 2, height // 2 + 70))
        
        elif not game_over and (start_time is None or (time.time() - start_time) < 5):
            pygame.draw.rect(display, RED, (width // 2 - 50, height // 2 - 50, 100, 100))
            if start_time is None:
                start_time = time.time()
        
        elif not game_over:
            pygame.draw.rect(display, GREEN, (width // 2 - 50, height // 2 - 50, 100, 100))
        
        elif game_over:
            game_over_text = font.render("Game Over", True, RED)
            display.blit(game_over_text, (width // 2 - game_over_text.get_width() // 2, height // 2 - 30))
            
            if reaction_time is not None and not click_before_green:
                reaction_text = font.render(f"Your reaction time: {reaction_time:.3f}  seconds", True, GREEN)
                display.blit(reaction_text, (width // 2 - reaction_text.get_width() // 2, height // 2 + 10))
            restart_text = font.render("Press SPACE to restart", True, GREEN)
            display.blit(restart_text, (width // 2 - restart_text.get_width() // 2, height // 2 + 50))

        pygame.display.flip()

    pygame.quit()

def challenge(): 
    global gems   
    print('''
            ________
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####
                       d###P
                    _g###@F
                 _gN##@P
               gN###F"
              d###F
             0###F
             0###F
             0###F
             "NN@'

              ___
             q###r
              ""
''')
    questions = { "\nWhat color is a frog?": "green", 
                 "\nWhat color is a flamingo?": "pink", 
                 "\nWhat color is the sky?": "blue", 
                 "\nWhat color is a bannana?": "yellow", 
                 "\nWhat color is a strawberry?": "red",
                 "\nWhat color is a blueberry?": "blue", 
                 "\nWhat color is a raspberry?": "red",
                 "\nWhat color is a blanco?": "white",
                 "\nWhat color is a rosado?": "pink",
                 "\nWhat color is a negro?": "black"} 
    question, answer = random.choice(list(questions.items()))
    print(question) 
    user_answer=input("\nEnter your answer: ")
    if user_answer == answer: 
        print(''' 
  _____________________________________________________________________
 |.============[_F_E_D_E_R_A_L___R_E_S_E_R_V_E___N_O_T_E_]============.|
 ||%&%&%&%_    _        _ _ _   _ _  _ _ _     _       _    _ %&%&%&%&||
 ||%&%&%&/||_||_ | ||\||||_| \ (_ ||\||_(_  /\|_ |\|V||_|)|/ |\ \%&%&%||
 ||&%.--.}|| ||_ \_/| ||||_|_/ ,_)|||||_,_) \/|  ||| ||_|\|\_||{.--.%&||
 ||%/__ _\                ,-----,-'____'-,-----,               /__ _\ ||
 ||||_ / \|              [    .-;"`___ `";-.    ]             ||_ / \|||
 |||  \| || """""""""" 1  `).'.'.'`_ _'.  '.'.(` A 76355942 J |  \| ||||
 |||,_/\_/|                //  / .'    '\    \\               |,_/\_/|||
 ||%\    /   d8888b       //  | /   _  _ |    \\      .-"""-.  \    /%||
 ||&%&--'   8P |) Y8     ||   //;   a \a \     ||    //A`Y A\\  '--'%&||
 ||%&%&|    8b |) d8     ||   \\ '.   _> .|    ||    ||.-'-.||   |&%&%||
 ||%&%&|     Y8888P      ||    `|  `-'_ ` |    ||    \\_/~\_//   |&%&%||
 ||%%%%|                 ||     ;'.  ' ` /     ||     '-...-'    |%&%&||
 ||%&%&|  A 76355942 J  /;\  _.-'. `-..'`>-._  /;\               |%&%&||
 ||&%.--.              (,  ':     \; >-'`    ;` ,)              .--.%&||
 ||%( 50 ) 1  """""""  _( \  ;...---""---...; / )_```"""""""1  ( 50 )%||
 ||&%'--'============\`----------,----------------`/============'--'%&||
 ||%&JGS&%&%&%&%&&%&%&) F I F T Y   D O L L A R S (%&%&%&%&%&%&&%&%&%&||
 '"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""`''')
        print("\n Congradulations, you earned 10 diamonds!")
        gems += 10 

    else:
        print("\n Wrong answer! Try again.")
        print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⢀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣤⣒⡮⠿⠒⠒⠊⠑⠘⠋⠓⠻⠭⢕⡦⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⢴⡿⠓⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠮⣖⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣣⠟⠀⠀⠀⠀⠀⡀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣘⢄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣜⡼⠁⠀⠀⣴⣶⣿⡿⠟⠀⠀⠀⠛⠿⢿⣿⣷⣶⠆⠀⠀⠀⠀⠀⠘⢶⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡞⡿⠀⠀⠀⠀⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⢳⡳⡀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⢹⠃⠀⠀⢀⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⢧⠀⠀⠀⠀⠀
⠀⠀⠀⢹⣾⠀⠀⠀⣿⠂⣀⡠⠤⠤⢀⡀⠀⣠⣀⠤⠤⠤⠄⣀⡀⠀⠀⢀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⠀⠀
⠀⠀⠀⢸⣿⠀⠀⠀⣿⣯⣭⣤⣀⠀⠀⠈⠳⣏⣤⣶⣤⡀⠀⠀⠈⠉⢛⡏⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠸⣿⡀⠀⠀⠹⣿⣿⣿⣿⡇⠀⠀⣶⠿⣿⣿⣿⣷⠀⠀⠀⣰⡿⡀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣷⠀⠀⠀⠱⢍⡻⢭⣵⠴⠚⠁⠀⠯⣻⠭⣥⣤⡶⠾⠋⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠀⠀⠀
⠀⠀⠀⢠⢭⠿⡆⠀⠀⠀⠀⠙⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢿⣤⣤⠀⠀⠀
⠀⠀⢀⠿⠂⢈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣷⣎⠀⠺⢆⠀⠀
⠀⢀⡞⠀⠀⠀⢻⣮⡻⣭⣉⣒⠓⠖⠲⠶⠦⠦⠤⠤⠤⠤⠄⠤⠠⠐⠀⠒⠒⢂⣤⣿⣿⣿⠁⠀⠀⠘⣆⠀
⢀⡞⠁⠀⣤⠀⢀⣿⠉⠛⢿⡻⣿⣶⣦⣤⣤⣀⣀⣠⣀⣤⣤⣴⠶⢞⡛⣻⣿⣿⠿⠋⢹⡇⠀⣠⡀⠈⠻⡄
⢸⠁⠀⣾⣿⡆⠈⣿⠀⠀⠀⠈⠙⢫⣽⣾⣯⣿⣿⢹⣯⡝⣶⣬⣶⣾⢻⡝⠋⠀⠀⠀⢹⡇⠀⣿⣿⡄⠀⢻
⠸⡇⠀⣿⠋⠧⢰⡿⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠉⠛⠉⠛⠉⠛⠉⠉⠀⠀⠀⠀⠀⠀⠹⢧⡤⠟⣿⡇⠀⣿
⠀⠣⠴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⠤⠏''')
#game that gives you the prizes
def spin_wheel():
        global gems
        print('''
        .                  __
                   . ' || ' .
                .`     ||     `.
              .   \    ||    /   .
           .'/ _   \ .-''-. /   _ \
         .' J   `- .' .--. '. -`   L
       .'   F======' ((<>)) '======J
            L      '. `||' .'      F
      (      \  _.-  `-||-'  -._  /
              .     /  ||  \     .
                .  /   ||   \  .
     /            ` . _||_ . `
    /  _________    _.-||_________
        ___.....       ||._      .
                      /__\/  ''') 
        if gems < 10:
            print("\nSorry, you don't have enough gems to spin.")
            return
        gems -= 10
        prize = random.choice(["Pencil", "Eraser", "Gum", "Nothing"])
        print(f"Spinning the wheel... You won: {prize}")
        display_balance()

def question():
    global gems 
    print('''
            ________
        _jgN########Ngg_
      _N##N@@""  ""9NN##Np_
     d###P            N####p
     "^^"              T####
                       d###P
                    _g###@F
                 _gN##@P
               gN###F"
              d###F
             0###F
             0###F
             0###F
             "NN@'

              ___
             q###r
              ""
''')
    questions = { "\nWhat is the population of Japan?": "125 million",
                "\nWhen did World War II end?": "1945",
                "\nWhat is the tallest mountain in the world?": "Mount Everest",
                "\nWho wrote 'To Kill a Mockingbird'?": "Harper Lee",
                "\nHow many degrees is the boiling point of water in Celsius?": "100",
                "\nHow many continents are there in the world?": "7",
                "\nWhat is the chemical symbol for gold?": "Au", } 
    question, answer = random.choice(list(questions.items()))
    print(question) 
    user_answer=input("\nEnter your answer: ")
    if user_answer == answer: 
        print(''' 
  _____________________________________________________________________
 |.============[_F_E_D_E_R_A_L___R_E_S_E_R_V_E___N_O_T_E_]============.|
 ||%&%&%&%_    _        _ _ _   _ _  _ _ _     _       _    _ %&%&%&%&||
 ||%&%&%&/||_||_ | ||\||||_| \ (_ ||\||_(_  /\|_ |\|V||_|)|/ |\ \%&%&%||
 ||&%.--.}|| ||_ \_/| ||||_|_/ ,_)|||||_,_) \/|  ||| ||_|\|\_||{.--.%&||
 ||%/__ _\                ,-----,-'____'-,-----,               /__ _\ ||
 ||||_ / \|              [    .-;"`___ `";-.    ]             ||_ / \|||
 |||  \| || """""""""" 1  `).'.'.'`_ _'.  '.'.(` A 76355942 J |  \| ||||
 |||,_/\_/|                //  / .'    '\    \\               |,_/\_/|||
 ||%\    /   d8888b       //  | /   _  _ |    \\      .-"""-.  \    /%||
 ||&%&--'   8P |) Y8     ||   //;   a \a \     ||    //A`Y A\\  '--'%&||
 ||%&%&|    8b |) d8     ||   \\ '.   _> .|    ||    ||.-'-.||   |&%&%||
 ||%&%&|     Y8888P      ||    `|  `-'_ ` |    ||    \\_/~\_//   |&%&%||
 ||%%%%|                 ||     ;'.  ' ` /     ||     '-...-'    |%&%&||
 ||%&%&|  A 76355942 J  /;\  _.-'. `-..'`>-._  /;\               |%&%&||
 ||&%.--.              (,  ':     \; >-'`    ;` ,)              .--.%&||
 ||%( 50 ) 1  """""""  _( \  ;...---""---...; / )_```"""""""1  ( 50 )%||
 ||&%'--'============\`----------,----------------`/============'--'%&||
 ||%&JGS&%&%&%&%&&%&%&) F I F T Y   D O L L A R S (%&%&%&%&%&%&&%&%&%&||
 '"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""`''')
        print("\n Congradulations, you earned 30 diamonds!")
        gems += 30
        display_balance()
    else:
        print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⡀⢀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⣤⣒⡮⠿⠒⠒⠊⠑⠘⠋⠓⠻⠭⢕⡦⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣀⢴⡿⠓⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠑⠮⣖⠄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣼⣣⠟⠀⠀⠀⠀⠀⡀⠀⠀⠀⢀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠣⣘⢄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣜⡼⠁⠀⠀⣴⣶⣿⡿⠟⠀⠀⠀⠛⠿⢿⣿⣷⣶⠆⠀⠀⠀⠀⠀⠘⢶⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡞⡿⠀⠀⠀⠀⠙⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠀⠀⢳⡳⡀⠀⠀⠀⠀⠀
⠀⠀⠀⣰⢹⠃⠀⠀⢀⡖⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⢧⠀⠀⠀⠀⠀
⠀⠀⠀⢹⣾⠀⠀⠀⣿⠂⣀⡠⠤⠤⢀⡀⠀⣠⣀⠤⠤⠤⠄⣀⡀⠀⠀⢀⠀⠀⠀⠀⠀⠈⣿⡄⠀⠀⠀⠀
⠀⠀⠀⢸⣿⠀⠀⠀⣿⣯⣭⣤⣀⠀⠀⠈⠳⣏⣤⣶⣤⡀⠀⠀⠈⠉⢛⡏⠀⠀⠀⠀⠀⠀⣿⡆⠀⠀⠀⠀
⠀⠀⠀⠸⣿⡀⠀⠀⠹⣿⣿⣿⣿⡇⠀⠀⣶⠿⣿⣿⣿⣷⠀⠀⠀⣰⡿⡀⠀⠀⠀⠀⠀⠀⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⣿⣷⠀⠀⠀⠱⢍⡻⢭⣵⠴⠚⠁⠀⠯⣻⠭⣥⣤⡶⠾⠋⠀⠀⠀⠀⠀⠀⠀⢠⣿⡇⠀⠀⠀⠀
⠀⠀⠀⢠⢭⠿⡆⠀⠀⠀⠀⠙⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⢿⣤⣤⠀⠀⠀
⠀⠀⢀⠿⠂⢈⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣷⣎⠀⠺⢆⠀⠀
⠀⢀⡞⠀⠀⠀⢻⣮⡻⣭⣉⣒⠓⠖⠲⠶⠦⠦⠤⠤⠤⠤⠄⠤⠠⠐⠀⠒⠒⢂⣤⣿⣿⣿⠁⠀⠀⠘⣆⠀
⢀⡞⠁⠀⣤⠀⢀⣿⠉⠛⢿⡻⣿⣶⣦⣤⣤⣀⣀⣠⣀⣤⣤⣴⠶⢞⡛⣻⣿⣿⠿⠋⢹⡇⠀⣠⡀⠈⠻⡄
⢸⠁⠀⣾⣿⡆⠈⣿⠀⠀⠀⠈⠙⢫⣽⣾⣯⣿⣿⢹⣯⡝⣶⣬⣶⣾⢻⡝⠋⠀⠀⠀⢹⡇⠀⣿⣿⡄⠀⢻
⠸⡇⠀⣿⠋⠧⢰⡿⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠉⠛⠉⠛⠉⠛⠉⠉⠀⠀⠀⠀⠀⠀⠹⢧⡤⠟⣿⡇⠀⣿
⠀⠣⠴⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠷⠤⠏''')
        print("\n Wrong answer! Try again.")
        question()
def Pick_A_Number():
  global gems
  if random.random()==3:
    gems*=15
    print("you have x15 your gems!!")
    display_balance()
  else: 
    gems*=0
    print('''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡭⠥⠐⠒⠒⠒⠒⠂⠤⢤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣤⠖⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠲⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠀⠀⠀
⠀⠀⢠⠟⠀⠀⠀⠀⠀⣠⣤⣤⡀⠀⠀⠀⠀⠀⣤⣤⣄⠀⠀⠀⠀⠈⠻⡄⠀⠀
⠀⣠⠋⠀⠀⠀⠀⠀⠀⣿⣿⣿⣧⠀⠀⠀⠀⣼⣿⣿⣿⠀⠀⠀⠀⠀⠀⠹⣄⠀
⠀⡏⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡟⠀⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⢹⠀
⢰⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠛⠀⠀⠀⠀⠀⠀⠛⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⡆
⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⣤⣤⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
⠸⠀⠀⠀⠀⠀⠀⠀⣠⣴⡿⠟⠛⠋⠉⠉⠙⠛⠻⢷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠇
⠀⣇⠀⠀⠀⠀⢀⣼⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⡀⠀⠀⠀⠀⣸⠀
⠀⠘⣆⠀⠒⠲⣾⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢘⡷⠖⠒⠀⣰⠃⠀
⠀⠀⠘⣦⡀⠀⠈⠳⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⠁⠀⠀⣴⠃⠀⠀
⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠈⠛⠦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠴⠛⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠓⠒⠠⠤⠤⠤⠤⠄⠒⠚⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
    print("you have lost all your gems!!!")
    display_balance()
def Contrast():
  global gems
  if gems == 10:
    print("you can buy pizza")
  if gems ==20000:
    print("you can buy empire state building")
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
    print("1. Play a Color guesing game (gives 10 gems)")
    print("2. Answer dificult questions (gives 30 gems)")
    print("3. Spin Wheel (costs 10 gems)")
    print("4. Show Gem Balance")
    print("5. Double Gems (costs 20 gems)")
    print("6. Quit")
    print("7. what can i buy with my items?")
    print("7. Pick a number 1-10(costs 30 gems) x15 your gems!")
    print("9. Reaction time game winn 100 gems!")
    print("wheel prizes: pencil, eraser, gum, nothing \n")
    print("\n")

    choice = input("Enter your choice: ")
#Choices that the user can chose
    if choice == "1":
        challenge()
    elif choice == "2":
        question()
    elif choice == "3":
        spin_wheel()
    elif choice == "4":
        display_balance()
    elif choice == "5":
        DoubleGems()
    elif choice == "7": 
       Contrast()
    elif choice == "8":
        Pick_A_Number()
    elif choice == "9":
        Reaction()
    elif choice == "6":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Please choose again.")
