def celsius_to_fahrenheit(c: float) -> float:
    return c * 9 / 5 + 32


def fahrenheit_to_celsius(f: float) -> float:
    return (f - 32) * 5 / 9


def celsius_to_kelvin(c: float) -> float:
    return c + 273.15


def kelvin_to_celsius(k: float) -> float:
    return k - 273.15


if __name__ == "__main__":
    print("=== Temperature Converter ===")
    try:
        value = float(input("Enter temperature value: "))
        unit = input("Enter unit (C/F/K): ").strip().upper()

        if unit == "C":
            print(f"{value}°C = {celsius_to_fahrenheit(value):.2f}°F")
            print(f"{value}°C = {celsius_to_kelvin(value):.2f}K")
        elif unit == "F":
            print(f"{value}°F = {fahrenheit_to_celsius(value):.2f}°C")
        elif unit == "K":
            print(f"{value}K = {kelvin_to_celsius(value):.2f}°C")
        else:
            print("Unknown unit. Please use C, F, or K.")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
