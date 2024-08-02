import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import CountVectorizer

# Sample documents
documents = [
    "breakthrough drug for schizophrenia",
    "new schizophrenia drug",
    "new approach for treatment of schizophrenia",
    "new hopes for schizophrenia patients"
]

# Create a CountVectorizer object to transform the documents into a term-document matrix
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)

# Convert the term-document matrix to a pandas DataFrame
df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out(), index=[f"Doc {i+1}" for i in range(len(documents))])

# Display the term-document matrix
print("Term-Document Matrix:")
print(df)

# Plot the term-document matrix
plt.figure(figsize=(10, 6))
sns.heatmap(df, annot=True, cmap="YlGnBu", fmt="d", cbar=True, linewidths=0.5, linecolor='black')
plt.title("Term-Document Matrix")
plt.xlabel("Terms")
plt.ylabel("Documents")
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()
