from collections import defaultdict

class InvertedIndex:
    def __init__(self):
        # Dictionary where each word maps to a list of document IDs
        self.index = defaultdict(list)

    def add_document(self, doc_id, text):
        # Tokenize text into words
        words = text.lower().split()
        for word in set(words):  # Use set to avoid duplicates within the same document
            self.index[word].append(doc_id)

    def search(self, query):
        # Returns list of document IDs containing the query word
        return self.index.get(query.lower(), [])

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
class SearchEngine:
    def __init__(self):
        self.index = InvertedIndex()
        self.trie = Trie()

    def add_document(self, doc_id, text):
        # Add document to the inverted index
        self.index.add_document(doc_id, text)
        # Add each word to the trie for prefix searching
        words = text.lower().split()
        for word in words:
            self.trie.insert(word)

    def search_by_keyword(self, keyword):
        # Search the inverted index
        return self.index.search(keyword)

    def search_by_prefix(self, prefix):
        # Search the trie
        return self.trie.search_prefix(prefix)
# Sample usage
search_engine = SearchEngine()

# Add sample documents
documents = {
    1: "Python programming is fun",
    2: "Python and data structures",
    3: "Search engines use data structures",
}

for doc_id, text in documents.items():
    search_engine.add_document(doc_id, text)

# Keyword search using the inverted index
print("Keyword search for 'python':", search_engine.search_by_keyword("python"))  # Expected: [1, 2]
print("Keyword search for 'data':", search_engine.search_by_keyword("data"))      # Expected: [2, 3]

# Prefix search using the Trie
print("Prefix search for 'pro':", search_engine.search_by_prefix("pro"))          # Expected: True
print("Prefix search for 'str':", search_engine.search_by_prefix("str"))          # Expected: True
print("Prefix search for 'java':", search_engine.search_by_prefix("java"))        # Expected: False
