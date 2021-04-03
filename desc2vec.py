import gensim, logging
from gensim.models import Word2Vec
import gensim.downloader as api
import pandas as pd
import numpy as np
import string
from tqdm import trange
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

v2w_model = api.load('glove-wiki-gigaword-300')
dim = v2w_model.vector_size

data = pd.read_csv('catalog.csv')
nwords = 0
desc_scores = []
descs = data['Description']
for i in trange(len(descs)):
    desc = descs[i]
    words = desc.split()
    scores = np.zeros([dim])
    for word in words:
        word = word.lower()
        word = word.translate(str.maketrans('','', string.punctuation))
        try:
            scores += v2w_model[word]
        except KeyError:
            nwords += 1
    scores /= len(words)
    desc_scores.append(scores)
print(nwords)

d2w_vectors = gensim.models.keyedvectors.BaseKeyedVectors(vector_size=dim)
d2w_vectors.add(data['Course'], desc_scores)