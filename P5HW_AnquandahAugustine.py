#Generating a Math driven Quiz with random numbers.
#05/04/2023
#CTI-110 P5HW-Math Quiz
#Anquandah Augustine


import random

def display_menu():
    print("Welcome to Math Quiz")
    print()
    print("MAIN MENU")
    print("-------------------")
    print("1. Add Random Numbers")
    print("2. Subtracting Random Numbers")
    print("3. Exit")

def add_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    total = num1 + num2
    guess = None
    num_guesses = 0
    while guess != total:
        num_guesses += 1
        guess = int(input(f" {num1}\n+{num2}\n "))
        if guess == total:
            print(f"Congratulations!!!! Your answer is correct. {num_guesses} guesses.")
        elif guess < total:
            print("Sorry, guess too low")
            print("Try again: ")
        else:
            print(" Sorry guess too high. ")
            print("Try again:")

def subtract_numbers():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    difference = num1 - num2
    guess = None
    num_guesses = 0
    while guess != difference:
        num_guesses += 1
        guess = int(input(f"What is {num1} - {num2}? "))
        if guess == difference:
            print("Congratulations!!!!Your answer is correct.")
            print(f"Number of guesses {num_guesses} ")    
        elif guess < difference:
            print("Sorry, guess is too low. Try again:")
        else:
            print("Sorry, guess is too high. Try again:")

def main():
    while True:
        display_menu()
        choice = input("Please choose one of the menu options: ")
        if choice == "1":
            add_numbers()
      
        elif choice == "2":
            subtract_numbers()
        elif choice == "3":
            print("Thank you for playing...")
            print("Bye!!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
