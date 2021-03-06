"""
Target game for ukrainian language.
"""
import random


def generate_grid():
    """
    Generate a list of 5 unique letters of ukrainian alphabet.

    >>> random.seed(5)
    >>> generate_grid()
    ['м', 'т', 'б', 'щ', 'л']
    """
    alphabet = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    letters = []
    while len(letters) < 5:
        letter = random.choice(alphabet)
        if letter not in letters:
            letters.append(letter)
    return letters


def get_words(path, letters):
    """
    (str, list[str]) -> list[tuple]
    Return a list of all words that matches conditions and their parts of language.

    >>> get_words('base.lst', ['ь'])
    []
    """
    with open(path, 'r') as vocabulary:
        lines = vocabulary.readlines()
        words = []
        for line in lines:
            line = line.strip()
            add_condition = True
            if line[0] not in letters:
                add_condition = False
            line_lst = line.split()
            if len(line_lst[0]) > 5:
                add_condition = False
            if add_condition:
                if line_lst[1].startswith('intj') or line_lst[1].startswith('noninfl'):
                    add_condition = False
                elif line_lst[1].startswith('/n') or line_lst[1].startswith('n'):
                    value = 'noun'
                elif line_lst[1].startswith('/v') or line_lst[1].startswith('v'):
                    value = 'verb'
                elif line_lst[1].startswith('/adj') or line_lst[1].startswith('adj'):
                    value = 'adjective'
                elif line_lst[1].startswith('adv'):
                    value = 'adverb'
                if add_condition:
                    words.append((line_lst[0], value))
        return words


def check_user_words(user_words, language_part, letters, dict_of_words):
    """
    (list[str], str, list[str], list[tuple]) -> (list[str], list[str])
    Return a list of correct words and missing words.

    >>> check_user_words([], "verb", ['щ'], get_words("base.lst", ['щ']))
    ([], [])
    """
    correct_words = []
    missing_words = []
    dict_of_words = dict(dict_of_words)
    for word in user_words:
        correct_condition = True
        if word[0] not in letters:
            correct_condition = False
        if word not in dict_of_words:
            correct_condition = False
        else:
            if dict_of_words[word] != language_part:
                correct_condition = False
        if correct_condition:
            correct_words.append(word)
    for word in dict_of_words:
        if word not in correct_words and dict_of_words[word] == language_part:
            missing_words.append(word)
    return correct_words, missing_words


def results():
    """
    Run a game and print results.
    """
    letters = generate_grid()
    print(letters)
    language_part = random.choice(['noun', 'verb', 'adjective', 'adverb'])
    dict_of_words = get_words('base.lst', letters)
    user_words = input()
    user_words = user_words.split()
    correct_wrds, missing_wrds = check_user_words(user_words, language_part, letters, dict_of_words)
    print(correct_wrds)
    print(missing_wrds)
