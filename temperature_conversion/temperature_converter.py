def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit: float) -> float:
    return celsius_to_kelvin(fahrenheit_to_celsius(fahrenheit))


def kelvin_to_celsius(kelvin: float) -> float:
    return kelvin - 273.15


def kelvin_to_fahrenheit(kelvin: float) -> float:
    return celsius_to_fahrenheit(kelvin_to_celsius(kelvin))


def get_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def main():
    while True:
        print("\n--- Temperature Conversion Application ---")
        print("1. Celsius to Fahrenheit and Kelvin")
        print("2. Fahrenheit to Celsius and Kelvin")
        print("3. Kelvin to Celsius and Fahrenheit")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "4":
            print("Thank you for using Temperature Converter!")
            break

        if choice not in {"1", "2", "3"}:
            print("Invalid choice. Try again.")
            continue

        temperature = get_float("Enter the temperature value: ")

        if choice == "3" and temperature < 0:
            print("Kelvin cannot be negative.")
            continue

        if choice == "1":
            print(f"\n{temperature} Celsius equals:")
            print(f"{celsius_to_fahrenheit(temperature):.2f} Fahrenheit")
            print(f"{celsius_to_kelvin(temperature):.2f} Kelvin")

        elif choice == "2":
            print(f"\n{temperature} Fahrenheit equals:")
            print(f"{fahrenheit_to_celsius(temperature):.2f} Celsius")
            print(f"{fahrenheit_to_kelvin(temperature):.2f} Kelvin")

        elif choice == "3":
            print(f"\n{temperature} Kelvin equals:")
            print(f"{kelvin_to_celsius(temperature):.2f} Celsius")
            print(f"{kelvin_to_fahrenheit(temperature):.2f} Fahrenheit")


if __name__ == "__main__":
    main()
