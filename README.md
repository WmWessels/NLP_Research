# NLP_Research

EDA repository with the missing file structure and updated code to work with sst2 only (others can easily be added)

Missing from this repo:
- Their "word2vec" (they used glove) can be found here: https://www.kaggle.com/takuok/glove840b300dtxt
- SST2 can be found here https://nlp.stanford.edu/sentiment/

Place the glove txt in the word2vec folder
Place the full unpacked stanfordsentiment folder in raw/sst_1/

run ```python preprocess/sst1_clean.py```
move the new train_orig.txt file to size_data_t1/4_full/sst2/
move the new test.txt to size_data_t1/test/sst2/

now you can run the experiments starting with:

```python experiments/e_1_data_process.py```

then the other experiments under 'e'

Output csv will be in baselines_cnn and baselines_rnn


