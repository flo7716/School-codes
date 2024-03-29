import math

# Example documents
documents = [
    "Machine learning is a subset of artificial intelligence.",
    "Artificial intelligence is transforming various industries and Artificial world.",
    "Machine learning and data science are closely related, and I love Artificial intelligence."
]

# Term to calculate TF-IDF for
term = "Artificial"

# Preprocessed and tokenized documents
tokens = [document.lower().split() for document in documents]

# Calculate TF (Term Frequency) for the term in each document
tf_scores = []
for doc_tokens in tokens:
    term_count = doc_tokens.count(term.lower())
    total_terms = len(doc_tokens)
    tf = term_count / total_terms
    tf_scores.append(tf)

# Calculate IDF (Inverse Document Frequency) for the term
N = len(documents)
df = sum(1 for doc_tokens in tokens if term.lower() in doc_tokens)
idf = math.log(N / (1 + df))

# Calculate TF-IDF scores for each document
tfidf_scores = [tf * idf for tf in tf_scores]

# Print the TF-IDF scores for the term in each document
for i, document in enumerate(documents):
    print(f"TF-IDF score for '{term}' in Document {i + 1}: {tfidf_scores[i]:.4f}")