import random
import os
from colorama import init, Fore, Style

init(autoreset=True)

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_words(filename):
    with open(filename, 'r') as f:
        return [word.strip().lower() for word in f.readlines() if word.strip()]

def display_word(word, guessed):
    return " ".join([letter if letter in guessed else "_" for letter in word])

def print_banner():
    print(Fore.RED + Style.BRIGHT + """
  _    _            _                 _   _                                          
 | |  | |          | |               | | | |                                         
 | |__| | __ _  ___| | _____ _ __ ___| |_| |__   ___  _ __ ___   ___  __ _ _ __ ___  
 |  __  |/ _` |/ __| |/ / _ \ '__/ __| __| '_ \ / _ \| '_ ` _ \ / _ \/ _` | '_ ` _ \ 
 | |  | | (_| | (__|   <  __/ |  \__ \ |_| | | | (_) | | | | | |  __/ (_| | | | | | |
 |_|  |_|\__,_|\___|_|\_\___|_|  |___/\__|_| |_|\___/|_| |_| |_|\___|\__,_|_| |_| |_|
    """)
    print(Fore.CYAN + "Welcome to Hacker Hangman! Guess the cybersecurity word...\n")

def play_game():
    words = load_words("word_bank.txt")
    word = random.choice(words)
    guessed_letters = set()
    attempts = 6
    clear()
    print_banner()

    while attempts > 0:
        print(f"Word: {Fore.YELLOW}{display_word(word, guessed_letters)}")
        print(f"Guessed Letters: {Fore.CYAN}{' '.join(sorted(guessed_letters))}")
        print(f"Attempts Left: {Fore.RED}{attempts}")
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print(Fore.MAGENTA + "Invalid input. Enter one letter.")
            continue

        if guess in guessed_letters:
            print(Fore.BLUE + "You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(Fore.GREEN + "Correct!")
            if all(letter in guessed_letters for letter in word):
                print(Fore.GREEN + f"\nYou hacked the system! The word was '{word.upper()}'.")
                break
        else:
            print(Fore.RED + "Wrong!")
            attempts -= 1
    else:
        print(Fore.RED + f"\nGame Over. The word was '{word.upper()}'.")

    if input("\nPlay again? (y/n): ").lower() == 'y':
        play_game()

if __name__ == "__main__":
    play_game()
