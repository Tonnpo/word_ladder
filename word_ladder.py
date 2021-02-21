#!/bin/python3
from collections import deque
from copy import copy


def word_ladder(start_word, end_word, dictionary_file='words5.dict'):
    '''
    Returns a list satisfying the following properties:

    1. the first element is `start_word`
    2. the last element is `end_word`
    3. elements at index i and i+1 are `_adjacent`
    4. all elements are entries in the `dictionary_file` file

    For example, running the command
    ```
    word_ladder('stone','money')
    ```
    may give the output
    ```
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny',
    'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty',
    'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''
    stack = []
    stack.append(start_word)
    q = deque()
    q.append(stack)
    dictionary = []
    f = open(dictionary_file)
    for word in f:
        word = word.rstrip()
        dictionary.append(word)
    if len(start_word) == 0 or len(start_word) != len(end_word):
        return None
    if start_word == end_word:
        return stack
    if start_word in dictionary:
        dictionary.remove(start_word)
    else:
        return None
    while len(list(q)) != 0:
        current_stack = q.popleft()
        for word in dictionary:
            if _adjacent(current_stack[-1], word):
                if word == end_word:
                    current_stack.append(word)
                    return current_stack
                copy_stack = copy(current_stack)
                if len(copy_stack) >= 2:
                    if _adjacent(current_stack[-2], word):
                        copy_stack.pop()
                        copy_stack.append(word)
                    else:
                        copy_stack.append(word)
                else:
                    copy_stack.append(word)
                q.append(copy_stack)
                dictionary.remove(word)
    return None


def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if(len(ladder) == 0):
        return False
    for i in range(len(ladder) - 1):
        if not _adjacent(ladder[i], ladder[i + 1]):
            return False
    return True


def _adjacent(word1, word2):
    '''
    Returns True if the input words differ by only a single character;
    returns False otherwise.

    >>> _adjacent('phone','phony')
    True
    >>> _adjacent('stone','money')
    False
    '''
    diff_char = []
    if len(word1) != len(word2):
        return False
    for i, char in enumerate(word2):
        if(char != word1[i]):
            diff_char.append(char)
    return len(diff_char) == 1
