from os import system, name
from random import randint
from warnings import catch_warnings

#This global variable is used when the needed text file cannot be access for 
#whatever reason (moved, removed, name changed, etc).
back_up = ['Failed', 'Malfunction', 'blunder']

#This global variable holds all chars that have been guessed.
guessed_chars = []

#This global variable draws the hangman figure.
figure = '\n\n\n\n\n_______'

#This global variable is the message displayed to the user letting them know how
#they are doing.
message = 'Good Luck!!!'

def clear():
    '''Clears the Terminal of all text.'''

    if name == 'nt': #Windows
        _ = system('cls')
    else: #Mac/Linux
        _ = system('clear')


def game_over(answer):
    '''Lets the user know the game is over. Then terminates the program.
    Parameter:
        answer (str): The chosen word that needed to be guessed.'''

    clear()
    print("Sorry, you're out of guesses. ")
    print(figure)
    print(f"The word was: {answer}")
    exit()


def game_won(answer):
    '''Lets the user know they've won by correctly guessing the word.
    Parameter:
        answer (str): The chosen word that was guessed correctly.'''

    clear()
    print(f"Congratulations! You've completed the word.")
    print(figure)    
    print(f"The word is: {answer}")


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


def get_guess(chosen_word):
    '''Prompts the user to make a guess.
    Parameter:
        chosen_word (str): The censored word that the user is trying to guess.
    Returns:
        String: The guess made by the user.'''

    clear()
    print(message)
    print(figure)
    return input(f"The word is: {chosen_word}. \nGuess the missing letter: ")


def validate_guess(guess):
    '''Checks if the guess made is a aplhabet character. Or if the user typed
    exit to stop playing, if this is the case the program will terminate.
    Parameters:
        guess (str): the character / string to be validated.
    Returns:
        Boolean: True if the guess is a valid char,
                 False if the guess is an invalid char.'''

    try:
        if ((ord(guess) > 64 and ord(guess) < 91) or 
        (ord(guess) > 96 and ord(guess) < 123)):
            return True
        else:
            return False
    except TypeError:
        if guess == "exit":
            exit()
        else:
            return False


def fill_in_char(answer, hidden_word, char):
    '''Fills in the missing characters of the hidden word with the correctly 
    guessed character.
    Parameters:
        answer (str): The visable chosen word.
        hidden_word (str): The censored chosen word.
        char (char): The correctly guessed character.
    Returns:
        string: The new censored word with the correctly guessed char made 
                visable.'''

    for x in range(len(answer)):
        if char == answer[x]:
            hidden_word = hidden_word[:x] + char + hidden_word[x+1:]
    return(hidden_word)


def add_guessed(char):
    ''' Adds the given char to the guessed_char list.
    Parameters:
        char (char): The given char to be added.'''

    global guessed_chars
    
    guessed_chars.append(char)


def draw_figure(number):
    '''Keeps adding more to the hangman figure depending on the number of 
    guesses the user has left
    Parameter:
        number (int): The number of guesses left.
    Returns:
        string: The current state of the hangman figure.'''

    if number == 4:
        return('\n/----\n|\n|\n|\n|\n_______')
    elif number == 3:
        return('\n/----\n|   0\n|\n|\n|\n_______')
    elif number == 2:
        return('\n/----\n|   0\n|   |\n|   |\n|\n_______')
    elif number == 1:
        return('\n/----\n|   0\n|  /|\\\n|   |\n|\n_______')
    elif number == 0:
        return('\n/----\n|   0\n|  /|\\\n|   |\n|  / \\\n_______')


def run_game(hidden_word, answer):
    ''' Handles the loop for getting/validating guesses untill the game is won,
    lost, or the user quits.'''

    global message
    global figure

    guesses_left = 4
    while hidden_word != answer:
        if guesses_left < 0:
            game_over(answer)
        
        guess = get_guess(hidden_word).lower()

        if validate_guess(guess):
            print("valid")
            if (guess in list(answer)) and (guess not in list(hidden_word)):
                print("1")
                message = 'Correct!'
                hidden_word = fill_in_char(answer, hidden_word, guess)
                guessed_chars.append(guess)
            elif (guess not in guessed_chars) and (guess not in list(answer)):
                print("2")
                message = (f'Wrong! Number of guesses left: {guesses_left}')
                figure = draw_figure(guesses_left)
                guesses_left -= 1
                guessed_chars.append(guess)
            else:
                message = "That letter was already guessed! try again."           
    else:
        game_won(answer)


if __name__ == "__main__":
    clear()
    print("Welcome to Hangman. \nYou can type 'exit' at anytime to leave.")
    
    words_file = select_difficulty()
    words_list = read_file(words_file)
    chosen_word = choose_word(words_list)
    hidden_word = hide_chars(chosen_word)

    run_game(hidden_word, chosen_word)