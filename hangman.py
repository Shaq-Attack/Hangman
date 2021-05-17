from os import system, name
from random import randint
from warnings import catch_warnings

#This global variable is used when the needed text file cannot be access for 
#whatever reason (moved, removed, name changed, etc).
back_up = ['Failed', 'Malfunction', 'blunder']

#This global variable holds all chars that have been guessed, and the one char
#that was initailly made visible.
guessed_chars = []

def clear():
    '''Clears the Terminal of all text.'''

    if name == 'nt': #Windows
        _ = system('cls')
    else: #Mac/Linux
        _ = system('clear')


def valid_guess(guess):
    '''Checks if the guess made is a aplhabet character.
    Parameters:
        guess (char): the character to be validated.
    Returns:
        Boolean: True if the guess is a valid chars
                 False if the guess is an invalid chars.'''
    try:
        if ((ord(guess) > 64 and ord(guess) < 91) or 
        (ord(guess) > 96 and ord(guess) < 123)):
            return True
        else:
            return False
    except TypeError:
        return False


def add_guessed(word):
    ''' Adds all alphabet chars in the given word to the guessed_char list.
    Parameters:
        word (str): The given word to check for alphabet chars.'''
    global guessed_chars
    
    for sub_char in word:
        if not any(sub_char in char for char in guessed_chars):
            guessed_chars.append(sub_char)


def select_difficulty():
    '''Determines the difficulty of the words given based on the users choice
    Returns:
	    str: The text file to use based on the difficulty level chosen.'''

    while True:
        choice = input("Please select the difficulty \
between: easy, medium, or hard...\n\
Input choice [e/m/h]: ")

        if choice.lower() == 'e' or choice.lower() == 'easy':
            return('Easy.txt')
        elif choice.lower() == 'm' or choice.lower() == 'medium':
            return('Medium.txt')
        elif choice.lower() == 'h' or choice.lower() == 'hard':
            return('Hard.txt')
        else:
            print("Invalid choice. Please try again!")


def read_file(file_name):
    '''Reads the content of the given text file and creates a list of the words
    within it.
    Parameters:
        file_name (Text File): The text file to be read. 
    Return:
        List[str]: The list of words.'''
    try:
        file = open(file_name, 'r')
        words = file.readlines()
        file.close()
        return(words)
    except FileNotFoundError:
        return(back_up)


def choose_word(words_list):
    '''Selects and returns a random word from the given list of words.
    Parameters:
        words_list (List[str]): The list of words to chose from.
    Return 
        str: The random word chosen from the list.'''

    return(words_list[randint(0, len(words_list)-1)].strip())


def hide_chars(word):
    '''Selects a random character from the given string then replaces evey other
    character with an underscore (_).
    Parameters:
        word (str): The word/string we want to modify.
    Return
        str: The modified/censored word.'''

    letter = word[randint(0, len(word)-1)]
    ans = ''

    for x in range(len(word)):
        if letter == word[x]:
            ans += word[x]
        else:
            ans += '_'
    return(ans)


if __name__ == "__main__":
    clear()
    print("Welcome to Hangman.")
    
    words_file = select_difficulty()
    words_list = read_file(words_file)
    chosen_word = choose_word(words_list)
    hidden_word = hide_chars(chosen_word)

#     while hidden_word != choose_word:
#         guess = input(f"The word is: {chosen_word}.\n\
# Guess the missing letter: ")
#         while not valid_guess(guess):
