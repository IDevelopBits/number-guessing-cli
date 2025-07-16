from random import randint

def welcome():
    print("Welcome to Number Guessing Game"
          "\nI'm thinking of a number between 1 and 100."
          "\nYou have a limited number of chances to guess the correct number\n")

    print("Please select a difficulty level:")
    print("1. Easy (10 Chances)"
          "\n2. Medium (5 Chances)"
          "\n3. Hard (3 Chances)")

def get_difficulty():
    choice = ""
    while True:
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            print("\nGreat! You have selected the Easy difficulty level."
            "\nLet's start the game!")
            break
        elif choice == 2:
            print("\nGreat! You have selected the Medium difficulty level."
                  "\nLet's start the game!")
            break
        elif choice == 3:
            print("\nGreat! You have selected the Hard difficulty level."
                  "\nLet's start the game!")
            break
        else:
            print("Invalid choice. Please try again.")

def get_guess():
    computer_guess = randint(1, 100)
    attempts = 1

    while True:
        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Invalid guess. Please try again.")
            continue

        if guess > computer_guess:
            print(f"Incorrect! The number is less than {guess}.")
            attempts += 1
        elif guess < computer_guess:
            print(f"Incorrect! The number is greater than {guess}.")
            attempts += 1

        if guess == computer_guess:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")

def main():
    welcome()
    get_difficulty()
    get_guess()

if __name__ == "__main__":
    main()
else:
    print("Thank you for playing!")



