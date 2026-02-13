import random

def choose_difficulty():
    print("\nSelect Difficulty Level:")
    print("1. Easy (1 - 10)")
    print("2. Medium (1 - 50)")
    print("3. Hard (1 - 100)")

    while True:
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            return 1, 10
        elif choice == "2":
            return 1, 50
        elif choice == "3":
            return 1, 100
        else:
            print("Invalid choice. Please select 1, 2, or 3.")


def play_game():
    lower, upper = choose_difficulty()
    secret_number = random.randint(lower, upper)
    attempts = 0

    print(f"\nI have selected a number between {lower} and {upper}. Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < secret_number:
                print("Too low! Try a higher number.")
            elif guess > secret_number:
                print("Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                return attempts

        except ValueError:
            print("Please enter a valid number.")


def main():
    best_score = None

    while True:
        attempts = play_game()

        if best_score is None or attempts < best_score:
            best_score = attempts
            print("🏆 New Best Score!")

        print(f"Best (lowest) attempts so far: {best_score}")

        replay = input("\nDo you want to play again? (yes/no): ").lower()
        if replay != "yes":
            print("Thanks for playing! 👋")
            break


if __name__ == "__main__":
    main()
