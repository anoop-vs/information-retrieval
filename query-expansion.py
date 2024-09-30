from collections import defaultdict

class QueryExpander:
    def __init__(self, synonyms):
        """
        Initialize the QueryExpander with a dictionary of synonyms.
        :param synonyms: A dictionary where keys are terms and values are lists of synonyms.
        """
        self.synonyms = synonyms

    def expand(self, query):
        """
        Expand the query using the synonyms dictionary.
        :param query: A string containing the original query.
        :return: A list of expanded terms.
        """
        query_terms = query.split()
        expanded_terms = set(query_terms)

        for term in query_terms:
            if term in self.synonyms:
                expanded_terms.update(self.synonyms[term])
        
        return list(expanded_terms)

# Example usage
if __name__ == "__main__":
    # Define a simple synonym dictionary
    synonyms = {
        "cat": ["feline", "kitten"],
        "dog": ["canine", "puppy"],
        "fast": ["quick", "swift"],
        "car": ["automobile", "vehicle"]
    }
    
    query_expander = QueryExpander(synonyms)

    original_query = "cat dog"
    expanded_query = query_expander.expand(original_query)

    print("Original Query:", original_query)
    print("Expanded Query:", expanded_query)
