
def split(delimiters, text):
    """
    Splits a string using all the delimiters supplied as input string
    :param delimiters:
    :param text: string containing delimiters to use to split the string, e.g. `,;? `
    :return: a list of words from splitting text using the delimiters
    """ 
    
    import re
    regex_pattern = '|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, text, 0)


def convert_to_word_list(text):
    """converts a string into a list of lowercased words"""
    text = text.lower()
    s_lit = split(". , ; : ? ", text)
    prop_split = list(filter(lambda x: False if x == '' else True ,s_lit))
    return prop_split

def words_longer_than(length, text):
    """returns only the words that are longer than the given length"""
    long_wordo = {}
    wordos = split(",;:? ", text)
    long_wordo = filter(lambda x : len(x) > length, wordos)
    long_wordos = list(long_wordo)
    return long_wordos


def words_lengths_map(text):
    """returns a dictionary with the lengths of every word and how many times that given length occurs"""
    s_lit = split(".,;:? ", text)
    wordos = list(filter(lambda x: False if x == '' else True ,s_lit))
    mp = {}
    mp = map(lambda x : len(x),wordos)
    ls = list(mp)
    l = set(ls)
    l_st = list(l)

    m_p = {}
    r_c = map(lambda x,y:ls.count(x) ,l_st,ls)
    m_p = list(r_c)
   
    mpp = dict(zip(l_st, m_p))
    return mpp
    
def letters_count_map(text):
    """returns a dictionary containing all the letters of the alphabet and how many times each letter occurs in a given string"""
    text = text.lower()
    wordos = split(",;:? ", text)
    letter =  list(str(wordos))
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    lsp = {}
    pb = map(lambda x:letter.count(x) ,alph)
    lsp = list(pb)
    a_phabet = dict(zip(alph, lsp))
    return a_phabet    

def most_used_character(text):
    """returns the most frequently occuring letter in a string"""
    import functools
    if text == '':
        return (None)
    else:
        a_phabet = letters_count_map(text)
        alfabet = a_phabet.values()
        hdp = functools.reduce(lambda a,b: a if a > b else b ,alfabet)
        
        ma_x = list(a_phabet.keys())[list(alfabet).index(hdp)]
        return(ma_x)

if __name__ == "__main__":
    convert_to_word_list(text)
    words_longer_than(length, text)
    words_lengths_map(text)
    letters_count_map(text)
    most_used_character(text)