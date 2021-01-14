import random
import json
import pickle
import numpy as np
import os

import nltk
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('wordnet')


root_abs_path = os.path.dirname(os.path.abspath(__file__)).split('/src')[0]

lemmatizer = WordNetLemmatizer()
json_file = json.loads(open("%s/intents.json" % root_abs_path).read())

tokens = []
classes = []

# contains a list of tuples
class_associations = []

ignored_tokens = ["?", "!", ".", ",", "'"]

intents = json_file["intents"]

for intent in intents:
    tag = intent['tag']
    patterns = intent.get('patterns', [])

    for pattern in patterns:
        # split the string into words
        token_list = nltk.word_tokenize(pattern)

        # concat the two lists
        tokens.extend(token_list)
        class_associations.append((token_list, tag))

        if tag not in classes:
            classes.append(tag)


lemmatized_words = []

for token in tokens:
    if token not in ignored_tokens:
        # group different forms of a word into a single form
        # for instance verbs may be transformed to infinitive form
        lem = lemmatizer.lemmatize(token)
        lemmatized_words.append(lem)

lemmatized_words = sorted(set(lemmatized_words))
print(lemmatized_words)