from gensim.models import KeyedVectors, word2vec
from gensim import models

original_word2vec = r'C:\Users\20174868\Desktop\NLP_Code\word2vec_dutch\model.bin'
model = models.KeyedVectors.load_word2vec_format(original_word2vec, binary=True)
word2vec_model = KeyedVectors.load(r"C:\Users\20174868\Desktop\NLP_Code\preprocess\word2vec_dutch_pickle.p")

