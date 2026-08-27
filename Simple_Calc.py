import time
from time import sleep
import sys


def show_ascii_calculator_animated():
    ascii_lines = [
        "  _____________________",
        " |  _________________  |",
        " | | Deez Calc :)    | |",
        " | |_________________| |",
        " |  ___ ___ ___   ___  |",
        " | | 7 | 8 | 9 | | + | |",
        " | |___|___|___| |___| |",
        " | | 4 | 5 | 6 | | - | |",
        " | |___|___|___| |___| |",
        " | | 1 | 2 | 3 | | * | |",
        " | |___|___|___| |___| |",
        " | | . | 0 | = | | / | |",
        " | |___|___|___| |___| |",
        " |_____________________|"
    ]
    for line in ascii_lines:
        print(line)
        sleep(0.15)  


print("=== Booting Calculator... ===")
sleep(1)
print("\nLoading modules...")
sleep(2)

show_ascii_calculator_animated()
sleep(1)
print("\n=== Calculator Ready ===\n")


while True:
    try:
        user_input = input("Enter first number (or 'q' to quit): ")
        if user_input.lower() == 'q':
            print("\nExiting Calculator. Goodbye!")
            break
        num1 = float(user_input)

        operator = input("\nEnter operator (+, -, *, /): ")
        num2_input = input("\nEnter second number: ")
        if num2_input.lower() == 'q':
            print("\nExiting Calculator. Goodbye!")
            break
        num2 = float(num2_input)

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("\nUhhhh...")
                sleep(2)
                print("\ndid you just try to divide by zero...\n")
                continue
        else:
            print("Error: Invalid operator.")
            continue

        print(f"Result: {result}\n")

    except ValueError:
        print("\nEnter a number!\n")
