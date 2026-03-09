import requests
import re
from markov_text import MarkovText

url = 'https://raw.githubusercontent.com/leontoddjohnson/datasets/main/text/inspiration_quotes.txt'

content = requests.get(url)
quotes_raw = content.text

quotes = quotes_raw.replace('\n', ' ')
quotes = re.split("[“”]", quotes)
quotes = quotes[1::2]

corpus = ' '.join(quotes)
corpus = re.sub(r"\s+", " ", corpus)
corpus = corpus.strip()

text_gen = MarkovText(corpus)

print(text_gen.generate(30))
