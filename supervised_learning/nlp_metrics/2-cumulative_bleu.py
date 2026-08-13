#!/usr/bin/env python3
"""Calculates the cumulative n-gram BLEU score for a sentence."""
import numpy as np


def cumulative_bleu(references, sentence, n):
    """Calculates the cumulative n-gram BLEU score for a sentence."""
    def make_ngrams(words, k):
        """Builds a list of k-grams from a list of words."""
        grams = []
        for i in range(len(words) - k + 1):
            grams.append(" ".join(words[i:i + k]))
        return grams

    def precision(k):
        """Clipped n-gram precision for a given gram size k."""
        sent_grams = make_ngrams(sentence, k)
        clipped = 0
        for gram in set(sent_grams):
            count = sent_grams.count(gram)
            max_ref = 0
            for ref in references:
                max_ref = max(max_ref, make_ngrams(ref, k).count(gram))
            clipped = clipped + min(count, max_ref)
        return clipped / len(sent_grams)

    sentence_len = len(sentence)

    precisions = []
    for k in range(1, n + 1):
        precisions.append(precision(k))

    precisions = np.array(precisions)
    geo_mean = np.exp(np.sum(np.log(precisions)) / n)

    ref_lens = [len(ref) for ref in references]
    closest = min(ref_lens, key=lambda r: (abs(r - sentence_len), r))

    if sentence_len > closest:
        bp = 1.0
    else:
        bp = np.exp(1 - closest / sentence_len)

    return bp * geo_mean
