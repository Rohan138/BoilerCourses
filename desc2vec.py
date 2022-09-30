import gensim, logging
from gensim.models import Word2Vec
from gensim.parsing.preprocessing import STOPWORDS
import gensim.downloader as api
import pandas as pd
import numpy as np
import string
import csv
from tqdm import trange
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

v2w_model = api.load('glove-wiki-gigaword-300')
dim = v2w_model.vector_size

data = pd.read_csv('catalog.csv')
size = len(data)
not_words = 0
desc_scores = np.zeros([size, dim])
descs = data['Description']
print('Parsing Descriptions')
for i in trange(len(descs)):
    desc = descs[i]
    desc = desc.lower()
    desc = desc.translate(str.maketrans('','', string.punctuation))
    words = desc.split()
    scores = np.zeros([dim])
    for word in words:
        if word in STOPWORDS:
            continue
        try:
            scores += v2w_model[word]
        except KeyError:
            not_words += 1
    scores /= len(words)
    mean = np.mean(scores)
    std = np.std(scores)
    scores = (scores - mean)/(std + 0.00000001)
    desc_scores[i] = scores

print('Writing Scores to scores.csv')
with open('vectors.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(desc_scores)
