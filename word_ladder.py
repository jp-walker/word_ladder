#!/bin/python3
from collections import deque

def verify_word_ladder(ladder):
    '''
    Returns True if each entry of the input list is adjacent to its neighbors;
    otherwise returns False.

    >>> verify_word_ladder(['stone', 'shone', 'phone', 'phony'])
    True
    >>> verify_word_ladder(['stone', 'shone', 'phony'])
    False
    '''
    if type(ladder) != list or len(ladder) < 1:
        return False
    elif len(ladder) == 1:
        return True
    for i in range(len(ladder) - 1):
        if ladder[i] == ladder[i + 1]:
            return True
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

    count = 0

    if len(word1) != len(word2):
        return False

    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1

    if count == 1:
        return True
    else:
        return False


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
    ['stone', 'shone', 'phone', 'phony', 'peony', 'penny', 'benny', 'bonny', 'boney', 'money']
    ```
    but the possible outputs are not unique,
    so you may also get the output
    ```
    ['stone', 'shone', 'shote', 'shots', 'soots', 'hoots', 'hooty', 'hooey', 'honey', 'money']
    ```
    (We cannot use doctests here because the outputs are not unique.)

    Whenever it is impossible to generate a word ladder between the two words,
    the function returns `None`.
    '''

    dictionary = open(dictionary_file).readlines()
    words = list(set([ word.strip() for word in dictionary ]))
    if len(start_word) != len(end_word):
        return None
    
    if start_word == end_word:
        return [start_word]
    stack = []
    stack.append(start_word)
    queue = deque()
    queue.append(stack)
    
    # Create a stack
    # Push the start word onto the stack
    # Create a queue
    # Enqueue the stack onto the queue

    while len(queue) != 0:
        current = queue[0]
        for word in words:
            if _adjacent(current[-1], word):
                copy = current[:]
                copy.append(word)
                if word == end_word:
                    return copy
                queue.append(copy)
                words.remove(word)
        queue.popleft()

    return None


print(word_ladder('stone','money'))
    #  While the queue is not empty
    # Dequeue a stack from the queue
    # For each word in the dictionary
    #   If the word is adjacent to the top of the stack
    #       If this word is the end word
    #           You are done!
    #           The front stack plus this word is your word ladder.
    #       Make a copy of the stack
    #       Push the found word onto the copy
    #       Enqueue the copy
    #       Delete word from the dictionary
