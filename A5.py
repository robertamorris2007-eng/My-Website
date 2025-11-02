import random
import math


score = 0


def play_guessing_game():
    number = random.randint(1, 50)
    attempts = 0
    print("\nGuess the number between 1 and 50.")

    while True:
        guess = int(input("Your guess: "))
        attempts += 1

        if guess < number:
            print("Too low.")
        elif guess > number:
            print("Too high.")
        else:
            print(f"Correct! Attempts: {attempts}")
            global score
            score += 1
            break


def play_dice_battle():
    global score
    player_wins = 0
    computer_wins = 0

    for i in range(5):
        input("\nPress Enter to roll...")
        player = random.randint(1, 6) + random.randint(1, 6)
        computer = random.randint(1, 6) + random.randint(1, 6)

        print(f"You: {player}, Computer: {computer}")

        if player > computer:
            print("You win this round.")
            player_wins += 1
            score += 1
        elif computer > player:
            print("Computer wins this round.")
            computer_wins += 1
        else:
            print("Tie.")

    if player_wins > computer_wins:
        print("\nYou won the Dice Battle!")
    elif computer_wins > player_wins:
        print("\nComputer won the Dice Battle.")
    else:
        print("\nIt's a tie!")


def bonus_round():
    print("\nBONUS ROUND!")
    num = random.randint(1, 6)
    answer = math.factorial(num)
    guess = int(input(f"What is {num}! (factorial)? "))

    if guess == answer:
        print("Correct!")
        global score
        score += 2
    else:
        print(f"Wrong. The answer was {answer}.")


def view_score():
    print(f"\nCurrent Score: {score}")


def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Play Number Guessing")
        print("2. Play Dice Battle")
        print("3. View Score")
        print("4. Exit")
        choice = input("Choose: ")

        if choice == "1":
            play_guessing_game()
        elif choice == "2":
            play_dice_battle()
        elif choice == "3":
            view_score()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

        if score >= 5:
            bonus_round()


main_menu()
