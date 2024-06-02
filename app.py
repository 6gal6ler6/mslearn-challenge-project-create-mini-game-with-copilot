import random

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 3 and computer_choice == 2) or \
         (player_choice == 2 and computer_choice == 1):
        return "win"
    else:
        return "lose"

# Function to play the game
def play_game():
    choices = {1: "rock", 2: "paper", 3: "scissors"}
    player_score = 0
    computer_score = 0

    while True:
        try:
            player_choice = int(input("Enter 1 for rock, 2 for paper, or 3 for scissors: "))
            if player_choice not in choices:
                print("Invalid choice, try again.")
                continue
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        computer_choice = random.randint(1, 3)
        print(f"Computer chose: {choices[computer_choice]}")
        
        result = determine_winner(player_choice, computer_choice)
        if result == "win":
            print("You win this round!")
            player_score += 1
        elif result == "lose":
            print("You lose this round!")
            computer_score += 1
        else:
            print("It's a tie!")
        
        print(f"Score - You: {player_score}, Computer: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break

    print("Thanks for playing!")
    print(f"Final Score - You: {player_score}, Computer: {computer_score}")

# Start the game
if __name__ == "__main__":
    play_game()
