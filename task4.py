import random

def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ")
    while choice not in ['rock', 'paper', 'scissors']:
        choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    return choice

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        
        print(f"\nYou chose {user_choice}.")
        print(f"The computer chose {computer_choice}.")
        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
            user_score += 1
        else:
            print("You lose!")
            computer_score += 1
        
        print(f"Score: You {user_score} - Computer {computer_score}\n")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_game()