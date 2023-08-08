import spacy
from collections import Counter
from tabulate import tabulate

nlp = spacy.load("en_core_web_sm")

def custom_count_vectorizer(documents):
    #tokenize, remove stopwords, ande perform stemming using Spacy
    tokens_list = []
    for doc in documents:
        tokens = [token.lemma_.lower() for token in nlp(doc) if not token.is_stop and token.is_alpha]
        tokens_list.append(tokens)
    # create vocabulary and count occurences
    vocabulary = set(word for tokens in tokens_list for word in tokens)
    vocabulary = sorted(vocabulary)
    word_to_index = {word: index for index, word in enumerate(vocabulary)}
    counts = []
    for tokens in tokens_list:
        counter = Counter(tokens)
        vector = [counter.get(word, 0) for word in vocabulary]
        counts.append(vector)
    return vocabulary, counts

# examples
documents = ["This is the first document.", "This document is the second document.", "And this is the third one."]
vocabulary, counts = custom_count_vectorizer(documents)

print(f"Vocabulary: {vocabulary}")
print(f"Counts: {counts}")

#create table-like representations
table_data = []
for word, count in zip(vocabulary, counts):
    table_data.append([word] + count)

table_headers = ["Word"] + [f"Doc {i + 1}" for i in range(len(documents))]
table = tabulate(table_data, headers=table_headers, tablefmt="grid")
print("\Word Counts")
print(table)