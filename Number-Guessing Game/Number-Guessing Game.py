import random

def is_valid(num):
    if num.isdigit():
        num = int(num)
        if min_num <= num <= max_num:
            return True
    return False


def Number_Guessing_Game(min_num, max_num):
    """
    Main function to run the Number-Guessing Game.
    """
    rand = random.randint(min_num, max_num)
    
    x = input(f'Enter an integer between {min_num} and {max_num}:\n')

    tries = 0

    while True:
        if not is_valid(x):
             x = input(f"Invalid input. Please enter an integer between {min_num} and {max_num}.\n")
             continue
        else:
            x = int(x)
            if rand > x:
                 x = input('Your number is too low. Guess again.\n')
            elif rand < x:
                 x = input('Your number is too high. Guess again.\n')
            else:
                tries += 1
                print(f"Congratulations! You guessed it in {tries} tries")
                break
        tries += 1
    
    again = input("Would you like to play more?(y/n)\n")
    
    if again.lower() == "y":
        min_num = int(input("Enter the minimum number: "))
        max_num = int(input("Enter the maximum number: "))
        Number_Guessing_Game(min_num, max_num)
    else:
        print("Thanks for playing Number-Guessing Game. Goodbye!")

if __name__ == '__main__':
    min_num = int(input("Enter the minimum number: "))
    max_num = int(input("Enter the maximum number: "))
    Number_Guessing_Game(min_num, max_num)