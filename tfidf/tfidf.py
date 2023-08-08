import os

from text_analyzer.text_analysis_package.text_analyzer import TextAnalyzer
import spacy
import math
from langdetect import detect
from collections import Counter


class TFIDFVectorizer:
    def __init__(self):
        self.corpus = []
        self.vocabulary = []
        self.idf = {}
        self.nlp = spacy.load("en_core_web_sm")

    def add_document(self, document):
        """
        Add a new document to the corpus for TF-IDF calculations.
        """
        self.corpus.append(document)
        self.update_vocabulary()
        self.update_idf()

    def update_vocabulary(self):
        """
        Update the vocabulary based on the unique words in the corpus.
        """
        unique_words = set()
        for document in self.corpus:
            doc = self.nlp(document)
            words = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
            unique_words.update(words)
        self.vocabulary = list(unique_words)

    def update_idf(self):
        """
        Update the Inverse Document Frequency (IDF) values for each word in the vocabulary.
        """
        num_documents = len(self.corpus)
        for word in self.vocabulary:
            word_count = sum(1 for doc in self.corpus if word in doc.lower())
            self.idf[word] = math.log(num_documents / (word_count + 1))  # Add 1 to avoid division by zero

    def get_tfidf_vector(self, document):
        """
        Calculate the TF-IDF vector for a given document.
        """
        doc = self.nlp(document)
        words = [token.text.lower() for token in doc if token.is_alpha and not token.is_stop]
        word_freq = Counter(words)
        vector = {word: word_freq[word] * self.idf.get(word, 0) for word in self.vocabulary}
        return vector

    def rank_sentences(self, document):
        """
        Rank sentences in a document based on their average TF-IDF scores.
        """
        doc = self.nlp(document)
        sentences = [sent.text for sent in doc.sents]
        ranked_sentences = []

        for sentence in sentences:
            sentence_tokens = [token.text.lower() for token in self.nlp(sentence) if
                               token.is_alpha and not token.is_stop]
            if len(sentence_tokens) > 0:  # Check if sentence_tokens is not empty
                sentence_score = sum(self.get_tfidf_vector(sentence).values()) / len(sentence_tokens)
                ranked_sentences.append((sentence, sentence_score))

        ranked_sentences.sort(key=lambda x: x[1], reverse=True)
        return ranked_sentences[:5] if len(ranked_sentences) >= 5 else ranked_sentences

file_paths = ['/home/anatolii-shara/Documents/LeetCode_Solutions/astronomy.txt',
              '/home/anatolii-shara/Documents/hackerrank_leetcode_solutions/cosmos.txt']
# List of file paths
text_analyzers = [TextAnalyzer(file_path) for file_path in file_paths]
tfidf_vectorizer = TFIDFVectorizer()

for text_analyzer in text_analyzers:
    text_analyzer.analyze()
    tfidf_vectorizer.add_document(text_analyzer.text.text)  # Pass the actual text content

new_document = "/home/anatolii-shara/Documents/LeetCode_Solutions/astronomy.txt"
with open(new_document, 'r', encoding='utf-8') as file:
    new_text = file.read()
# Get ranked sentences as a list
top_ranked_sentences = tfidf_vectorizer.rank_sentences(new_text)
ranked_sentences = [sentence for sentence, _ in top_ranked_sentences]

# Print the list of ranked sentences
print("Ranked Sentences:")
for i, sentence in enumerate(ranked_sentences, start=1):
    print(f"Rank {i}: Sentence: {sentence}")


