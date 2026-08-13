#!/usr/bin/env python3
"""Calculates the n-gram BLEU score for a sentence."""
import numpy as np


def ngram_bleu(references, sentence, n):
    """Calculates the n-gram BLEU score for a sentence."""
    def make_ngrams(words, n):
        """Builds a list of n-grams from a list of words."""
        grams = []
        for i in range(len(words) - n + 1):
            gram = " ".join(words[i:i + n])
            grams.append(gram)
        return grams

    sentence_len = len(sentence)
    sent_grams = make_ngrams(sentence, n)

    clipped = 0
    for gram in set(sent_grams):
        count = sent_grams.count(gram)
        max_ref = 0
        for ref in references:
            ref_grams = make_ngrams(ref, n)
            max_ref = max(max_ref, ref_grams.count(gram))
        clipped = clipped + min(count, max_ref)

    precision = clipped / len(sent_grams)

    ref_lens = [len(ref) for ref in references]
    closest = min(ref_lens, key=lambda r: (abs(r - sentence_len), r))

    if sentence_len > closest:
        bp = 1.0
    else:
        bp = np.exp(1 - closest / sentence_len)

    return bp * precision
