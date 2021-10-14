import glob

neg = 0
pos = 0

filePath = ".\\test\\*\\*"
with open('test.txt', 'w', encoding="utf8") as outfile:
    for f in glob.glob(filePath):
        print(f)

        with open(f, encoding="utf8") as infile:
            rev = infile.read()
            r = rev.splitlines(True)
            if (len(r) <= 1):
                
                scoreText = f.split('_')[1].split('.')[0]
                score = int(scoreText)
                if (score > 3):
                    pos += 1
                    scoreText = '1'
                else: 
                    neg += 1 
                    scoreText = '0'
                outfile.write(scoreText+'\t'+rev+'\n')
                print("total neg: "+str(neg))
                print("total pos: "+str(pos))