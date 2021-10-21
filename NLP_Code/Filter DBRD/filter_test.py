import glob
import re

neg = 0
pos = 0

filePath = ".\\test\\*\\*"
with open('test.txt', 'w', encoding="utf8") as outfile:
    for f in glob.glob(filePath):
        print(f)

        with open(f, encoding="utf8") as infile:
            rev = infile.read()
            words = rev.split(' ')
            if(len(words) <= 50):
                rev = re.sub(r'http\S+',' ',rev)
                
                rev = rev.replace('\n',' ')
                rev = rev.replace('\t', ' ')
                rev = rev.replace('-', ' ')
                rev = rev.replace('.', ' ')
                rev = rev.replace(':', ' ')

                rev = rev.replace(',', ' ')
                rev = rev.replace("'", '')
                rev = rev.replace("\"", '')
                rev = rev.replace('!', ' ')
                rev = rev.replace('?', ' ')

                rev = rev.replace('(', ' ')
                rev = rev.replace(')', ' ')

                rev = rev.replace('[', ' ')
                rev = rev.replace(']', ' ')

                rev = rev.replace('{', ' ')
                rev = rev.replace('}', ' ')

                rev = rev.replace(';', ' ')
                rev = rev.replace('/', ' ')

                rev = rev.replace('\\', ' ')
                rev = rev.replace('_', ' ')
                rev = rev.replace('+', ' ')
                rev = rev.replace('&', ' en ')

                clean_rev = re.sub(' +',' ',rev) #delete extra spaces
                clean_rev = clean_rev.lower()
                words = rev.split(' ')
                if(len(words) <= 50):
                    scoreText = f.split('_')[1].split('.')[0]
                    score = int(scoreText)
                    if (score > 3):
                        pos += 1
                        scoreText = '1'
                    else: 
                        neg += 1 
                        scoreText = '0'
                outfile.write(scoreText+'\t'+clean_rev+'\n')
    print("total neg: "+str(neg))
    print("total pos: "+str(pos))