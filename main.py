import nltk
from nltk import word_tokenize
from nltk.corpus import wordnet as wn

REPL_TAGS = ['VB', 'JJ', 'RB']


#will permute emotion of sentence to desired emotion???
def permSentEmo(sentence):    
    tokens = word_tokenize(sentence)
    tagged_text = nltk.pos_tag(tokens)
    for i in range(len(tokens)):
        tag = tagged_text[i][1] 
        if(helper_PosToReplace(tag, REPL_TAGS)):
            #replace this with however you want to replace the word
            print("replace: " + tokens[i] + " tag: " + tag)

   
    #for tag in tagged_text:

        
#comes up with possible replacement words
def replacementWords(word):
    temp_synset = wn.synsets(word)
    #takes all the hyponyms of the hypernym(only one hypernym
    temp_hyponyms = temp_synset[0].hypernyms()[0].hyponyms()
    replWords = []
    for x in temp_hyponyms:
        replWords.append(x.lemmas()[0].name())

    return replWords

def selectReplWord(words, sentence):
    return words[0]

def helper_PosToReplace(tag, tags):
    for pos in tags:
        if(tag[0:2] == pos):
            return True

    return False

def testing():
    tag = 'JJJ'
    sentence = "I don't like my life, it is long and really hard"

    print(helper_PosToReplace(tag, REPL_TAGS))
    print(replacementWords('talked'))
    permSentEmo(sentence)

testing()

    




