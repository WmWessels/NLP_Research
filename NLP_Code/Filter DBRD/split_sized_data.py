import numpy as np

#set seed
np.random.seed(10)

#desired dataset sizes
size = [500, 1000, 2000, 10000]

for s in size:
    
    #to count balance
    neg = 0
    pos = 0

    #it takes the preprocessed train_orig.txt obtained from filter_data.py as its infile
    with open('train_'+str(s)+'.txt', 'w', encoding="utf8") as outfile:
        with open('train_orig.txt', 'r', encoding="utf8") as infile:
            
            #read txt into np array
            rev = np.array(infile.read().splitlines(True))

            #max array size
            max_size = len(rev)
            
            #randomize
            np.random.shuffle(rev)
            
            #make sure 's' isn't larger than the dataset size
            if s > max_size:
                s = max_size
            
            #set buffer of 20% incase there's not enough of one sentiment
            buffer = int(s*0.2)

            #if it results in the buffer increasing size above max dataset size change buffer + s = max_size
            if s+buffer > max_size:
                buffer = max_size - s
            
            #splice array for desired size + buffer
            lines_sized = rev[:s+buffer]
            
            #set max allowed of one sentiment to half the target size
            max_sentiment = int(s/2)
            
            #loop
            for ls in lines_sized:
                #read sentiment value
                sentiment = int(ls.split('\t')[0])
                #check if we maxed out on either sentiment then write
                if sentiment == 0 and neg < max_sentiment:
                    neg += 1
                    outfile.write(ls)
                elif sentiment == 1 and pos < max_sentiment:
                    pos += 1
                    outfile.write(ls)
                     
    print("Size "+str(s)+" with neg: "+str(neg)+", pos: "+str(pos))