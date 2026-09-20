import random

print("=" * 35)
print("      ROCK PAPER SCISSORS")
print("=" * 35)

# Number of rounds
while True:
    try:
        rounds = int(input("Enter number of rounds: "))

        if rounds > 0:
            break
        else:
            print(" Number of rounds must be greater than 0.")

    except ValueError:
        print(" Please enter a valid number.")

# Player name
while True:
    player = input("Enter your name: ").strip()

    if player:
        break
    else:
        print(" Name cannot be empty.")

computer = "Computer"

# Scores
player_score = 0
computer_score = 0

choices = ["rock", "paper", "scissors"]

# Game
for round_number in range(1, rounds + 1):

    print(f"\n{'=' * 12} ROUND {round_number} {'=' * 12}")

    # Player choice
    while True:
        player_choice = input(
            f"{player}, choose rock, paper, or scissors: "
        ).lower().strip()

        if player_choice in choices:
            break
        else:
            print(" Invalid choice! Please choose rock, paper, or scissors.")

    # Computer choice
    computer_choice = random.choice(choices)

    print(f"\n{player} chose: {player_choice}")
    print(f"{computer} chose: {computer_choice}")

    # Determine winner
    if player_choice == computer_choice:

        print(" It's a DRAW!")

    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or
        (player_choice == "paper" and computer_choice == "rock")
        or
        (player_choice == "scissors" and computer_choice == "paper")
    ):

        print(f" {player} wins this round!")
        player_score += 1

    else:

        print(f" {computer} wins this round!")
        computer_score += 1

    # Score
    print("\n---------- SCORE ----------")
    print(f"{player}: {player_score}")
    print(f"{computer}: {computer_score}")
    print("---------------------------")


# Final result
print("\n" + "=" * 35)
print("          FINAL RESULT")
print("=" * 35)

print(f"{player}: {player_score}")
print(f"{computer}: {computer_score}")

if player_score > computer_score:
    print(f"\n {player} IS THE WINNER!")

elif computer_score > player_score:
    print(f"\n {computer} IS THE WINNER!")

else:
    print("\n THE MATCH IS A DRAW!")

print("\n Thanks for playing!")