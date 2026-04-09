import random


def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        print("\n--- Number Guessing Game ---")
        print("1. Play")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ").strip()

        if choice == "2":
            print("Goodbye!")
            break

        if choice != "1":
            print("Invalid choice.")
            continue

        number = random.randint(1, 100)
        attempts = 0

        print("\nGuess a number between 1 and 100")

        while True:
            guess = get_int("Enter your guess: ")
            attempts += 1

            if guess < number:
                print("Too low")
            elif guess > number:
                print("Too high")
            else:
                print(f"Correct! You guessed it in {attempts} attempts")
                break


if __name__ == "__main__":
    main()
