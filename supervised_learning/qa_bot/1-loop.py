#!/usr/bin/env python3
"""Interactive loop that echoes an empty answer until the user exits."""

EXIT_WORDS = {'exit', 'quit', 'goodbye', 'bye'}

while True:
    question = input('Q: ')
    if question.lower().strip() in EXIT_WORDS:
        print('A: Goodbye')
        break
    print('A:')
