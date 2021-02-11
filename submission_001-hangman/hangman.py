#TIP: use random.randint to get a random word from the list
import random

def read_file(file_name):
    """
    TODO: Step 1 - open file and read lines as words
    """
    with open(file_name,"r") as i:
        k = i.readlines()
    
    return k


def select_random_word(words):
    """
    TODO: Step 2 - select random word from list of file
    """
    word = (words[random.randint (1, len(words))]) 
    random_letter = random.randint(1, len(word) - 2)
    string = (word[:random_letter] + "_" + word[random_letter+1:])
    print('Guess the word: ' + string )
    
    return word



def get_user_input():
    """
    TODO: Step 3 - get user input for answer
    """
    input ("Guess the missing letter: ")
    return 'TODO'


def run_game(file_name):
    """
    This is the main game code. You can leave it as is and only implement steps 1 to 3 as indicated above.
    """
    words = read_file(file_name)
    word = select_random_word(words)
    answer = get_user_input()
    print('The word was: '+word)


if __name__ == "__main__":
    run_game('short_words.txt')

