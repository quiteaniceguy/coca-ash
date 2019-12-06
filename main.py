import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet as wn

#Tokenizes sentences
sent = "this is my sentence"
text = word_tokenize(sent)
#print(nltk.pos_tag(text))


test_synset = wn.synsets('talked')
#print(test_synset)
#print(test_synset[0].hypernyms())
#print(test_synset[0].hypernyms()[0].hyponyms())
def return 
def replacementWords(word):
    temp_senset = wn.synsets(word)
    #takes all the hyponyms of the hypernym(only one hypernym
    temp_hyponyms = test_synset[0].hypernyms()[0].hyponyms()
    replWords = []
    for x in temp_hyponyms:
        replWords.append(x.lemmas()[0].name())

    return replWords

print(replacementWords('talked'))

    




