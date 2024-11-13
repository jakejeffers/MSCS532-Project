Basic Search Engine with Inverted Index and Trie

Welcome to the Basic Search Engine project! 🚀 

This project explores how modern search engines like Google and Bing perform their magic, with a focus on creating an efficient, scalable solution that handles large-scale text queries. We leverage fundamental data structures to build a search engine that can rapidly index documents, handle keyword queries, and provide autocomplete functionality.

**Table of Contents**

Project Overview

Data Structures Used

Inverted Index

Trie (Prefix Tree)

Implementation Details

Performance Testing

Next Steps

Repository Link

**Project Overview**

This project is inspired by the search engine technology that revolutionized the internet. Our aim is to gain hands-on experience with essential data structures, focusing on:

Efficient document indexing

Fast query response times

Autocomplete functionality

By creating a basic version of a search engine, this project serves as an educational journey into data structure implementation and optimization.

**Data Structures Used**

To achieve the search engine's core functionalities, we implemented two primary data structures:

**Inverted Index**

The inverted index is the backbone of the search engine. It functions as a dictionary where each unique word maps to a list of document IDs that contain that word. This structure allows for rapid keyword lookups, essential for search engines.

****Key Features:****

Uses Python’s defaultdict to efficiently store and retrieve document IDs.

Ensures each document ID appears only once per word through deduplication.

Quick response times for searches due to direct mapping of words to document references.

**Trie (Prefix Tree)**

The trie supports prefix-based search, enabling autocomplete functionality. This tree-like structure allows for fast retrieval of words with common prefixes, enhancing the user experience by suggesting relevant terms as they type.

****Key Features:****

Nodes represent individual characters, building words incrementally.

Supports efficient prefix-based lookups and potential autocomplete suggestions.

**Implementation Details**

****Inverted Index:****

Tokenization: Documents are broken down into individual words.

Indexing: Each word points to a list of document IDs in which it appears.

Search Functionality: Enables rapid retrieval of document IDs for any queried keyword.

****Trie:****

Structure: Nodes are linked to form words through character-based paths.

Insertion & Search: Provides efficient insertion of words and lookup for any given prefix, supporting autocomplete.

**Performance Testing**

Performance is critical for any search engine. Inspired by Tunkelang's approach (2022), we tested both data structures for time and memory efficiency:

Inverted Index: Achieved fast document indexing, with 1000 documents indexed in approximately 0.0181s and a memory footprint of 1.92 MB.

Trie: Demonstrated efficient prefix lookups with an average query response time of 0.121s for 1000 documents, and memory usage of 48 bytes.

Tests confirmed that both data structures are scalable and perform well with larger datasets, validating their suitability for handling complex text queries.

**Next Steps**

In Phase 1, we've established the core functionality of our search engine using optimized data structures. The next phase will involve developing a Proof of Concept (PoC) to showcase the search engine's capabilities, specifically highlighting the efficiency and usability of the inverted index and trie for search and autocomplete functionalities.

**Repository Link**
For the full code and Phase 1 implementation, check out the repository: https://github.com/jakejeffers/ProjectPhase1 

Thank you for checking out the Basic Search Engine project! Please feel free to contribute or reach out with any feedback.
