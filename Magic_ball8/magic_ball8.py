import random 

answers = ["Undoubtedly", "I think so", "It's not clear yet, try again", "Don't even think about it.",
           "Predetermined", "Most likely", "Ask later", "My answer is no.",
           "No doubt", "Good prospects", "Better not to tell", "Not according to me",
           "You can be sure of that", "Yes", "Concentrate and ask again", "Very doubtful."]

print("Hello World, I'm a magic orb, and I know the answer to any question you have.")

name = input("Print your name: \n")

print(f"Hello {name}")

while True:
    question = input("Ask me question\n")
    print(random.choice(answers))
    again = input("Would you like to play more?(y/n)\n")
    if again.lower() == 'n':
        print('Come back if you have any questions!')
        break
    