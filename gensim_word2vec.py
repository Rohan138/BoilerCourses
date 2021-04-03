import gensim, logging
from gensim.models import Word2Vec
import gensim.downloader as api
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

v2w_model = api.load('glove-wiki-gigaword-300')