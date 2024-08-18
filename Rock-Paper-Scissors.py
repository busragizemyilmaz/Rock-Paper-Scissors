import random

game = 1
round = 1
player_score = 0
computer_score = 0
    
def rock_paper_scissors_Busra_Gizem_Yilmaz():  
    global game, round, player_score, computer_score

    if game == 1:
        exit_message = "Why did you call the function if you do not want to play? Come back when you want to play the game!\n"

        print("Welcome to the game! We are playing Rock-Paper-Scissors.\n"
              "This game consists of 3 rounds and whoever wins a total of 2 rounds, wins the game.\n"
              "Enter 'Rock', 'Paper', or 'Scissors' to play if you do not want to play, write 'exit'.\n"
              "The game starts!!\n")

    else:
        exit_message = "Thanks for playing!\n"

    options = ["rock", "paper", "scissors"]
                        
    while True:
        if player_score == 2:
            print("You won the game :( Congratulations!!!\n")
            break

        elif computer_score == 2:
            print("You lost the game hahaha!\n")
            break

        message = input(f"### GAME: {game} - ROUND: {round} ###\n\n"
                        "Rock, Paper, Scissors or 'exit'? : ").strip().lower()


        computer_choice = random.choice(options)

        def tie():
            global round
            round += 1

            print(f"Computer choice: {computer_choice}\n\n"
                  "It is a tie this round!\n")
        
        def lost():
            global round, computer_score
            computer_score += 1
            round += 1

            print(f"Computer choice: {computer_choice}\n\n"
                  "You lost this round!\n")
        
        def won():
            global round, player_score
            player_score += 1
            round += 1

            print(f"Computer choice: {computer_choice}\n\n"
                  "You won this round!\n")

        if message == computer_choice:
            tie()
            
        elif message == "rock":
            if computer_choice == "paper":
                lost()

            else:
                won()
        
        elif message == "paper":
            if computer_choice == "rock":
                won()

            else:
                lost()

        elif message == "scissors":
            if computer_choice == "rock":
                lost()

            else:
                won()

        elif message == "exit":
            print(exit_message)
            return
        
        else:
            print("Invalid choice! Please choose either Rock, Paper, or Scissors!\n")
            
        print(f"Player = {player_score}, Computer = {computer_score}\n\n"
              "#########################################################\n")
    
    continue_game()
        
def continue_game():
    global game, round, player_score, computer_score

    while True:
        message = input("Do you want to challenge me again? (yes/no): ").strip().lower()

        continue_options = ["I want to play again, let's play one more!", "I do not want to play with you!"]

        computer_continue_choice = random.choice(continue_options)

        if message == "yes":
            if computer_continue_choice == "I want to play again, let's play one more!":
                print(computer_continue_choice)

                game += 1
                round = 1
                player_score = 0
                computer_score = 0

                rock_paper_scissors_Busra_Gizem_Yilmaz()
                break
        
            else:
                print(computer_continue_choice)
                return

        elif message == "no":
            print("It was nice playing with you. Come back when you want to play the game!")
            return

        else:
            print("Invalid choice! Please choose yes or no!\n")

rock_paper_scissors_Busra_Gizem_Yilmaz()