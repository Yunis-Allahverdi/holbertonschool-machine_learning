#!/usr/bin/env python3
"""Dataset class that loads and preps a dataset for machine translation"""
import tensorflow as tf
import transformers
from setup import load_pt2en


class Dataset:
    """Loads and preps a dataset for machine translation"""

    def __init__(self):
        """Initializes the dataset and its tokenizers"""
        self.data_train = load_pt2en('train')
        self.data_valid = load_pt2en('validation')

        tokenizers = self.tokenize_dataset(self.data_train)
        self.tokenizer_pt = tokenizers[0]
        self.tokenizer_en = tokenizers[1]

    def tokenize_dataset(self, data):
        """Creates sub-word tokenizers for the dataset"""
        pt_sentences = []
        en_sentences = []

        for pt, en in data:
            pt_sentences.append(pt.numpy().decode('utf-8'))
            en_sentences.append(en.numpy().decode('utf-8'))

        tokenizer_pt = transformers.AutoTokenizer.from_pretrained(
            'neuralmind/bert-base-portuguese-cased'
        )
        tokenizer_en = transformers.AutoTokenizer.from_pretrained(
            'bert-base-uncased'
        )

        tokenizer_pt = tokenizer_pt.train_new_from_iterator(
            pt_sentences, vocab_size=2 ** 13
        )
        tokenizer_en = tokenizer_en.train_new_from_iterator(
            en_sentences, vocab_size=2 ** 13
        )

        return tokenizer_pt, tokenizer_en