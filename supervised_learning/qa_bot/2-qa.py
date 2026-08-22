#!/usr/bin/env python3
"""Interactive QA loop over a reference document using BERT."""

question_answer = __import__('0-qa').question_answer

EXIT_WORDS = {'exit', 'quit', 'goodbye', 'bye'}


def answer_loop(reference):
    """
    Answers questions from a reference text in an interactive loop.

    reference: string containing the reference document

    On exit words, prints 'A: Goodbye' and stops. If no answer is
    found, prints 'Sorry, I do not understand your question.'
    """
    while True:
        question = input('Q: ')
        if question.lower().strip() in EXIT_WORDS:
            print('A: Goodbye')
            break
        answer = question_answer(question, reference)
        if answer is None or answer == '':
            print('A: Sorry, I do not understand your question.')
        else:
            print('A: {}'.format(answer))
