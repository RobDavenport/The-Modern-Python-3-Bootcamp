import random

while True:
    choice = -1
    random_number = random.randint(1, 10)

    while not choice == random_number:
        print("Pick a number between 1 and 10: ")
        choice = input()
        choice = int(choice)

        if (choice > random_number):
            print("Too high!")
        elif(choice < random_number):
            print("Too low!")
        else:
            break

    print("You guessed it!")
    print("Play again? y/n")
    playAgain = input()

    if (playAgain == "n"):
        print("Bye.")
        break