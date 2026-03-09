from collections import defaultdict
import numpy as np


class MarkovText(object):

    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = None

    def get_term_dict(self):

        tokens = self.corpus.split()
        term_dict = defaultdict(list)

        for i in range(len(tokens)):
            current_word = tokens[i]

            if i < len(tokens) - 1:
                next_word = tokens[i + 1]
                term_dict[current_word].append(next_word)
            else:
                term_dict[current_word]  # ensure last word is included

        self.term_dict = dict(term_dict)

        return self.term_dict


    def generate(self, seed_term=None, term_count=15):

        if self.term_dict is None:
            self.get_term_dict()

        if seed_term is None:
            current_word = np.random.choice(list(self.term_dict.keys()))
        else:
            if seed_term not in self.term_dict:
                raise ValueError
            current_word = seed_term

        output = [current_word]

        for _ in range(term_count - 1):

            next_words = self.term_dict.get(current_word)

            if not next_words:
                break

            current_word = np.random.choice(next_words)
            output.append(current_word)

        return " ".join(output)
