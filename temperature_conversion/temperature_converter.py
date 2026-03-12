def celsius_to_fahrenheit(celsius: float) -> float:
    return (celsius * 9 / 5) + 32


def celsius_to_kelvin(celsius: float) -> float:
    return celsius + 273.15


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def fahrenheit_to_kelvin(fahrenheit: float)
-> float:
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
