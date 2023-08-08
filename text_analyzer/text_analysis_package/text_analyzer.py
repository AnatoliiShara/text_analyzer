import os
import re
import fitz
import docx
import spacy
from collections import Counter
#from langdetect import detect

class TextAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.file_extension = os.path.splitext(file_path)[1].lower()
        self.text = None
        self.nlp = spacy.load("en_core_web_sm")

    def analyze(self):
        if self.file_extension == ".txt":
            with open(self.file_path, "r", encoding="utf-8") as file:
                self.text = file.read()
        elif self.file_extension == ".rtf":
            from pyth.plugins.plaintext.reader import PlaintextReader
            with open(self.file_path, "r", encoding="utf-8") as file:
                self.text = PlaintextReader.read(file)
        elif self.file_extension == '.doc':
            import docx
            doc = docx.Document(self.file_path)
            self.text = "\n".join([paragraph.text for paragraph in doc.paragraphs])
        elif self.file_extension == ".pdf":
            import fitz
            doc = fitz.open(self.file_path)
            self.text = ""
            for page in range(doc.page_count):
                self.text += page.get_text("text")

        self.text = str(self.text)
        self.text = self.nlp(self.text)
        sentences = [sent.text for sent in self.text.sents]
        words = [token.text.lower() for token in self.text if token.is_alpha]
        words_counter = Counter(words)
        most_common_words = [word for word, _ in words_counter.most_common(10)]
        #language = detect(self.text)

        print(f"Document type: {self.file_extension}")
        #print(f"Language: {language}")
        print(f"Number of sentences: {len(sentences)}")
        print(f"Number of words: {len(words)}")
        print(f"Most common 10 words: {', '.join(most_common_words)}")

        if len(sentences) > 5:
            print("This text may be summarized")