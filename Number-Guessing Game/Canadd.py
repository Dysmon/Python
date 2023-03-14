import random

def is_valid(num, min_num, max_num):
    if num.isdigit():
        num = int(num)
        if min_num <= num <= max_num:
            return True
    return False


def Number_Guessing_Game():
    min_num = int(input("Enter the minimum number: "))
    max_num = int(input("Enter the maximum number: "))
    rand = random.randint(min_num, max_num)
    max_tries = 7
    difficulty = "normal"

    print(f"Welcome to the {difficulty} mode of Number-Guessing Game!")
    print(f"I'm thinking of a number between {min_num} and {max_num}. You have {max_tries} tries to guess it.")

    tries = 0

    for i in range(max_tries):
        x = input(f"Guess #{i+1}: ")
        if not is_valid(x, min_num, max_num):
            print(f"Invalid input. Please enter an integer between {min_num} and {max_num}.")
            continue
        x = int(x)
        tries += 1
        if rand > x:
            print('Your number is too low. Guess again.')
        elif rand < x:
            print('Your number is too high. Guess again.')
        else:
            print(f'Congratulations! You guessed it in {tries} tries.')
            break

    if tries == max_tries:
        print(f"Sorry, you've used up all your guesses. The number I was thinking of was {rand}.")

    again = input("Would you like to play again? (y/n) ")
    if again.lower() == "y":
        Number_Guessing_Game()
    else:
        print("Thanks for playing Number-Guessing Game.")

if __name__ == '__main__':
    print('Welcome to Number-Guessing Game')
    Number_Guessing_Game()