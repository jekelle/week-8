import numpy as np
import pandas as pd
import requests
import re
from collections import defaultdict


class MarkovText:
    
    def __init__(self, corpus):
        self.corpus = corpus
        self.term_dict = self.get_term_dict()
    
    
    def get_term_dict(self):
        tokens = self.corpus.split(" ")
        term_dict = defaultdict(list)
        
        for i in range(len(tokens) - 1):
            current_word = tokens[i]
            next_word = tokens[i + 1]
            term_dict[current_word].append(next_word)
        
        return dict(term_dict)
    
    
    def generate(self, term_count=20, seed_term=None):
        
        if seed_term is None:
            current_word = np.random.choice(list(self.term_dict.keys()))
        else:
            if seed_term not in self.term_dict:
                raise ValueError("Seed term not found in corpus.")
            current_word = seed_term
        
        output = [current_word]
        
        for _ in range(term_count - 1):
            
            if current_word not in self.term_dict:
                break
            
            next_words = self.term_dict[current_word]
            current_word = np.random.choice(next_words)
            output.append(current_word)
        
        return " ".join(output)
