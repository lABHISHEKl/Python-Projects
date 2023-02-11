import random
computer_count=0
player_count=0
while True:
    choices = ["rock", "paper", "scissors"]
    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("Rock, paper or Scissors? : ").lower()

    if player== computer:
        print("Computer: ", computer)
        print("Player: ", player)
        print("Tie")

    elif player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose")
            computer_count += 1
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win")
            player_count += 1

    elif player == "scissors":
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose")
            computer_count += 1
        if computer == "paper":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win")
            player_count += 1

    elif player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You lose")
            computer_count += 1
        if computer == "rock":
            print("Computer: ", computer)
            print("Player: ", player)
            print("You win")
            player_count += 1
    playagain = input("Play Again (Y/N): ").lower()

    if playagain != "y":
        break
print("Computer score: ", computer_count)
print("You score: ", player_count)
print("End")


