
import similarity
!curl 'http://www.gutenberg.org/files/11/11-0.txt' -o aliceText.txt
# take all words from alice and store them in memory

aliceFile = open("aliceText.txt")

wordCorpus = []

for line in aliceFile:
    
    # remove newlines
    line = line.strip().lower()
    
    # get words
    words = line.split(" ")
    
    for word in words:
        if word.isalnum():
            if word not in wordCorpus:
                wordCorpus.append(word)
                
print similarity.similarity("rabbi",wordCorpus)