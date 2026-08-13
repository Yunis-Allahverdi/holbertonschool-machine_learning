#!/usr/bin/env python3
"""Calculates the unigram BLEU score for a sentence."""
import numpy as np


def uni_bleu(references, sentence):
    """Calculates the unigram BLEU score for a sentence."""
    sentence_len = len(sentence)

    clipped = 0
    for word in set(sentence):
        count = sentence.count(word)
        max_ref = 0
        for ref in references:
            max_ref = max(max_ref, ref.count(word))
        clipped = clipped + min(count, max_ref)

    precision = clipped / sentence_len

    ref_lens = [len(ref) for ref in references]
    closest = min(ref_lens, key=lambda r: (abs(r - sentence_len), r))

    if sentence_len > closest:
        bp = 1.0
    else:
        bp = np.exp(1 - closest / sentence_len)

    return bp * precision
