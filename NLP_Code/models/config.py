#user inputs
#load hyperparameters
# sizes = ['4_full']#['1_tiny', '2_small', '3_standard', '4_full']
# size_folders = ['size_data_t1/' + size for size in sizes]

dataset_sizes = [3000]
alphas = ["005", "01", "02", "03", "04", "05"]
aug_sizes = [8]

#datasets
datasets = ['cr', 'sst2', 'subj', 'trec', 'pc']

#number of output classes
num_classes_list = [2, 2, 2, 6, 2]

#number of augmentations per original sentence
n_aug_list_dict = {'size_data_t1/1_tiny': [32, 32, 32, 32, 32], 
					'size_data_t1/2_small': [32, 32, 32, 32, 32],
					'size_data_t1/3_standard': [16, 16, 16, 16, 4],
					'size_data_t1/4_full': [16, 16, 16, 16, 4]}

#number of words for input
input_size_list = [50, 50, 40, 25, 25]

#word2vec dictionary
# huge_word2vec = huge_word2vec
# "C:/Users/20174868/Desktop/NLP_Code/preprocess/word2vec_dutch_pickle"
word2vec_len = 300


# from gensim.models import KeyedVectors
# from gensim import models

# model = models.KeyedVectors.load_word2vec_format(huge_word2vec, binary=True)
# model.save("word2vec_dutch_pickle.pkl")
