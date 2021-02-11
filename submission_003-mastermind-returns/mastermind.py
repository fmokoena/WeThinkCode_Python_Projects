import random

def create_code():
    """Function that creates a 4 digit code, using random digits from 1 to 8"""
    code = [0, 0, 0, 0]

    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    #print (code)
    return code


def show_instructions():
    """Shows the game instructions to the user"""

    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')


def show_results(code, answer):
    """Shows the results of one turn"""
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

    print('Number of correct digits in correct place:     ' + str(correct_digits_and_position))
    print('Number of correct digits not in correct place: ' + str(correct_digits_only))
    return (correct_digits_and_position)


def get_answer_input():
    """ gets input from the user/player """
    answer = input("Input 4 digit code: ")
    while len(answer) < 4 or len(answer) > 4:
        print("Please enter exactly 4 digits.")
        answer = input("Input 4 digit code: ")
    return answer


def show_code(code):
    """Shows the Code that was created to the user"""
    print('The code was: '+str(code))


def check_correctness(turns, correct_digits_and_position):
    """Checks the correctness of the answer and shows output to the user"""
    correct = False
    if correct_digits_and_position == 4:
        correct = True
        print('Congratulations! You are a codebreaker!')
        return correct
    else:
        take_turn(turns)
        

def take_turn(turns):
     """Handles the logic of taking a turn, which includes:
     * getting an answer from the user
     * checking if the answer is valid
     * checking the correctness of the answer
    """
     print('Turns left: ' + str(11 - turns))

def run_game():
    """The Main function for running the game"""
    correct = False

    code = create_code()
    show_instructions()

    turns = 0
    while not correct and turns < 12:
        answer = get_answer_input()
        correct_digits_and_position = show_results(code, answer)
        correct = check_correctness(turns, correct_digits_and_position)
        turns += 1
       
    show_code(code)


if __name__ == "__main__":
    run_game()
