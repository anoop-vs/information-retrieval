import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict
import re

# Sample documents
documents = {
    "Doc 1": "new home sales top forecasts",
    "Doc 2": "home sales rise in july",
    "Doc 3": "increase in home sales in july",
    "Doc 4": "july new home sales rise"
}

def tokenize(text):
    """Tokenize the input text into a set of lowercase words."""
    return set(re.findall(r'\b\w+\b', text.lower()))

def build_inverted_index(docs):
    """
    Build an inverted index from a collection of documents.

    Args:
        docs (dict): A dictionary where keys are document IDs and values are the document texts.

    Returns:
        dict: An inverted index where keys are words and values are sets of document IDs containing the word.
    """
    index = defaultdict(set)
    for doc_id, text in docs.items():
        words = tokenize(text)
        for word in words:
            index[word].add(doc_id)
    return index



# Build the inverted index from the sample documents
inverted_index = build_inverted_index(documents)

# Print the inverted index
print("Inverted Index:")
for term, doc_ids in inverted_index.items():
    print(f"{term}: {doc_ids}")
