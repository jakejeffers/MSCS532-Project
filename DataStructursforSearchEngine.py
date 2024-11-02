import random
import string
import time
import sys
from collections import defaultdict

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(list)

    def add_document(self, doc_id, text):
        words = text.lower().split()
        for word in set(words):
            self.index[word].append(doc_id)

    def search(self, query):
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

# Function to generate random documents
def generate_random_documents(num_docs, words_per_doc):
    documents = {}
    for i in range(num_docs):
        # Create a random document with a specified number of words
        random_words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
                        for _ in range(words_per_doc)]
        documents[i] = ' '.join(random_words)
    return documents

# Function to measure efficiency for Inverted Index
def measure_inverted_index_efficiency(num_docs, words_per_doc):
    inverted_index = InvertedIndex()
    
    # Generate random documents
    documents = generate_random_documents(num_docs, words_per_doc)

    # Measure time to add documents
    start_time = time.time()
    for doc_id, text in documents.items():
        inverted_index.add_document(doc_id, text)
    end_time = time.time()

    # Measure memory usage
    inverted_index_size = sys.getsizeof(inverted_index.index)

    print(f"Inverted Index - Time taken to add {num_docs} documents: {end_time - start_time:.4f} seconds")
    print(f"Inverted Index - Memory size: {inverted_index_size} bytes")

# Function to measure efficiency for Trie
def measure_trie_efficiency(num_docs, words_per_doc):
    trie = Trie()
    
    # Generate random documents
    documents = generate_random_documents(num_docs, words_per_doc)

    # Measure time to add documents
    start_time = time.time()
    for text in documents.values():
        for word in text.lower().split():
            trie.insert(word)
    end_time = time.time()

    # Measure memory usage (approximation)
    trie_size = sys.getsizeof(trie.root)

    print(f"Trie - Time taken to add {num_docs} documents: {end_time - start_time:.4f} seconds")
    print(f"Trie - Approximate memory size: {trie_size} bytes")

# Parameters for testing
num_docs = 1000    # Number of documents to generate
words_per_doc = 50 # Number of words per document

# Measure efficiency for both data structures
measure_inverted_index_efficiency(num_docs, words_per_doc)
measure_trie_efficiency(num_docs, words_per_doc)
