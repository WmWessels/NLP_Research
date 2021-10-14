from gensim.models import KeyedVectors
from gensim import models
import gensim

original_word2vec = r'C:\Users\20174868\Desktop\NLP_Code\word2vec_dutch\model.bin'

model = models.KeyedVectors.load_word2vec_format(original_word2vec, binary=True)
model.save("savedmodel.pickle")

