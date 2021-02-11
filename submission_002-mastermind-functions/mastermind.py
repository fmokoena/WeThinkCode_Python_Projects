import random
def generate_code():
    generate_code.__doc__ = "generates a random code"
    print('4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.')
    code = [0,0,0,0]
    for i in range(4):
        value = random.randint(1, 8) # 8 possible digits
        while value in code:
            value = random.randint(1, 8)  # 8 possible digits
        code[i] = value
    return code 

def get_user_input():
    get_user_input.__doc__ = "gets user input and returns it as answer"
    for i in range (0, 1):
        answer = input("Input 4 digit code: ")
        if len(answer) < 4 or len(answer) > 4:
            print("Please enter exactly 4 digits.")
            return get_user_input()
            continue
        return(answer)

def correct_digit(code, answer):
    correct_digit.__doc__ = "checks user input(answer) for correct digits and prints number of correct digits"
    correct_digits_and_position = 0
    correct_digits_only = 0
    for i in range(len(answer)):
        if code[i] == int(answer[i]):
            correct_digits_and_position += 1
        elif int(answer[i]) in code:
            correct_digits_only += 1

    print('Number of correct digits in correct place:     '+str(correct_digits_and_position))
    print('Number of correct digits not in correct place: '+str(correct_digits_only))
    return correct_digits_and_position

# TODO: Decompose into functions
def run_game():
    code = generate_code()
    correct = False
    turns = 1
    while not correct and turns <= 12:
        answer = get_user_input()
        correct_digits_and_position = correct_digit(code, answer)
        if correct_digits_and_position == 4:
            correct = True
            print('Congratulations! You are a codebreaker!')
        else:
            print('Turns left: '+str(12 - turns))
        turns += 1
    print('The code was: '+str(code))


if __name__ == "__main__":
    run_game()
