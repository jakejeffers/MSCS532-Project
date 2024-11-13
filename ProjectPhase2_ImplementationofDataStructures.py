from collections import defaultdict
import sys
import time
import random
import string

class InvertedIndex:
    def __init__(self):
        self.index = defaultdict(list)

    def add_document(self, doc_id, text):
        words = text.lower().split()
        for word in set(words):
            self.index[word].append(doc_id)

    def search(self, query):
        return self.index.get(query.lower(), [])

    def delete_document(self, doc_id, text):
        words = text.lower().split()
        for word in set(words):
            if doc_id in self.index[word]:
                self.index[word].remove(doc_id)
                if not self.index[word]:  # Remove word if no document has it
                    del self.index[word]

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
                return []
            node = node.children[char]
        return self._collect_words(node, prefix)

    def _collect_words(self, node, prefix):
        results = []
        if node.is_end_of_word:
            results.append(prefix)
        for char, child in node.children.items():
            results.extend(self._collect_words(child, prefix + char))
        return results

# Additional Helper Functions for Testing
def generate_random_documents(num_docs, words_per_doc):
    documents = {}
    for i in range(num_docs):
        random_words = [''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
                        for _ in range(words_per_doc)]
        documents[i] = ' '.join(random_words)
    return documents

# Script to Demonstrate Key Operations

# Initialize data structures
index = InvertedIndex()
trie = Trie()

# Generate sample documents
sample_docs = generate_random_documents(5, 10)
for doc_id, text in sample_docs.items():
    index.add_document(doc_id, text)
    for word in text.split():
        trie.insert(word)

# Demonstrate Inverted Index Search
print("Inverted Index Search Results for a sample word:")
query_word = list(sample_docs.values())[0].split()[0]  # Select a random word from a sample doc
print(f"Searching for '{query_word}'...")
print(f"Documents containing '{query_word}': {index.search(query_word)}\n")

# Demonstrate Trie Prefix Search
print("Trie Prefix Search Results:")
prefix = query_word[:3]  # Use the first 3 characters as a sample prefix
print(f"Autocomplete for prefix '{prefix}': {trie.search_prefix(prefix)}")
