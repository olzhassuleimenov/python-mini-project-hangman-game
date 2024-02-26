# My Mini-Project : Hangman Game
# Started : 10/01/2024
# End : 11/01/2024


import json
import random
from functions import hide_random_letters

print(" 'Welcome to Hangman Game from JasGame' ")
print(" 'start' ")
print(" 'about' ")
print(" 'exit' ")

while True :
    command = input("> ")

    # Start
    if command == "start" :
        print(" 1. 'Cars' ")
        print(" 2. 'Films' ")
        choice = int(input("Choose a category: "))
        if choice == 1 :
            with open('cars.json', 'r') as f:
                cars = json.load(f)
            random_car = random.choice(cars)["word"]
            hidden_car = hide_random_letters(random_car)
            print(hidden_car)
            letters_list = list(random_car)
            max_tries = 3
            current_try = 0

            while "_" in hidden_car and current_try < max_tries :
                letter = input("Guess a letter: ")
                correct_guess = False

                for i in range(len(hidden_car)) :
                    if hidden_car[i] == "_" and letter == letters_list[i] :
                        hidden_car = hidden_car[:i] + letter + hidden_car[i + 1:]
                        correct_guess = True

                if correct_guess :
                    print("Your answer is correct")
                    print(hidden_car)
                else :
                    current_try += 1
                    print(f"Try again, Tries {current_try}/{max_tries}")

            if "_" not in hidden_car :
                print("Congratulations! You guessed the word:", hidden_car)
                print(" 'start' ")
                print(" 'about' ")
                print(" 'exit' ")
            else :
                print("Sorry, you've run out of tries. The correct word was:", random_car)
                print(" 'start' ")
                print(" 'about' ")
                print(" 'exit' ")     

        elif choice == 2 :
            with open('films.json', 'r') as f:
                films = json.load(f)
            random_film = random.choice(films)["film"]
            hidden_film = hide_random_letters(random_film)
            print(hidden_film)
            letters_list = list(random_film)
            max_tries = 3
            current_try = 0

            while "_" in hidden_film and current_try < max_tries :
                letter = input("Guess a letter: ")
                correct_guess = False

                for i in range(len(hidden_film)) :
                    if hidden_film[i] == "_" and letter == letters_list[i] :
                        hidden_film = hidden_film[:i] + letter + hidden_film[i + 1:]
                        correct_guess = True

                if correct_guess :
                    print("Your answer is correct")
                    print(hidden_film)
                else :
                    current_try += 1
                    print(f"Try again, Tries {current_try}/{max_tries}")

            if "_" not in hidden_film :
                print("Congratulations! You guessed the word:", hidden_film)
                print(" 'start' ")
                print(" 'about' ")
                print(" 'exit' ")
            else :
                print("Sorry, you've run out of tries. The correct word was:", random_film)
                print(" 'start' ")
                print(" 'about' ")
                print(" 'exit' ")

    # About
    if command == "about" :
        print(" ' JasGame company ' ")
        print(" ' The Creator is : Olzhas Suleimenov ' ")
        print(" ' If you have Questions, contact me : '")
        print(" ' suleimenovvv840@gmail.com ' ")

    # Exit
    if command == "exit" :
        break