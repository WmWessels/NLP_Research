from gensim.models import KeyedVectors
import os

#code to write the word2vec .bin file to a pickle file, which we will use later to access the word embeddings

#make sure you are in ../NLP_Code

path = os.getcwd()

path_check = os.path.split(path)

if not path_check[1] == "NLP_Code":
    raise Exception("Please change your directory to ../NLP_Code")

original_word2vec = path + "/word2vec_dutch/model.bin"
model = KeyedVectors.load_word2vec_format(original_word2vec, binary=True)
model.save(path+"/preprocess/word2vec_dutch_pickle.p")


