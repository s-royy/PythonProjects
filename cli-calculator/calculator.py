def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    return a / b


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        print("\n--- Calculator ---")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
choice = input("Enter your choice (1-5): ").strip()

        if choice == "5":
            print("Thank you for using the calculator!")
            break

        if choice not in {"1", "2", "3", "4"}:
            print("Invalid choice. Try again.")
            continue

        num1 = get_float("Enter first number: ")
        num2 = get_float("Enter second number: ")

       if choice == "4" and num2 == 0:
            print("Division by zero is not allowed.")
            continue

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {result}")

        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {result}")

        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {result}")

        elif choice == "4":
            result = divide(num1, num2)
            print(f"Result: {result}")
