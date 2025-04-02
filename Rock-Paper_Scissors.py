import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def get_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def play_game():
    print("Welcome to Rock-Paper-Scissors!")

    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        user_choice = input("Choose Rock, Paper, or Scissors (or type 'exit' to quit): ").lower()
        if user_choice == "exit":
            print(f"Final Score: You {user_score} - {computer_score} Computer")
            print("Thanks for playing! ")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please select Rock, Paper, or Scissors.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice.capitalize()}")

        result = get_winner(user_choice, computer_choice)
        if result == "user":
            user_score += 1
            print(" You win this round!")
        elif result == "computer":
            computer_score += 1
            print(" Computer wins this round!")
        else:
            print("It's a draw!")

        rounds += 1
        print(f"Score: You {user_score} - {computer_score} Computer (Rounds Played: {rounds})")
        print("-" * 30)

if __name__ == "__main__":
    play_game()
