import random

def code_guess():
    try :
        number = int(input("Input 4 digit code: "))
        guess = str(number)
        if len(guess) == 4 :
            return guess
        else:
            print("Please enter exactly 4 digits.")
            return code_guess()
    except:
        print("Please enter exactly 4 digits.")
        return code_guess()

def correct_digits(code, guess):
    b, c = 0, 0 

    for i in range (0, len(code)):
        if code[i] == guess[i] :
           c+=1
    print("Number of correct digits in correct place:    ",c)

    for i in range(0, len(code)):
        if guess[i] in code and guess[i] != code[i]:
            b+=1
    print("Number of correct digits not in correct place:", b) 

    

def run_game():
    
#def random_code():
    digits = str(random.randint(1 ,8)) + str(random.randint(1 ,8)) + str(random.randint(1 ,8))+ str(random.randint(1 ,8))
    code = str(digits)
    print("4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.")
    #print(code)
    #return code

    guess = code_guess()

    """
    TODO: implement Mastermind code here
    """

    number_guesses = 12
    while (number_guesses > 1 and code != guess):
        correct_digits(code, guess)
        print("Turns left:", number_guesses-1)
        guess = code_guess()
        number_guesses -= 1 
    if guess == code :
        correct_digits(code, guess)
        print("Congratulations! You are a codebreaker!\nThe code was:", code) 
         

if __name__ == "__main__":
    #code = random_code()
    #guess = code_guess()
    run_game()
    