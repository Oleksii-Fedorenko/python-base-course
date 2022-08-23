import random

score = 2

while score >= 0:
    choices = ["rock", "paper", "scissors"]

    computer = random.choice(choices)
    player = None

    if score == 0:
        play_again = input("Let's try again bro? (yes/no): ").lower()
        if play_again == "yes":
            score = 2
        else:
            print("See you soon bro!")
            break

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()
    if player == computer:
        print("computer: ", computer)
        print("player: ", player)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose bro!")
            score -= 1
            print(f"Your score is {score} now")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You win bro!")
            score += 1
            print(f"Your score is {score} now")
    elif player == "scissors":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose bro!")
            score -= 1
            print(f"Your score is {score} now")
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You win bro!")
            score += 1
            print(f"Your score is {score} now")
    elif player == "paper":
        if computer == "rock":
            print("computer: ", computer)
            print("player: ", player)
            print("You win bro!")
        if computer == "scissors":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose bro!")
            score += 1
            print(f"Your score is {score} now")