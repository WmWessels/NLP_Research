from methods import *
from numpy.random import seed
seed(0)
from e_config import *
import os

###############################
#### run model and get acc ####
###############################

def run_model(train_file, test_file, num_classes, input_size, percent_dataset, word2vec):

	#initialize model
	model = build_cnn(input_size, word2vec_len, num_classes)

	#load data
	train_x, train_y = get_x_y(train_file, num_classes, word2vec_len, input_size, word2vec, percent_dataset)
	test_x, test_y = get_x_y(test_file, num_classes, word2vec_len, input_size, word2vec, 1)

	#implement early stopping
	callbacks = [EarlyStopping(monitor='val_loss', patience=3)]

	#train model
	model.fit(	train_x, 
				train_y, 
				epochs=100000, 
				callbacks=callbacks,
				validation_split=0.1, 
				batch_size=1024, 
				shuffle=True, 
				verbose=0)
	#model.save('checkpoints/lol')
	#model = load_model('checkpoints/lol')

	#evaluate model
	y_pred = model.predict(test_x)
	test_y_cat = one_hot_to_categorical(test_y)
	y_pred_cat = one_hot_to_categorical(y_pred)
	acc = accuracy_score(test_y_cat, y_pred_cat)

	#clean memory???
	train_x, train_y = None, None
	gc.collect()

	#return the accuracy
	#print("data with shape:", train_x.shape, train_y.shape, 'train=', train_file, 'test=', test_file, 'with fraction', percent_dataset, 'had acc', acc)
	return acc

###############################
### get baseline accuracies ###
###############################

def compute_baselines(writer):

	#baseline computation
	performances = []
	
	dataset_folder = os.getcwd() + "/data"
			
	word2vec = KeyedVectors.load(huge_word2vec)

	train_path = dataset_folder + '/test.txt'
	test_path = dataset_folder + '/train_orig.txt'
	acc = run_model(train_path, test_path, 2, 50, 1, word2vec) ##changed to 2
	performances.append(str(acc))

	line = ','.join(performances)
	print(line)
	writer.write(line+'\n')

###############################
############ main #############
###############################

if __name__ == "__main__":

	writer = open(result_folder+"/accuracys_cnn.txt", 'w')

	for i in range(10, 24):

		seed(i)
		print(i)
		compute_baselines(writer)
