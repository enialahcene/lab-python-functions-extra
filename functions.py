# functions.py

def get_unique_list_f(lst):
    """
    Takes a list as an argument and returns a new list with unique elements from the first list.
    """
    unique_set = set(lst)
    unique_list = list(unique_set)
    return unique_list

def count_case_f(string):
    """
    Returns the number of uppercase and lowercase letters in the given string.
    """
    uppercase_count = 0
    lowercase_count = 0

    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1

    return (uppercase_count, lowercase_count)

def remove_punctuation_f(sentence):
    """
    Removes all punctuation marks from a sentence.
    """
    import string
    translator = str.maketrans('', '', string.punctuation)
    sentence_without_punct = sentence.translate(translator)
    return sentence_without_punct

def word_count_f(sentence):
    """
    Counts the number of words in a given sentence after removing punctuation.
    """
    sentence_without_punct = remove_punctuation_f(sentence)
    words = sentence_without_punct.split()
    return len(words)