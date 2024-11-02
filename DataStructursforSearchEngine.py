from collections import defaultdict

class InvertedIndex:
    def __init__(self):
        # A dictionary where each word maps to a list of document IDs
        self.index = defaultdict(list)

    def add_document(self, doc_id, text):
        # Tokenize the text into words (simple splitting by spaces for now)
        words = text.lower().split()
        for word in set(words):  # Use set to avoid duplicate words in the same document
            self.index[word].append(doc_id)

    def search(self, query):
        # Returns a list of document IDs for the query word
        return self.index.get(query.lower(), [])
