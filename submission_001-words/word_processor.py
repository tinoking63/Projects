
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

words = "These are indeed interesting, an obvious understatement, times. What say you?"
def convert_to_word_list(text):
    '''
    It splits the text string at spaces, commas ,, semi-colons ;, question marks ? and points . into a list of words.
    Converts everything to lower case
    '''
    text = split(', . ? / \\ ! ; : {}',text.lower())
    if not text:
        return None
    else:
        return list(filter(None,text))




def words_longer_than(length, text):
    '''
    Finds the words that have a specific length
    '''
    new = convert_to_word_list(text)
    answer = list(map(lambda x: x, filter(lambda x: len(x) > length,new)))
    
    return(answer)



def words_lengths_map(text):
    '''
    Itreturns a dictionary (dict) that maps a word length, e.g. 3, to the number of words in the text of that length.
    '''
    new2 = convert_to_word_list(text)
    lst = sorted(list(map(lambda x : len(x), new2)))
    dictionary = {}

    for value in lst:
        dictionary[value] = lst.count(value)
    
    return(dictionary)


def letters_count_map(text):
    '''
    Shows how many times a letter shows up in the string.
    '''
    new2 = ''.join(convert_to_word_list(text))
    lst = list(map(lambda x : x, new2))
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    dictionary = {}

    for value in alphabet:
        dictionary[value] = lst.count(value)

    return(dictionary)


def most_used_character(text):
    '''
    Shows the the letter that appears the most in a string
    '''
    count = letters_count_map(text)
    bigger  = max(count, key=count.get)
    if not text:
        return None
    else:
        return (bigger)
