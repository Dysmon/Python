import random

cities = ['New York', 'Tokyo', 'Rio de Janeiro', 'Moscow', 'Paris', 'Cairo',
          'Barcelona', 'New Delhi', 'Toronto', 'Sydney', 'Shanghai', 'Berlin',
          'Mexico City', 'Rome', 'Cape Town', 'Lagos', 'BuenosAires', 'Seoul',
          'Bangkok', 'Lima', 'Chicago', 'Osaka', 'Salvador', 'St.Petersburg', 
          'Marseille', 'Alexandria', 'Madrid', 'Mumbai', 'Vancouver', 'Melbourne',
          'Beijing', 'Hamburg', 'Guadalajara', 'Naples', 'Durbann', 'Kano', 'Kuala Lumpur',
          'Belem', 'Munich', 'Kolkata', 'Calgary', 'Brisbane', 'Tianjin', 'Warsaw', 'Monterrey',
          'Bologna', 'Johannesburg', 'Budapest', 'Edmonton', 'Adelaide', 'Hangzhou', 'Frankfurt',
          'Montréal', 'Fukuoka', 'Manaus', 'Düsseldorf', 'Taipei', 'Havana', 'Recife', 'Kyoto',
          'Curitiba', 'Amsterdam', 'Giza', 'Nairobi', 'Jaipur', 'Nanjing', 'Denver', 'Athens',
          'Hyderabad', 'Seattle', 'Sapporo', 'Brasília', 'San Francisco', 'Portland', 'San Diego',
          'Minsk', 'Detroit', 'Fortaleza', 'Istanbul', 'San Antonio', 'Tijuana', 'Phoenix', 'Milan',
          'Luanda', 'San Jose', 'Dallas', 'Cincinnati', 'Cleveland', 'Pittsburgh', 'Minneapolis', 'Miami',
          'Tampa', 'Orlando', 'Charlotte', 'Austin', 'Nashville', 'New Orleans', 'Honolulu', 'Las Vegas', 'Los Angeles']


def get_word():
    word = random.choice(cities)
    return word.upper()

# function to get the current status
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, both legs
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # head, torso, both arms, one leg
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # head, torso, both arms
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # head, torso and one arm
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # head and torso
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # head
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # initial state
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]


def play(word):
    
    word_completion = '_' * len(word)
    print("Let's play guessing words!\n")
    tries = 6
    
    guessed = False
    guessed_letters = []
    guessed_words = []

    print(display_hangman(tries), word_completion, sep = "\n")
    
    while not guessed and tries > 0:
        answer = input("Enter a letter or word: ").upper()
        if answer in guessed_letters:
            print("You already guessed that letter!\n")
            continue
        elif answer in guessed_words:
            print("You already guessed that word!\n")
            continue
        if len(answer) == 1:
                guessed_letters.append(answer)
                if answer in word:
                    completion_list = list(word_completion)
                    for count,i in enumerate(word):
                        if answer == i:
                            completion_list[count] = answer
                        word_completion = "".join(completion_list)
                    if "_" not in word_completion:
                        guessed = True
        else:
            guessed_words.append(answer)
            if answer == word and answer.isalpha():
                guessed = True
                word_completion = word
        if answer not in word:
            tries -= 1
        print(display_hangman(tries), word_completion, sep = "\n")
    if guessed:
        print("Congratulations, you guessed the word!")    
    else:
        print(f"You lost all tries\nThe answer was {word}")
 
again = 'y'

while again.lower() == 'y':
    word = get_word()
    play(word)
    again = input("\nWould you like to play more?(y/n)\n")

