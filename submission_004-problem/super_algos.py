
def find_min(element):
    """Finds and returns the smallest value in a list of integers """
    try:
        if element == [] or element == " ":
            return(-1)
        else:
            if len(element) > 1:
                if element[0] > element[1]:
                    element.pop(0)
                    find_min(element)
                else:
                    element.pop(1)
                    find_min(element)
            number = str(element)[1:-1]
            minimum = int(number)
            #print(minimum)
            return (minimum) 
    except TypeError:
            return (-1)
            
       
def sum_all(elements):
    """adds all the values of a list of integers and returns the total""" 
    try:
        if elements == [] or elements == " ":
            return(-1)
        else:
            if len(elements) > 1:
                elements[1] = elements[0] + elements[1]
                elements.pop(0)
                sum_all(elements)
            value = str(elements)[1:-1]
            total = int(value)
            return total
    except TypeError:
        return(-1)


def find_possible_strings(character_set, n):
    """finds all possible combinations for a list of characters and returns them as strings of a given length in the form of a list of strings"""
    if character_set == " " or character_set == []:
        return([])
    else:
        try:
            return possible_strings_recursive(character_set, "", n, [])

        except TypeError:
            return([])


def possible_strings_recursive(character_set, prefix, n, strings):
    """ A Recursive function that creates a list with all possible combinations for a list of characters """
    if n == 0:
        strings.append(prefix)
        return 
            
    for i in range(len(character_set)):
        newprefix = prefix + character_set[i]
        possible_strings_recursive(character_set, newprefix, (n-1),strings)
   
    return strings


def main():
    """used to run functions"""
    #elements = [32,43,51,67]
    #element = [22,77,89,100]
    print(sum_all(elements))
    print(find_min(element))
    #character_set =["a","b"]
    #n = 2
    print(find_possible_strings(character_set,n))

if __name__ == "__main__":
    main()