import math
from collections import defaultdict

class TFIDF:
    def __init__(self, documents):
        self.documents = documents
        self.doc_count = len(documents)
        self.term_freqs = [self._term_frequencies(doc) for doc in documents]
        self.idf = self._compute_idf()

    def _term_frequencies(self, doc):
        freq = defaultdict(int)
        for term in doc.split():
            freq[term] += 1
        return freq

    def _compute_idf(self):
        idf = defaultdict(int)

        for doc in self.documents:
            unique_terms = set(doc.split())
            for term in unique_terms:
                idf[term] += 1

        for term in idf:
            idf[term] = math.log((self.doc_count + 1) / (idf[term] + 1)) + 1  # Smoothing
        return idf

    def tfidf_score(self, doc_idx, query_terms):
        score = 0
        for term in query_terms:
            tf = self.term_freqs[doc_idx].get(term, 0)
            idf = self.idf.get(term, 0)
            score += tf * idf
        return score

    def rank(self, query):
        query_terms = query.split()
        scores = [(doc_idx, self.tfidf_score(doc_idx, query_terms)) for doc_idx in range(self.doc_count)]
        scores.sort(key=lambda x: x[1], reverse=True)
        return scores

# Example usage
if __name__ == "__main__":
    documents = [
        "the cat in the hat",
        "the quick brown fox",
        "the lazy dog",
        "the cat sat on the mat",
        "the dog chased the cat"
    ]
    
    tfidf = TFIDF(documents)
    
    query = "cat dog"
    rankings = tfidf.rank(query)
    
    print("Ranked documents:")
    for doc_idx, score in rankings:
        print(f"Document {doc_idx}: {documents[doc_idx]} (Score: {score:.4f})")
