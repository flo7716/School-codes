from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.preprocessing import normalize
import pandas as pd

corpus = {1: "Machine learning is a subset of artificial intelligence.", 2: "Artificial intelligence is transforming various industries and Artificial world.", 3: "Machine learning and data science are closely related, and I love Artificial intelligence."}

cvect = CountVectorizer(ngram_range=(1,1), token_pattern='(?u)\\b\\w+\\b')
counts = cvect.fit_transform(corpus.values())
normalized_counts = normalize(counts, norm='l1', axis=1)

tfidf = TfidfVectorizer(ngram_range=(1,1), token_pattern='(?u)\\b\\w+\\b', smooth_idf=False)
tfs = tfidf.fit_transform(corpus.values())
new_tfs = normalized_counts.multiply(tfidf.idf_)

feature_names = tfidf.get_feature_names_out()
corpus_index = [n for n in corpus]
df = pd.DataFrame(new_tfs.T.todense(), index=feature_names, columns=corpus_index)

print(df.loc[['artificial']])