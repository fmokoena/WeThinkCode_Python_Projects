import random


def read_file(file_name):
    file = open(file_name,'r')
    words = file.readlines()
    file.close()
    return words


def get_user_input():
    char = input("Guess the missing letter: ")
    return char
        
    


def ask_file_name():
    file_name = input("Words file? [leave empty to use short_words.txt] : ")
    if not file_name:
        return 'short_words.txt'
    return file_name


def select_random_word(words):
    random_index = random.randint(0, len(words)-1)
    word = words[random_index].strip()
    original_word = word
    return original_word


# TODO: Step 1 - update to randomly fill in one character of the word only
def random_fill_word(word):
    random_index = random.randint(0, len(word)-1)
    s = ("_"* (random_index) + word[random_index]+"_"* ((len(word)-1)-random_index))
    return s

# TODO: Step 1 - update to check if character is one of the missing characters
def is_missing_char(original_word, answer_word, char):
    for i in range (0, len(original_word)):
        if char == original_word[i] and original_word[i] != answer_word[i]:
            return True
    
    return False


# TODO: Step 1 - fill in missing char in word and return new more complete word
def fill_in_char(original_word, answer_word, char):
    for i in range(0, len(original_word)):
        if char == original_word[i]:
            L = list(answer_word)
            L[i] = char
            answer_word = "".join(L)
    return answer_word

def do_correct_answer(original_word, answer, guess):
    answer = fill_in_char(original_word, answer, guess)
    print(answer)
    return answer


# TODO: Step 4: update to use number of remaining guesses
def do_wrong_answer(word, answer, number_guesses):
    print('Wrong! Number of guesses left: '+str(number_guesses))
    return draw_figure(number_guesses)


# TODO: Step 5: draw hangman stick figure, based on number of guesses remaining
def draw_figure(number_guesses):
    x = "\\"  
    if number_guesses == 4:
        print("/----\n"+ "|\n"*4 +"_"*7)
    elif number_guesses == 3:
       print("/----\n"+"|"+" "*3 +"0\n"+"|\n"*3 +"_"*7)
    elif number_guesses == 2:
        print("/----\n"+"|"+" "*3 +"0\n"+("|"+" "*3+"|\n")*2+"|\n" +"_"*7)
    elif number_guesses == 1:
        print("/----\n"+"|"+" "*3 +"0\n"+("|"+" "*2+"/|" + x + "\n")+ "|"+" "*3+"|\n"+"|\n" +"_"*7)
    elif number_guesses == 0:
        print("/----\n"+"|"+" "*3 +"0\n"+("|"+" "*2+"/|"+ x +"\n")+ "|"+" "*3+"|\n"+("|"+" "*2+"/ "+ x + "\n")+"_"*7)
       
        
        #print('TODO')

# TODO: Step 2 - update to loop over getting input and checking until whole word guessed
# TODO: Step 3 - update loop to exit game if user types `exit` or `quit`
# TODO: Step 4 - keep track of number of remaining guesses
def run_game_loop(word, answer):
    print("Guess the word: "+ answer)
    number_guesses = 4 
    while number_guesses > 0 and answer != word:
        guess = get_user_input()
        if is_missing_char(word, answer, guess) == True:
            answer = do_correct_answer(word, answer, guess)
        elif guess.lower() == "exit" or guess.lower() == "quit":
            print("Bye!")
            return(0)
        else:
            do_wrong_answer(word, answer, number_guesses)
            number_guesses = number_guesses - 1
            print(answer)
    if number_guesses == 0:
        print ("Sorry, you are out of guesses. The word was: "+ word)

# TODO: Step 6 - update to get words_file to use from commandline argument
if __name__ == "__main__":
    words_file = ask_file_name()
    words = read_file(words_file)
    selected_word = select_random_word(words)
    current_answer = random_fill_word(selected_word)
    run_game_loop(selected_word, current_answer)