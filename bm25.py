import math
from collections import defaultdict

class BM25:
    def __init__(self, documents, k1=1.5, b=0.75):
        self.documents = documents
        self.k1 = k1
        self.b = b
        self.doc_len = [len(doc.split()) for doc in documents]
        self.avg_doc_len = sum(self.doc_len) / len(documents)
        self.term_freqs = [self._term_frequencies(doc) for doc in documents]
        self.idf = self._compute_idf()

    def _term_frequencies(self, doc):
        freq = defaultdict(int)
        for term in doc.split():
            freq[term] += 1
        return freq

    def _compute_idf(self):
        idf = defaultdict(int)
        num_docs = len(self.documents)

        for doc in self.documents:
            unique_terms = set(doc.split())
            for term in unique_terms:
                idf[term] += 1

        for term in idf:
            idf[term] = math.log((num_docs - idf[term] + 0.5) / (idf[term] + 0.5) + 1)
        
        return idf

    def score(self, doc_idx, query_terms):
        score = 0
        doc_len = self.doc_len[doc_idx]
        for term in query_terms:
            if term in self.term_freqs[doc_idx]:
                tf = self.term_freqs[doc_idx][term]
                idf = self.idf.get(term, 0)
                score += idf * (tf * (self.k1 + 1)) / (tf + self.k1 * (1 - self.b + self.b * (doc_len / self.avg_doc_len)))
        return score

    def rank(self, query):
        query_terms = query.split()
        scores = [(doc_idx, self.score(doc_idx, query_terms)) for doc_idx in range(len(self.documents))]
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
    
    bm25 = BM25(documents)
    
    query = "cat dog"
    rankings = bm25.rank(query)
    
    print("Ranked documents:")
    for doc_idx, score in rankings:
        print(f"Document {doc_idx}: {documents[doc_idx]} (Score: {score:.4f})")
