# Haven't learned how to do python functions yet...

from random import choice

print("Welcome to Rock, Paper, Scissors!")

playerScore = 0
aiScore = 0

while playerScore < 3 and aiScore < 3:
    print("\nStarting a new round.")
    print(f"The score is Player with {playerScore} pts and the AI has {aiScore} pts.\n")

    playerChoice = input("Enter your choice: ").lower()

    aiChoice = choice(["rock", "paper", "scissors"])
    print("The AI threw " + aiChoice)

    if (playerChoice == "quit"):
        print("Quitting game...")
        break
    elif playerChoice == aiChoice:
        print("It's a draw!")
    elif (playerChoice == "rock" and aiChoice == "paper") or (playerChoice == "paper" and aiChoice == "scissors") or (playerChoice == "scissors" and aiChoice == "rock"):
        print("You lose!")
        aiScore += 1
    else:
        print("You win!")
        playerScore += 1

print("\nGame over!")
print(f"You ended the game with {playerScore} pts while the AI had {aiScore} pts.")

if playerScore > aiScore:
    print("Congrats! You won!")
elif playerScore == aiScore:
    print("It's a tie!")
else:
    print("Sorry! Better luck next time.")
