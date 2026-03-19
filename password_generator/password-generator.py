import random
import string


def generate_password(length: int, use_digits: bool, use_symbols: bool) -> str:
    characters = string.ascii_letters
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))


def get_int(prompt: str) -> int:
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Enter a positive number.")
        except ValueError:
            print("Please enter a valid number.")


def get_choice(prompt: str) -> bool:
    while True:
        choice = input(prompt).strip().lower()
        if choice in {"y", "yes"}:
            return True
        if choice in {"n", "no"}:
            return False
        print("Enter yes or no.")


def main():
    while True:
        print("\n--- Password Generator ---")
        print("1. Generate Password")
        print("2. Exit")

        choice = input("Enter your choice (1-2): ").strip()

        if choice == "2":
            print("Goodbye!")
            break

        if choice != "1":
            print("Invalid choice.")
            continue

        length = get_int("Enter password length: ")
        use_digits = get_choice("Include digits? (yes/no): ")
        use_symbols = get_choice("Include symbols? (yes/no): ")

        password = generate_password(length, use_digits, use_symbols)
        print(f"\nGenerated Password: {password}")


if __name__ == "__main__":
    main()
