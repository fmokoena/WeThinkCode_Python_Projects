import random

def create_outline():
    """
    TODO: implement your code here
    """
    topics = sorted( set(("Introduction to Python", "Tools of the Trade", "How to make decisions", "How to repeat code", "How to structure data", "Functions", "Modules")))
    problems = list(("Problem 1,", "Problem 2,", "Problem 3"))
    student = [("Orm", "How to make decisions","[STARTED]"),("David","Tools of the Trade","[GRADED]"),("Jotaro","How to repeat code","[COMPLETED]")]
    MP = {}


    print("Course Topics:")
    for i in (topics):
        print("*", i)
      
    print("Problems:")
    for i in (topics):
        MP[i] = problems
    for key, value in  MP.items():
        print(f'* {key} : ',end='')
        print(*value)

    print("Student Progress:")
    j = 1
    for c in student :
        r = random.randint(0, 2)
        print(str(j)+". " + c[0] +" - " + c[1] + " - "+ problems[r] + " " +c[2])
        j+=1

if __name__ == "__main__":
    create_outline()
