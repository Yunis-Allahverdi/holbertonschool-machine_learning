#!/usr/bin/env python3
"""Multi-reference QA: semantic search to pick a doc, then BERT to answer."""

semantic_search = __import__('3-semantic_search').semantic_search
qa = __import__('0-qa').question_answer

EXIT_WORDS = {'exit', 'quit', 'goodbye', 'bye'}


def question_answer(corpus_path):
    """
    Answers questions from multiple reference texts.

    corpus_path: path to the corpus of reference documents

    For each question, finds the most relevant document via semantic
    search, then extracts the answer from it with BERT. Exits on any
    exit word; falls back to a default message when no answer is found.
    """
    while True:
        question = input('Q: ')
        if question.lower().strip() in EXIT_WORDS:
            print('A: Goodbye')
            break
        reference = semantic_search(corpus_path, question)
        answer = qa(question, reference)
        if answer is None or answer == '':
            print('A: Sorry, I do not understand your question.')
        else:
            print('A: {}'.format(answer))
