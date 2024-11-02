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
# Example usage and test
documents = {
    1: "Python programming is fun",
    2: "Python and data structures",
    3: "Search engines use data structures",
}

index = InvertedIndex()
for doc_id, text in documents.items():
    index.add_document(doc_id, text)

# Testing search function
print(index.search("python"))  # Should return [1, 2]
print(index.search("data"))    # Should return [2, 3]
print(index.search("fun"))     # Should return [1]
