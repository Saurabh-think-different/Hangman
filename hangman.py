from words import get_hints, get_words
import random, time
import math
from colorama import init, Fore, Style


init()

print("\nWelcome to Custom-SAT-Hangman!\n")
name = input("Enter your name: ")

print(f'Hello {name}! Let\'s play Custom-SAT-Hangman!!\n')
time.sleep(1.5)
print("The Game begins in 3....2.....1.....GOGO, Best of Luck!!\n")

guess_words = get_words()
given_hint = get_hints()

def main():
    global already_guessed
    global limit
    global count
    global word
    global length_of_word
    global display
    global hint
    

    already_guessed = []
    limit = 5
    count = 0
    index = math.floor(random.random() * 300)
    word = guess_words[index].upper()
    length_of_word = len(word)
    display = '_ ' * length_of_word
    hint = given_hint[index]

def play_again():
    print(Fore.LIGHTCYAN_EX, "Do you want to play the game again to increase your English Proficiency? y = yes, n = no ")
    print(Style.RESET_ALL)
    ynYN = input().upper()
    if ynYN not in ['Y','N']:
        print(Fore.RED, "Enter valid iput please...\n")
        play_again()
    elif ynYN == 'Y':
        main()
        hangman()
    elif ynYN == 'N':
        print(Fore.GREEN, "Thanks for playing Custom-SAT-Hangman, We hope you'll come back again\n")
        exit()


def hangman():
    global display 
    global count
    
    print(f'This is the Hint: {hint.capitalize()}\n')
    print(f'       The word : {display}')
    # print(word, hint)
    print(f'    Guessed letters = {already_guessed}')
    print("You've Got ", end="");print(Fore.CYAN, limit-count,end="");print(Style.RESET_ALL,end="");print(" chances")
    guess = input('Your guess: ').upper()
    if guess == "EXIT":
        exit()
        
    if guess<'A' or guess>'Z' or len(guess)>1:
        print(Fore.YELLOW, f'Enter Valid Inputs plz\n')
        print(Style.RESET_ALL)
        hangman()
    elif guess in word:
        if guess in display:
            print(Fore.BLUE, "You already guessed this... Guess another letter\n")
            print(Style.RESET_ALL)
            hangman()
        for i in range(len(word)):
            if(word[i] == guess):
                display = display[:i*2]+guess+display[i*2+1:]
        

    else:
        
        if guess in already_guessed:
            print(Fore.BLUE, "You already guessed this... Guess another letter\n")
            print(Style.RESET_ALL)
            hangman()

        count += 1
        already_guessed.append(guess)

        if count == 1:
            time.sleep(1)
            print("    _____ \n"
                  "   |      \n"  
                  "   |      \n"  
                  "   |      \n"  
                  "   |      \n"  
                  "   |      \n"
                  " __|__\n"  
            )
            print(Fore.RED, " Wrong Guess Daa...\n Okay... You have ",end="")
            print(Fore.WHITE ,str(limit-count), end="")
            print(Fore.RED," lives remaining\n GO GET 'EM\n")
            print(Style.RESET_ALL)
            
        elif count == 2:
            time.sleep(1)
            print("    _____ \n"
                  "   |     | \n"  
                  "   |      \n"  
                  "   |      \n"  
                  "   |      \n"  
                  "   |      \n"
                  " __|__\n"  
            )
            print(Fore.RED, " Shizzz bro Wrong again...\n Okay... You have ",end="")
            print(Fore.WHITE , str(limit-count), end="")
            print(Fore.RED," lives remaining\n GO GET 'EM\n")
            print(Style.RESET_ALL)
        elif count == 3:
            time.sleep(1)
            print("    _____ \n"
                  "   |     | \n"  
                  "   |     | \n"  
                  "   |      \n"  
                  "   |      \n"  
                  "   |      \n"
                  " __|__\n"  
            )
            print(Fore.RED, " Broooooo Wrong again...\n Okay... You have ",end="")
            print(Fore.WHITE , str(limit-count), end="")
            print(Fore.RED," lives remaining\n GO GET 'EM\n")
            print(Style.RESET_ALL)

        elif count == 4:
            time.sleep(1)
            print("    _____ \n"
                  "   |     | \n"  
                  "   |     | \n"  
                  "   |     o \n"  
                  "   |      \n"  
                  "   |      \n"
                  " __|__\n"  
            )
            print(Fore.RED, " OMG Thin Ice Brotha\n Okay... You have ",end="" )
            print(Fore.WHITE , str(limit-count), end="")
            print(Fore.RED," lives remaining\n GO GET 'EM\n")
            print(Style.RESET_ALL)
        elif count == 5:
            time.sleep(1)
            print("    _____ \n"
                  "   |     | \n"  
                  "   |     | \n"  
                  "   |     o \n"  
                  "   |    /|\ \n"  
                  "   |    / \ \n"
                  " __|__\n"  
            )
            print(Fore.RED, " DEADDDDD\n You have ",end="")
            print(Fore.WHITE, str(limit-count), end="")
            print(Fore.RED, " lives remaining\n")
            print(Fore.LIGHTYELLOW_EX, f" The correct word was: {word}\n")
            print(Style.RESET_ALL)
            play_again()
    
    if display.find('_') == -1:
        print(f'This is the Hint: {hint.capitalize()}\n')
        print(f'       The word : {display}')
        print("Congrats! You are the winner!!! You guessed the word in " + str( length_of_word + count ) + " guesses.\n")
        play_again()
    
    elif count!=limit:
        hangman()

def play_hangman():
    main()
    hangman()
    

play_hangman()




