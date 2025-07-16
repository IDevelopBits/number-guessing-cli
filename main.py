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

        # The return statements return the numbers of attempts the user should have
        if choice == 1:
            print("\nGreat! You have selected the Easy difficulty level."
            "\nLet's start the game!")
            return 10
        elif choice == 2:
            print("\nGreat! You have selected the Medium difficulty level."
                  "\nLet's start the game!")
            return 5
        elif choice == 3:
            print("\nGreat! You have selected the Hard difficulty level."
                  "\nLet's start the game!")
            return 3
        else:
            print("Invalid choice. Please try again.")

def get_guess(max_attempts):
    computer_guess = randint(1, 100)
    attempts = 1

    while True:
        if attempts > max_attempts:
            print(f"You lose! The computer guess was {computer_guess}.")
            break

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
    max_attempts = get_difficulty()
    get_guess(max_attempts)

if __name__ == "__main__":
    main()
    print("Thank you for playing!")



