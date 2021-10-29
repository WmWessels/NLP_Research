# GROUP 10 - NLP Research

This is the repo of group 10 for the TU/eindhoven 2021 course 2AMM20 - Research Topics in Data Mining.

The work and code done in this repo is based off of the research paper: 

[EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks](https://arxiv.org/abs/1901.11196)

Not included in this repo but required to run:

[OpenDutchWordnet](https://github.com/cltl/OpenDutchWordnet)
    
[DBRD: Dutch Book Reviews Dataset](https://github.com/benjaminvdb/DBRD)

## Directory Structure
```
    .
    |--- README.md
    |--- NLP_Code
         |--- Data                       //contains our training data
         |--- Models                     //contains CNN & RNN models + experiments 
         |      |--- cnn.py              //cnn model experiments
         |      |--- rnn.py              //rnn model experiments
         |      |--- methods.py          //required methods
         |      |--- config.py           //config file that includes sizes, augmentation numbers and alphas
         |--- Filter DBRD                //contains dataset preprocessing and filtering tools for the DBRD dataset
         |      |--- filter_test.py      //filters the test folder of dbrd
         |      |--- filter_training.py  //filters the training folder of dbrd
         |      |--- split_sized_data.py //splits filtered dataset into different sized chunks
         |--- Preprocess                 //contains the resulting word2vec pickle
         |--- augment.py                 //runs augmentations on target file
         |--- augment_all.bat            //runs a batch of augmentations with different parameters on our specific created files
         |--- eda.py                     //contains the adjusted data augmentation techniques 

```
## How to run

You will need to install certain dependencies.

Obviously needed are Python, Keras (and Tensorflow) as well as installing NLTK through pip.

Run the filtering and size splitting first on the DBRD dataset, the resulting datasets should be put into the Data folder

From there you can run augment.py on the desired file.

Within config.py specify the sizes, alphas and augs for filename purposes.

Within cnn.py and rnn.py, specifiy the desired path and then run.

# Acknowledgements
In this section we would like to acknowledge and thank the authors of the [EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks](https://arxiv.org/abs/1901.11196) and their work done which formed the basis of this project. 

Also the creator of [DBRD: Dutch Book Reviews Dataset](https://github.com/benjaminvdb/DBRD) for providing one of the best datasets for sentiment analysis available to the public.

Last but definitely not least, we'd like to thank our professor and guide at the TU/e M. Fang for his advice, feedback and input during the weekly meetings.
