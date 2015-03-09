from nltk.corpus import gutenberg

for sentence in gutenberg.sents('shakespeare-macbeth.txt'):
    # each sentence is a list of words
    print sentence 
