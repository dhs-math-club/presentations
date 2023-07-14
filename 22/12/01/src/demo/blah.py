import math
import os

from bm25 import BM25

DATA_DIRECTORY = "documents"


def get_contents(file_path):
    with open(file_path) as f:
        blah = f.read()
    return blah


# we'll generate some fake texts to experiment with
document_paths = [
    os.path.join(DATA_DIRECTORY, file_path)
    for file_path in os.listdir(DATA_DIRECTORY)
    if file_path.endswith(".txt")
]
corpus = [get_contents(document_path) for document_path in document_paths]

# remove stop words and tokenize them (we probably want to do some more
# preprocessing with our text in a real world setting, but we'll keep
# it simple here)
stopwords = set(["for", "a", "of", "the", "and", "to", "in"])
texts = [
    [word for word in document.lower().split() if word not in stopwords]
    for document in corpus
]

# build a word count dictionary so we can remove words that appear only once
word_count_dict = {}
for text in texts:
    for token in text:
        word_count = word_count_dict.get(token, 0) + 1
        word_count_dict[token] = word_count

texts = [[token for token in text if word_count_dict[token] > 1] for text in texts]

# query our corpus to see which document is more relevant
query = input("search for thing! ")
query = [word for word in query.lower().split() if word not in stopwords]

bm25 = BM25()
bm25.fit(texts)
scores = bm25.search(query)

for score, doc_path in zip(scores, document_paths):
    score = round(score, 3)
    print(str(score) + "\t" + doc_path)
