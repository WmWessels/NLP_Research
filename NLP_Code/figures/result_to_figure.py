    import os
    import glob
    import pandas as pd
    import matplotlib.pyplot as plt

    list_eda = []
    path = os.getcwd()
    print(path)

    for f in glob.glob(path + '/results/*'):
        with open(f, encoding="utf8") as current_file:
            first_split = current_file.name.split('accuracys_')[1]
            second_split = first_split.split('_')
            values = list(map(float, current_file.readlines()))
            maximum = max(values)
            average = sum(values)/len(values)
            assert maximum >= average
            list_eda.append([second_split[0], second_split[1], second_split[2], second_split[3][0], average, maximum])


    print(list_eda)
    dataframe = pd.DataFrame(list_eda, columns=["model", "dataset_size", "alpha", "n_aug", "avg", "max"])
    dataframe.sort_values(by=['model','dataset_size','alpha','n_aug'])

    list_baselines = []

    for f in glob.glob(path + '/baseline_results/*'):
        with open(f, encoding="utf8") as current_file:
            values = list(map(float, current_file.readlines()))
            maximum = max(values)
            average = sum(values)/len(values)
            assert maximum >= average
            list_baselines.append(average)


    print(list_baselines)
    dataframe['performance_gain'] = dataframe['avg']

    for i in range(len(dataframe)):
        if dataframe.iloc[i, 0] == "cnn" and dataframe.iloc[i, 1] == "500":
            dataframe.iloc[i, 6] = dataframe.iloc[i, 6] - list_baselines[3]
        if dataframe.iloc[i, 0] == "cnn" and dataframe.iloc[i, 1] == "1000":
            dataframe.iloc[i, 6] = dataframe.iloc[i, 6] - list_baselines[0]
        if dataframe.iloc[i, 0] == "cnn" and dataframe.iloc[i, 1] == "1500":
            dataframe.iloc[i, 6] = dataframe.iloc[i, 6] - list_baselines[1]
        if dataframe.iloc[i, 0] == "cnn" and dataframe.iloc[i, 1] == "3000":
            dataframe.iloc[i, 6] = dataframe.iloc[i, 6] - list_baselines[2]

        if dataframe.iloc[i, 0] == "rnn" and dataframe.iloc[i, 1] == "500":
            dataframe.iloc[i, 6] = dataframe.iloc[i, 6] - list_baselines[7]
        if dataframe.iloc[i, 0] == "rnn" and dataframe.iloc[i, 1] == "1000":
            dataframe.iloc[i, 6] = dataframe.iloc[i, 6] - list_baselines[4]
        if dataframe.iloc[i, 0] == "rnn" and dataframe.iloc[i, 1] == "1500":
            dataframe.iloc[i, 6] = dataframe.iloc[i, 6] - list_baselines[5]
        if dataframe.iloc[i, 0] == "rnn" and dataframe.iloc[i, 1] == "3000":
            dataframe.iloc[i, 6] = dataframe.iloc[i, 6] - list_baselines[6]

    data_500_rnn_aug_4 = dataframe.loc[(dataframe['dataset_size'] == "500") & (dataframe['model'] == "rnn") & (dataframe['n_aug'] == "4")]['performance_gain']
    data_500_rnn_aug_8 = dataframe.loc[(dataframe['dataset_size'] == "500") & (dataframe['model'] == "rnn") & (dataframe['n_aug'] == "8")]['performance_gain']

    data_1000_rnn_aug_4 = dataframe.loc[(dataframe['dataset_size'] == "1000") & (dataframe['model'] == "rnn") & (dataframe['n_aug'] == "4")]['performance_gain']
    data_1000_rnn_aug_8 = dataframe.loc[(dataframe['dataset_size'] == "1000") & (dataframe['model'] == "rnn") & (dataframe['n_aug'] == "8")]['performance_gain']

    data_1500_rnn_aug_4 = dataframe.loc[(dataframe['dataset_size'] == "1500") & (dataframe['model'] == "rnn") & (dataframe['n_aug'] == "4")]['performance_gain']
    data_1500_rnn_aug_8 = dataframe.loc[(dataframe['dataset_size'] == "1500") & (dataframe['model'] == "rnn") & (dataframe['n_aug'] == "8")]['performance_gain']

    data_full_rnn_aug_4 = dataframe.loc[(dataframe['dataset_size'] == "3000") & (dataframe['model'] == "rnn") & (dataframe['n_aug'] == "4")]['performance_gain']
    data_full_rnn_aug_8 = dataframe.loc[(dataframe['dataset_size'] == "3000") & (dataframe['model'] == "rnn") & (dataframe['n_aug'] == "8")]['performance_gain']

    data_500_cnn_aug_4 = dataframe.loc[(dataframe['dataset_size'] == "500") & (dataframe['model'] == "cnn") & (dataframe['n_aug'] == "4")]['performance_gain']
    data_500_cnn_aug_8 = dataframe.loc[(dataframe['dataset_size'] == "500") & (dataframe['model'] == "cnn") & (dataframe['n_aug'] == "8")]['performance_gain']

    data_1000_cnn_aug_4 = dataframe.loc[(dataframe['dataset_size'] == "1000") & (dataframe['model'] == "cnn") & (dataframe['n_aug'] == "4")]['performance_gain']
    data_1000_cnn_aug_8 = dataframe.loc[(dataframe['dataset_size'] == "1000") & (dataframe['model'] == "cnn") & (dataframe['n_aug'] == "8")]['performance_gain']

    data_1500_cnn_aug_4 = dataframe.loc[(dataframe['dataset_size'] == "1500") & (dataframe['model'] == "cnn") & (dataframe['n_aug'] == "4")]['performance_gain']
    data_1500_cnn_aug_8 = dataframe.loc[(dataframe['dataset_size'] == "1500") & (dataframe['model'] == "cnn") & (dataframe['n_aug'] == "8")]['performance_gain']

    data_full_cnn_aug_4 = dataframe.loc[(dataframe['dataset_size'] == "3000") & (dataframe['model'] == "cnn") & (dataframe['n_aug'] == "4")]['performance_gain']
    data_full_cnn_aug_8 = dataframe.loc[(dataframe['dataset_size'] == "3000") & (dataframe['model'] == "cnn") & (dataframe['n_aug'] == "8")]['performance_gain']


    plt.xticks([0,1,2,3,4,5], ["0.05", "0.1", "0.2", "0.3", "0.4", "0.5"])
    plt.plot(dataframe['alpha'].unique(), data_500_cnn_aug_8*100, marker = "^", label = "N=500")
    plt.plot(dataframe['alpha'].unique(), data_1000_cnn_aug_8*100, marker = "o", label = "N=1000")
    plt.plot(dataframe['alpha'].unique(), data_1500_cnn_aug_8*100, marker = "v",label = "N=1500")
    plt.plot(dataframe['alpha'].unique(), data_full_cnn_aug_8*100, marker = "s", label = "Full")
    plt.xlabel("Alphas", fontsize = 16)
    plt.ylabel("Performance Gain", fontsize = 16)
    plt.title("CNN with naug = 8", fontsize = 20)
    plt.legend(bbox_to_anchor=(1.1,1))
    plt.show()