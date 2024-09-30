import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class VectorSpaceModel:
    def __init__(self, documents):
        # Store documents
        self.documents = documents
        # Initialize the TF-IDF Vectorizer
        self.vectorizer = TfidfVectorizer()
        # Fit and transform the documents into a TF-IDF matrix
        self.tfidf_matrix = self.vectorizer.fit_transform(documents)

    def query(self, query_string):
        # Transform the query into the same TF-IDF space
        query_vector = self.vectorizer.transform([query_string])
        # Compute cosine similarity between the query and the documents
        similarities = cosine_similarity(query_vector, self.tfidf_matrix)
        return similarities.flatten()

    def retrieve_top_n(self, query_string, n=5):
        # Get similarity scores
        scores = self.query(query_string)
        # Get indices of the top n documents
        top_indices = np.argsort(scores)[-n:][::-1]
        # Retrieve top n documents and their scores
        top_documents = [(self.documents[i], scores[i]) for i in top_indices]
        return top_documents

# Sample documents
documents = [
    "The cat in the hat.",
    "A cat is a fine pet.",
    "Dogs are great pets.",
    "The dog chased the cat.",
    "Cats and dogs can be friends."
]

# Initialize the Vector Space Model
vsm = VectorSpaceModel(documents)

# Example query
query_string = "cat and dog"
top_n = 3

# Retrieve top N documents
results = vsm.retrieve_top_n(query_string, n=top_n)

# Print the results
print("Top documents for the query:", query_string)
for doc, score in results:
    print(f"Document: {doc} | Score: {score:.4f}")
